# IOT_Project


### Apache Server
```
sudo apt-get update
sudo apt-get upgrade
sudo apt install apache2 -y
hostname -I
sudo usermod -a -G www-data pi
sudo chown -R -f www-data:www-data /var/www/html

```
### MySql Database
#### Install and configure Mariadb
1. Install Mariadb
```
sudo apt install mariadb-server
```
2. Secure database (set password = 'root') Answer 'Y' to all prompts
```
sudo mysql_secure_installation
```
### Create a database
1. Access MySQL server and create database
```
sudo mysql -u root -p
```
2. Create main databse
```
CREATE DATABASE Details;
CREATE USER 'iotuser'@'localhost' IDENTIFIED BY 'iot2022';
GRANT ALL PRIVILEGES ON Details.* TO 'iotuser'@'localhost';
```
3. type 'quit' and then Enter to exit MySQL command terminal 
### Install phpmyadmin
1. Install phpmyadmin with teh command below
```
sudo apt-get install phpmyadmin
```
2. When asked which type of server you want to run it off, select **Apache2**
3. Configure PHPMyAdmin to connect to MySQL server by selecting **Yes** on the prompt
4. Set password for PHPMyAdmin. Use **iot2022** the one set for MYSQL server
5. Configure Apache for PHPMyAdmin
* Edit the **Apache2.conf** file
```
sudo nano /etc/apache2/apache2.conf
```
* Add the following line of code at the bottom of the file
```
Include /etc/phpmyadmin/apache.conf
```
* Press **CTrL+X**, then **Y** then **ENTER** to save and exit
6. Restart the Apache Service
```
sudo service apache2 restart
```
### Install Mariadb Connector for Python
```
pip3 install mariadb
```
