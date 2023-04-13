CREATE DATABASE my_db;
USE my_db;
CREATE TABLE personals (
    id INT(10) NOT NULL AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    phone VARCHAR(10) NOT NULL,
    PRIMARY KEY (id)
);
INSERT INTO personals (name, phone)
VALUES
    ('minh', '0919566916'),
    ('hoang', '0589108058');

# create procedure
DELIMITER $
CREATE PROCEDURE psGetDataWithName(
	IN _name varchar(255)
)
BEGIN
	SELECT * FROM personals WHERE name LIKE CONCAT('%', _name, '%');
END $

CREATE PROCEDURE psGetPersons(
)
BEGIN
	SELECT * FROM personals;
END $

CREATE PROCEDURE psAddPerson(
	IN _name varchar(255),
	IN _phone varchar(10)
)
BEGIN
	INSERT INTO personals (name, phone)
	VALUES
	    (_name, _phone);
END $
DELIMITER ;
