CREATE TABLE users (
  user_id INT AUTO_INCREMENT PRIMARY KEY,
  username VARCHAR(100) UNIQUE NOT NULL,
  password_hash VARCHAR(255) NOT NULL,
  email VARCHAR(100) UNIQUE NOT NULL,
  full_name VARCHAR(100),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE collections (
  collection_id INT AUTO_INCREMENT PRIMARY KEY,
  user_id INT,
  collection_name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (user_id) REFERENCES users(user_id)
);

CREATE TABLE pages (
  page_id INT AUTO_INCREMENT PRIMARY KEY,
  collection_id INT,
  title VARCHAR(255) NOT NULL,
  page_type ENUM('Daily', 'Monthly', 'Task List', 'Tracker', 'Notes', 'Other') NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (collection_id) REFERENCES collections(collection_id)
);


CREATE TABLE tasks (
  task_id INT AUTO_INCREMENT PRIMARY KEY,
  page_id INT,
  task_name VARCHAR(255) NOT NULL,
  is_completed BOOLEAN DEFAULT FALSE,
  due_date DATE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (page_id) REFERENCES pages(page_id)
);


CREATE TABLE events (
  event_id INT AUTO_INCREMENT PRIMARY KEY,
  page_id INT,
  event_name VARCHAR(255) NOT NULL,
  event_date DATE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (page_id) REFERENCES pages(page_id)
);




CREATE TABLE logs (
  log_id INT AUTO_INCREMENT PRIMARY KEY,
  page_id INT,
  content TEXT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (page_id) REFERENCES pages(page_id)
);

CREATE TABLE habit_trackers (
  habit_id INT AUTO_INCREMENT PRIMARY KEY,
  page_id INT,
  habit_name VARCHAR(255) NOT NULL,
  target INT,  -- target number for tracking (e.g., 30 for 30 days in a month)
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (page_id) REFERENCES pages(page_id)
);

CREATE TABLE daily_logs (
  daily_log_id INT AUTO_INCREMENT PRIMARY KEY,
  page_id INT,
  log_date DATE NOT NULL,
  content TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (page_id) REFERENCES pages(page_id)
);

CREATE TABLE tags (
  tag_id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100) NOT NULL
);

CREATE TABLE task_tags (
  task_id INT,
  tag_id INT,
  PRIMARY KEY (task_id, tag_id),
  FOREIGN KEY (task_id) REFERENCES tasks(task_id),
  FOREIGN KEY (tag_id) REFERENCES tags(tag_id)
);
