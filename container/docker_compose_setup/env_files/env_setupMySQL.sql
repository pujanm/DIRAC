CREATE USER 'root'@'%' IDENTIFIED BY '$root_pass';
GRANT ALL ON *.* TO 'root'@'%' WITH GRANT OPTION;
FLUSH PRIVILEGES;