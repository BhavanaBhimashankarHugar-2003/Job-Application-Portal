CREATE_SCHEMA = """
CREATE SCHEMA IF NOT EXISTS `mydb`;
"""



Create_users_Table = """
CREATE TABLE IF NOT EXISTS mydb.Users( 
        name VARCHAR(45) NOT NULL, 
        email Varchar(120) Not NULL,   
        type VARCHAR(45) NOT NULL,
        password VARCHAR(45) NULL,  
        UNIQUE INDEX email_UNIQUE (email), 
        CHECK (type in ('Recruiter','Client')),
        PRIMARY KEY (email)   );
  """
Create_recruiter_Table = """
CREATE TABLE IF NOT EXISTS mydb.Recruiter(
  RID INT NOT NULL AUTO_INCREMENT,
  RName VARCHAR(45) NOT NULL,
  REmail VARCHAR(45) NOT NULL,
  CompanyName VARCHAR(45) NOT NULL,
  CompanyLocation VARCHAR(45) NOT NULL,
  RGender VARCHAR(2) NOT NULL,
  jobcount int NOT NULL AUTO_INCREMENT,
   PRIMARY KEY (RID),
   UNIQUE (REmail)
   );
  """

Create_RecruiterStats_Table = """
CREATE TABLE IF NOT EXISTS mydb.RecruiterStats (
  RID INT NOT NULL,
  TotalApplications INT NOT NULL,
  SuccessfulApplications INT NOT NULL,
  PRIMARY KEY (RID),
  FOREIGN KEY (RID) REFERENCES mydb.Recruiter(RID)
);
"""
Create_client_Table = """
CREATE TABLE IF NOT EXISTS mydb.Client (
  CID INT NOT NULL AUTO_INCREMENT,
  CName VARCHAR(45) NOT NULL,
  CEmail VARCHAR(45) NOT NULL,
  CAge INT NOT NULL,
  CLocation VARCHAR(45) NOT NULL,
  CGender VARCHAR(2) NOT NULL,
  CExp INT NOT NULL,
  CSkills VARCHAR(45) NOT NULL,
  CQualification VARCHAR(45) NOT NULL,
  UNIQUE (CEmail),
  PRIMARY KEY (CID)
  );
  """

Create_Job_Table = """
CREATE TABLE IF NOT EXISTS mydb.Job (
  RID INT NOT NULL,
  JID INT NOT NULL AUTO_INCREMENT,
  JobRole VARCHAR(45) NOT NULL,
  JobType VARCHAR(45) NOT NULL,
  Qualification VARCHAR(45) NOT NULL,
  MinExp INT NOT NULL,
  Salary INT NOT NULL,
  FOREIGN KEY (RID) REFERENCES mydb.Recruiter(RID),
  PRIMARY KEY (JID)
  );
  """

Create_Application_Table="""
CREATE TABLE IF NOT EXISTS mydb.Application(
    AID INT NOT NULL AUTO_INCREMENT,
    RID INT NOT NULL,
    JID INT NOT NULL,
    CID INT NOT NULL,
    PRIMARY KEY(AID),
    FOREIGN KEY(RID) REFERENCES mydb.Recruiter(RID),
    FOREIGN KEY(JID) REFERENCES mydb.Job(JID),
    FOREIGN KEY(CID) REFERENCES mydb.Client(CID)
);
"""

"""CREATE TRIGGER application_check_qualification
    -> BEFORE INSERT ON mydb.Application
    -> FOR EACH ROW
    -> BEGIN
    ->   DECLARE job_qualification VARCHAR(45);
    ->   DECLARE client_qualification VARCHAR(45);
    ->
    ->   SELECT Qualification INTO job_qualification FROM mydb.Job WHERE JID = NEW.JID;
    ->   SELECT CQualification INTO client_qualification FROM mydb.Client WHERE CID = NEW.CID;
    ->
    ->   IF job_qualification != client_qualification THEN
    ->     SIGNAL SQLSTATE '45000'
    ->     SET MESSAGE_TEXT = 'Client does not have the required qualification for this job';
    ->   END IF;
    -> END;
    -> //
"""

""" CREATE FUNCTION CalculateAverageSalary( RID integer)
    -> RETURNS DECIMAL(10, 2)
    -> READS SQL DATA
    -> BEGIN
    ->     DECLARE avg_salary DECIMAL(10, 2);
    ->
    ->     SELECT AVG(Salary) INTO avg_salary
    ->     FROM mydb.Job as j
    ->     WHERE j.RID = RID;
    ->
    ->     RETURN avg_salary;
    -> END //"""

"""DELIMITER //

CREATE PROCEDURE GetRecruiterJobCount(job_type VARCHAR(45))
READS SQL DATA
BEGIN
    -- Use a nested query with JOIN to get recruiter information and job count
    SELECT r.RName, r.REmail, COUNT(j.JID) AS TotalJobs
    FROM mydb.Recruiter r
    LEFT JOIN mydb.Job j ON r.RID = j.RID
    WHERE j.JobType = job_type OR j.JobType IS NULL
    GROUP BY r.RID;
END //

DELIMITER ;"""
