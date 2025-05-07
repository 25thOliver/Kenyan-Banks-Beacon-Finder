from pypdf import PdfReader
import json

# Initialize storage
bank_dict = {}

# Load the PDF
reader = PdfReader("Bank-and-Branches-July-2023v.pdf")
print("📄 Reading PDF and extracting data...")

for page in reader.pages:
    text = page.extract_text()
    lines = text.strip().split("\n")

    for line in lines:
        words = line.strip().split()

        if len(words) < 4:
            continue  # Skip too-short lines

        # Find bank code (2-digit) and branch code (3-digit)
        for i in range(len(words) - 2):
            if words[i].isdigit() and len(words[i]) == 2 and words[i + 1].isdigit() and len(words[i + 1]) == 3:
                bank_name = " ".join(words[:i])
                bank_code = words[i]
                branch_code = words[i + 1]
                branch_name = " ".join(words[i + 2:])

                # Store in structured format
                if bank_name not in bank_dict:
                    bank_dict[bank_name] = {
                        "bank_code": bank_code,
                        "branches": []
                    }

                bank_dict[bank_name]["branches"].append({
                    "branch_code": branch_code,
                    "branch_name": branch_name
                })

                break

# Final structure as list of banks
bank_list = [
    {
        "bank_name": name,
        "bank_code": data["bank_code"],
        "branches": data["branches"]
    }
    for name, data in bank_dict.items()
]

# Write to JSON file
with open("banks_and_branches_structured.json", "w", encoding="utf-8") as f:
    json.dump(bank_list, f, indent=4)

print("✅ Done! Data saved to 'banks_and_branches_structured.json'")
