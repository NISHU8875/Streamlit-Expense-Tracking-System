# Sreamlit Expense Tracking System

This project is an expense management system that consists of a Streamlit frontend application and a FastAPI backend server.


## Project Structure

- **frontend/**: Contains the Streamlit application code.
- **backend/**: Contains the FastAPI backend server code.
- **tests/**: Contains the test cases for both frontend and backend.
- **requirements.txt**: Lists the required Python packages.
- **README.md**: Provides an overview and instructions for the project.


## Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/expense-management-system.git
   cd expense-management-system
   ```
1. **Install dependencies:**:   
   ```commandline
    pip install -r requirements.txt
   ```
1. **Run the FastAPI server:**:



## 🌟 Features

- **📝 Add/Update Expenses**: Track daily expenses with amounts, categories, and notes
- **📊 Analytics by Category**: Visualize spending patterns across different expense categories
- **📈 Monthly Analytics**: View expense trends and breakdowns by month
- **💾 Cloud Database**: Persistent data storage using Railway MySQL
- **🎨 Modern UI**: Clean, responsive interface with gradient designs and smooth interactions
- **⚡ Real-time Updates**: Instant data synchronization between frontend and backend

## 🚀 Live Application

- **Frontend (Streamlit)**: https://app-expense-tracking-system-nishu-kumar.streamlit.app/


## 🛠️ Tech Stack

### Frontend
- **Streamlit** - Interactive web application framework
- **Pandas** - Data manipulation and analysis
- **Requests** - HTTP library for API communication

### Backend
- **FastAPI** - Modern, high-performance web framework
- **Uvicorn** - ASGI server
- **Pydantic** - Data validation using Python type annotations
- **MySQL Connector** - Database connectivity

### Database
- **Railway MySQL** - Cloud-hosted MySQL database

### Deployment
- **Render** - Backend API hosting
- **Streamlit Cloud** - Frontend application hosting

## 📋 Prerequisites

- Python 3.10+
- MySQL 8.0+
- pip (Python package manager)

## 🔧 Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/NISHU8875/Streamlit-Expense-Tracking-System.git
cd Streamlit-Expense-Tracking-System
```

### 2. Backend Setup

```bash
cd backend
pip install -r requirements.txt
```

Create a `.env` file in the backend directory:
```

Run the backend server:
```bash
uvicorn server:app --host 0.0.0.0 --port 8000
```

### 3. Database Setup

Import the database schema:
```bash
mysql -h your_host -u root -p railway < database/expense_db_creation.sql
```

### 4. Frontend Setup

```bash
cd frontend
pip install -r requirements.txt
```

Update `API_URL` in the following files:
- `add_update.py`
- `analytics_by_category.py`
- `analytics_by_months.py`

Run the Streamlit app:
```bash
streamlit run app.py
```

## 📁 Project Structure

```
Streamlit-Expense-Tracking-System/
├── backend/
│   ├── server.py              # FastAPI application
│   ├── db_helper.py           # Database operations
│   ├── logging_setup.py       # Logging configuration
│   └── requirements.txt       # Backend dependencies
├── frontend/
│   ├── app.py                 # Main Streamlit app
│   ├── add_update.py          # Add/Update expenses tab
│   ├── analytics_by_category.py  # Category analytics
│   ├── analytics_by_months.py    # Monthly analytics
│   └── requirements.txt       # Frontend dependencies
├── database/
│   └── expense_db_creation.sql   # Database schema
└── README.md
```

## 🔌 API Endpoints

### Base URL: `https://streamlit-expense-tracking-system-nishu-4wkv.onrender.com`

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | API root - health check |
| GET | `/health` | Health status |
| GET | `/expenses/{date}` | Get expenses for a specific date |
| POST | `/expenses/{date}` | Add/update expenses for a date |
| POST | `/analytics/` | Get expense breakdown by category |
| GET | `/monthly_summary/` | Get monthly expense summary |

### Example API Requests

**Get Expenses:**
```bash
curl https://streamlit-expense-tracking-system-nishu-4wkv.onrender.com/expenses/2024-08-02
```

**Add Expenses:**
```bash
curl -X POST https://streamlit-expense-tracking-system-nishu-4wkv.onrender.com/expenses/2024-08-02 \
  -H "Content-Type: application/json" \
  -d '[{"amount": 50, "category": "Food", "notes": "Lunch"}]'
```

## 💡 Key Features Explained

### 1. Add/Update Expenses
- Select any date and view existing expenses
- Add multiple expense entries at once
- Categories: Rent, Food, Shopping, Entertainment, Other
- Real-time validation and error handling

### 2. Analytics by Category
- Choose date range for analysis
- View percentage breakdown by category
- Interactive bar charts
- Detailed data table with totals

### 3. Monthly Analytics
- Automatic monthly expense aggregation
- Bar chart visualization by month
- Sortable data table
- Historical trend analysis

## 🔐 Environment Variables

### Backend (Render)
```env
DB_HOST=shinkansen.proxy.rlwy.net
DB_PORT=38397
DB_USER=root
DB_PASSWORD=your_railway_password
DB_NAME=railway
```

### Frontend (Streamlit Cloud)
No environment variables needed - API URL is configured in code.

## 🎨 UI/UX Highlights

- Clean, modern design with gradient themes
- Responsive layout for all screen sizes
- Smooth animations and transitions
- Color-coded categories
- Interactive data visualizations
- User-friendly forms with validation

## 📊 Database Schema

### `expenses` Table
```sql
CREATE TABLE expenses (
  id INT PRIMARY KEY AUTO_INCREMENT,
  expense_date DATE NOT NULL,
  amount FLOAT NOT NULL,
  category VARCHAR(255) NOT NULL,
  notes TEXT,
  INDEX idx_date (expense_date)
);
```

## 🚀 Deployment

### Backend (Render)
1. Connected GitHub repository
2. Set environment variables in Render dashboard
3. Build command: `pip install -r backend/requirements.txt`
4. Start command: `uvicorn backend.server:app --host 0.0.0.0 --port $PORT`

### Frontend (Streamlit Cloud)
1. Connected GitHub repository
2. Main file path: `frontend/app.py`
3. Python version: 3.10
4. Automatic deployment on push

### Database (Railway)
1. Created MySQL database instance
2. Imported schema and sample data
3. Configured public access with proxy URL

## 🐛 Troubleshooting

**Issue: Cannot connect to database**
- Verify environment variables are set correctly
- Check Railway database is running
- Ensure firewall allows connections from Render

**Issue: Frontend shows 500 error**
- Verify API_URL is set to production endpoint
- Check backend logs on Render
- Ensure database tables exist

**Issue: No data displayed**
- Import the SQL file to create tables
- Check database connection credentials
- Verify API endpoints are accessible

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📧 Contact

**Nishu Kumar**
- GitHub: [@NISHU8875](https://github.com/NISHU8875)

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

⭐ If you found this project helpful, please give it a star!
