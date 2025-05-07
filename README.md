# Bank Beacon Finder

A modern web application designed to help users quickly search and find bank information in Kenya, without having to sift through lengthy documents.

---

## Problem Statement

While seeking comprehensive bank information from the Kenya Bankers Association, I found only a cumbersome 56-page PDF. Searching for specific details like branch codes or contact info was tedious and inefficient. To solve this, I built Bank Beacon Finder-a tool to automate and simplify the search process, providing instant access to bank details, contact info, working hours, and hints on non-working days (such as Sundays, national holidays, and limited Saturday hours).

---

## Table of Contents

- [Features](#features)
- [Usage](#usage)
- [Screenshots](#screenshots)
- [Technical Details](#technical-details)
- [Folder Structure](#folder-structure)
- [Getting Started](#getting-started)
- [Contributing](#contributing)
- [License](#license)

---

## Features

- **Powerful Search:** Find banks by name, code, branch name, or branch code.
- **Bank Filtering:** Filter results by specific bank names.
- **Detailed Information:** Access bank/branch names, codes, contact info, working hours, and location.
- **Real-time Status:** Instantly see if a bank is open or closed.
- **Quick Copy:** Click any bank card to copy its code.
- **Responsive Design:** Works seamlessly on desktop and mobile.
- **Pagination:** Easily navigate large result sets.
- **Non-Working Day Hints:** Highlights Sundays, national holidays, and Saturday limited hours (8am–12pm).

---

## Usage

1. Enter a bank name, code, branch name, or branch code in the search bar.
2. Use the bank filter dropdown to narrow results.
3. Click a search result to copy its bank code.
4. Use pagination controls to browse multiple results.

---

## Screenshots

![Search Interface](assets/screenshotsils](assets/screenshots/b Technical Details

Built with:

- **React + TypeScript:** Robust, scalable frontend.
- **Tailwind CSS:** Responsive, elegant styling.
- **Shadcn UI:** Consistent design system.
- **React Router:** Smooth navigation.
- **React Query:** Efficient data fetching.
- **Lucide React:** Scalable icons.

### Date and Time Utilities

- `parseTimeStringToDate`: Converts time strings (e.g., "9:00am") to JS Date objects.
- `isWeekend`: Checks if a date is a weekend.
- `isOpenNow`: Determines if a bank is currently open.
- `formatContactInfo`: Formats contact details for display.

### Component Structure

- **SearchBar:** User input for searches.
- **SearchResultCard:** Displays bank/branch info.
- **BankFilter:** Filter by bank.
- **InfoRow:** Reusable labeled info display.
- **WorkingHours:** Shows formatted hours.
- **BranchInfo:** Detailed branch data.

---

## Folder Structure

```
bank-beacon-finder/
├── README.md
├── node_modules/
├── package.json
├── .gitignore
├── public/
│   ├── favicon.ico
│   ├── index.html
│   └── manifest.json
└── src/
    ├── assets/
    │   └── screenshots/
    ├── components/
    │   ├── SearchBar.tsx
    │   ├── SearchResultCard.tsx
    │   ├── BankFilter.tsx
    │   ├── InfoRow.tsx
    │   ├── WorkingHours.tsx
    │   └── BranchInfo.tsx
    ├── utils/
    │   ├── dateUtils.ts
    │   └── formatContactInfo.ts
    ├── App.tsx
    ├── index.tsx
    ├── styles/
    │   └── tailwind.css
    └── data/
        └── banks.json
```

---

## Getting Started

### Prerequisites

- Node.js (v16+)
- npm or yarn

### Installation

```sh
git clone 
cd bank-beacon-finder
npm install
# or
yarn install
```

### Running the App

```sh
npm run dev
# or
yarn dev
```

Visit [http://localhost:5173](http://localhost:5173) in your browser.

---

## Contributing

Contributions are welcome! Please open an issue or submit a Pull Request.

