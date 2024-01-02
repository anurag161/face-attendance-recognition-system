## Overview

The Face Attendance Recognition Web App is a project aimed at automating the attendance tracking process using facial recognition technology and computer vision. The application is divided into two main parts: the frontend and the backend.

### Frontend

The frontend is built using HTML, CSS, and JavaScript to create an intuitive and user-friendly interface. It includes the following pages:

- **Login Page:** Allows students to log in to their accounts.
- **Signup Page:** Enables new users to create an account.
- **Dashboard:** Provides students with an overview of their attendance graph for a specific semester and allows them to choose their courses.

### Backend

The backend utilizes Django and Firebase for seamless integration and efficient data management. The facial recognition functionality is implemented using computer vision to record attendance. Here's how it works:

1. **Face Detection with Computer Vision:** When a student's face is detected, the information is processed using computer vision algorithms.
2. **Firebase Integration:** Firebase stores the facial recognition data securely.
3. **Excel Sheet Logging:** The attendance records are logged in an Excel sheet for easy access and reference.
4. **Teacher's Attendance List:** Teachers can view the attendance list, facilitating quick and accurate tracking.

## Setup

Follow these steps to set up and run the Face Attendance Recognition Web App locally:

1. **Frontend:**
   - Navigate to the `frontend` directory.
   - Open the `index.html` file in your browser.

2. **Backend:**
   - Navigate to the `backend` directory.
   - Install the required dependencies using `pip install -r requirements.txt`.
   - Run the Django development server with `python manage.py runserver`.

## Technologies Used

- **Frontend:**
  - HTML, CSS, JavaScript

- **Backend:**
  - Django
  - Firebase
  - Computer Vision for Face Detection

## Future Enhancements

This project is open for contributions and improvements. Future enhancements may include additional features, security updates, and optimization.

Feel free to contribute to make the Face Attendance Recognition Web App even more robust and user-friendly!
