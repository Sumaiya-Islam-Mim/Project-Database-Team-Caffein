<?php
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "bullet_journal";


$conn = new mysqli($servername, $username, $password, $dbname);


if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}
echo "Connected successfully";
?>




<?php
session_start(); // to store user info in session


// Assuming the user is logged in and user_id is stored in session
$user_id = $_SESSION['user_id'];
$entry_date = $_POST['entry_date']; // Date of the entry (from the form)
$content = $_POST['content']; // Content of the entry (from the form)


$servername = "localhost";
$username = "root";
$password = "";
$dbname = "bullet_journal";


$conn = new mysqli($servername, $username, $password, $dbname);


if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}


// Insert journal entry
$stmt = $conn->prepare("INSERT INTO entries (user_id, entry_date, content) VALUES (?, ?, ?)");
$stmt->bind_param("iss", $user_id, $entry_date, $content);


if ($stmt->execute()) {
    echo "New entry added successfully!";
} else {
    echo "Error: " . $stmt->error;
}


$stmt->close();
$conn->close();
?>




<?php
session_start(); // Ensure user is logged in and user_id is available
$user_id = $_SESSION['user_id'];


$servername = "localhost";
$username = "root";
$password = "";
$dbname = "bullet_journal";


$conn = new mysqli($servername, $username, $password, $dbname);


if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}


// Fetch user entries
$sql = "SELECT * FROM entries WHERE user_id = ?";
$stmt = $conn->prepare($sql);
$stmt->bind_param("i", $user_id);
$stmt->execute();


$result = $stmt->get_result();


if ($result->num_rows > 0) {
    while($row = $result->fetch_assoc()) {
        echo "Date: " . $row['entry_date'] . " - Content: " . $row['content'] . "<br>";
    }
} else {
    echo "No entries found.";
}


$stmt->close();
$conn->close();
?>




<?php
session_start();


$servername = "localhost";
$username = "root";
$password = "";
$dbname = "bullet_journal";


$conn = new mysqli($servername, $username, $password, $dbname);


if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}


if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $input_username = $_POST['username'];
    $input_password = $_POST['password'];


    // Get user from database
    $sql = "SELECT * FROM users WHERE username = ?";
    $stmt = $conn->prepare($sql);
    $stmt->bind_param("s", $input_username);
    $stmt->execute();
    $result = $stmt->get_result();


    if ($result->num_rows > 0) {
        $user = $result->fetch_assoc();
        // Verify password
        if (password_verify($input_password, $user['password'])) {
            $_SESSION['user_id'] = $user['user_id'];
            $_SESSION['username'] = $user['username'];
            echo "Login successful!";
        } else {
            echo "Invalid password.";
        }
    } else {
        echo "No user found with that username.";
    }
}


$conn->close();
?>









