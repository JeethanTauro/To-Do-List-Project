# Multi-User Role-Based Todo List Application

##  Project Description

**Multi-User Role-Based Todo List Application** backend application designed to support task management across multiple authenticated users with distinct roles and permissions. The system enables users to securely register and manage their personal todo lists, while administrators have elevated privileges to oversee and control user access. Key features include role-based authentication and authorization, promotion and demotion of user roles (from user to admin and vice versa), and the implementation of basic authentication mechanisms to ensure secure access control. This project emphasizes modularity, secure role management, and scalable design suitable for collaborative environments or administrative dashboards.

---

##  Features

*  Basic authentication using Spring Security
*  Role-based authentication and authorization (`USER`, `ADMIN`)
*  CRUD operations for todo tasks via REST APIs
*  MongoDB integration for persistence
*  Admins can view all users and their todo tasks
*  Promote user to admin /  Demote admin to user
*  Modular code structure with clear separation of concerns

---

##  Tech Stack

| Category       | Technology        |
| -------------- | ----------------- |
| Backend        | Java, Spring Boot |
| Database       | MongoDB           |
| Authentication | Spring Security   |
| Testing        | JUnit             |
| API Testing    | Postman           |

---

##  Folder Structure



```
src/main/java/com.todo.To_Do/
├── Controller/
│   ├── AdminController
│   ├── PublicController
│   └── TodoUserController
├── Entity/
│   ├── Roles
│   ├── ToDo
│   └── User
├── Repository/
│   ├── ToDoRepo
│   └── UserRepo
├── SecurityConfig/
│   ├── Config
│   ├── PasswordEncoderBean
│   └── UserServiceImpl
```

---

##  API Endpoints
| Method   | Endpoint                   | Description                                        |
| -------- | -------------------------- | -------------------------------------------------- |
| `POST`   | `/public`                  | Register a new user                                |
| `GET`    | `/todo/user`               | Get the authenticated user’s profile               |
| `PUT`    | `/todo/user`               | Update username/password of the authenticated user |
| `POST`   | `/todo/user`               | Add a new todo item for the authenticated user     |
| `PUT`    | `/todo/user/{id}`          | Update an existing todo item by ID                 |
| `DELETE` | `/todo/user/{id}`          | Delete a todo item by ID                           |
| `GET`    | `/todo/user/{id}`          | Get a specific todo item by ID                     |
| `GET`    | `/admin/all-users`         | Admin: Fetch all registered users                  |
| `GET`    | `/admin/all-admins`        | Admin: Fetch all admin users                       |
| `POST`   | `/admin/add-new-admin`     | Admin: Add a new admin user                        |
| `PUT`    | `/admin/promote-to-admin`  | Admin: Promote a regular user to admin             |
| `PUT`    | `/admin/demote-from-admin` | Admin: Demote an admin back to regular user        |


---

##  Setup Instructions

To set this project up on your local system from GitHub:

1. **Clone the repository**:

   ```bash
   git clone https://github.com/your-username/todo-app.git
   cd todo-app
   ```

2. **Import the project**:

   * Open in your favorite IDE (e.g., IntelliJ IDEA, Eclipse).
   * Ensure JDK 17+ and Maven are properly configured.

3. **Set up MongoDB**:

   * Make sure MongoDB is installed and running locally on default port `27017`.
   * You can configure database settings in `application.properties`.

4. **Configure `application.properties`**:

   ```properties
   spring.data.mongodb.uri=mongodb://localhost:27017/todo_db
   server.port=8080
   ```

5. **Build and run the application**:

   ```bash
   ./mvnw spring-boot:run
   ```

6. **Test APIs** using Postman:

   * Use endpoints from the table above.
   * Send credentials via Basic Auth to test protected routes.

---

##  Contact

**Author** : Jeethan Tauro, was happy to share this with you, wanna connect? Do reach out!

---

