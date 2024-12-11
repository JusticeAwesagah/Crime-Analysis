{
    "metadata": {
        "kernelspec": {
            "name": "SQL",
            "display_name": "SQL",
            "language": "sql"
        },
        "language_info": {
            "name": "sql",
            "version": ""
        }
    },
    "nbformat_minor": 2,
    "nbformat": 4,
    "cells": [
        {
            "cell_type": "markdown",
            "source": [
                "#"
            ],
            "metadata": {
                "azdata_cell_guid": "e93e0a93-d758-4b73-8d5f-987d110ce2f2"
            },
            "attachments": {}
        },
        {
            "cell_type": "markdown",
            "source": [
                "### **Crime Analysis Database for Los Angeles**\n",
                "\n",
                "### Introduction\n",
                "\n",
                "Welcome to the **Crime Analysis Database for Los Angeles (LA, USA)**, a comprehensive resource designed to explore crime trends in the city over the past five years, from **2020 to 2024**. This database offers valuable insights into how different age groups, crime categories, and gender identities are represented across various criminal activities in LA, helping researchers, policymakers, and the public understand the complexities of crime in this vibrant urban area. The data is organized by key demographic and crime-related factors:\n",
                "\n",
                "1. **Age Categories**: **Infants**          <span style=\"color: var(--vscode-foreground);\">&nbsp;,</span>**Children**          <span style=\"color: var(--vscode-foreground);\">&nbsp;,</span>**Adolescents**          <span style=\"color: var(--vscode-foreground);\">&nbsp;,</span>**Adults**          <span style=\"color: var(--vscode-foreground);\">&nbsp;and&nbsp;</span>          **Elderly** \n",
                "    \n",
                "2. **Crime Categories**: \\*\\*Violent Crime,\\*\\***Property Crime** <span style=\"color: var(--vscode-foreground);\">and&nbsp;</span>          **Quality of Life Offenses**\n",
                "    \n",
                "3. **Gender Categories**<span style=\"color: var(--vscode-foreground);\">:&nbsp;</span>          **Male,** **Female** <span style=\"color: var(--vscode-foreground);\">and</span> **Other**\n",
                "    \n",
                "\n",
                "By examining these factors, this database enables an in-depth analysis of how crime patterns vary across different segments of the population, shedding light on trends and disparities that can inform more effective crime prevention, policy development, and community engagement. This resource is ideal for understanding the evolving dynamics of crime in Los Angeles, offering a granular perspective that can support efforts in building a safer and more equitable city. **The Crime Analysis Seek to Answer The Following Questions**\n",
                "\n",
                "1. <span style=\"color: var(--vscode-foreground);\">How does crime rates differ across various age category (infant, child, adolescent, adult, elderly) in Los Angeles between 2020 and 2024?</span>\n",
                "2. What is the distribution of violent crimes, property crimes, and quality of life offenses across different age categories in LA over the past five years?\n",
                "3. How does the gender distribution (male, female, other) correlate with the incidence of various crime categories, such as violent crime, property crime, and quality of life offenses?\n",
                "4. What are the trends in crime rates for each demographic (age and gender) over the years 2020 to 2024, and are there any noticeable increases or decreases in specific categories?\n",
                "5. Are certain age groups or genders disproportionately affected by particular types of crimes, and if so, what implications does this have for crime prevention and social support programs in LA? Using SQL Server Management Studio to Create Database The steps in creating the database and its associated schemas are guided by the techniques outlined in the \\[W3Schools\\](https:\\\\[www.w3schools.com\\\\\\\\sql\\\\\\\\sql\\\\\\_create\\\\\\_table.asp](http:\\www.w3schools.com\\sql\\sql_create_table.asp)). The \\[W3Schools\\](https:\\\\[www.w3schools.com\\\\\\\\sql\\\\\\\\sql\\\\\\_foreignkey.asp](http:\\www.w3schools.com\\sql\\sql_foreignkey.asp)) tutorial was used for all constraints in the Ampo\\\\\\_Tech database for the project. Using SQL Server Management Studio to Create Database The steps for creating the database and its schemas are based on techniques from W3Schools<span style=\"color: var(--vscode-foreground);\">(https:&lt;/span&gt;<a href=\"http://www.w3schools.com/sql/sql_create_table.asp\" data-href=\"http:\\www.w3schools.com\\sql\\sql_create_table.asp\" title=\"http:\\www.w3schools.com\\sql\\sql_create_table.asp\" is-markdown=\"true\" is-absolute=\"false\">www.w3schools.com\\sql\\sql_create_table.asp</a><span style=\"color: var(--vscode-foreground);\">)</span><span style=\"color: var(--vscode-foreground);\">. The&nbsp;</span>W3Schools<span style=\"color: var(--vscode-foreground);\">(https:&lt;/span&gt;<a href=\"http://www.w3schools.com/sql/sql_foreignkey.asp\" data-href=\"http:\\www.w3schools.com\\sql\\sql_foreignkey.asp\" title=\"http:\\www.w3schools.com\\sql\\sql_foreignkey.asp\" is-markdown=\"true\" is-absolute=\"false\">www.w3schools.com\\sql\\sql_foreignkey.asp</a><span style=\"color: var(--vscode-foreground);\">)&nbsp;</span>&nbsp;<span style=\"color: var(--vscode-foreground);\">tutorial was used for all constraints in the Awesagah_2024 database for the project.</span></span></span> Database Creation\n",
                "\n",
                "```\n",
                "CREAT DATBASE AWESAGAH_2024\n",
                "\n",
                "```"
            ],
            "metadata": {
                "azdata_cell_guid": "20588add-d8f7-4add-ab81-ff8081cda483"
            },
            "attachments": {}
        },
        {
            "cell_type": "markdown",
            "source": [
                "Using SQL Server Management Studio to Create Database\n",
                "\n",
                "The steps for creating the database and its schemas are based on techniques from [W3Schools]()<span style=\"color: var(--vscode-foreground);\">(https:\\</span>[www.w3schools.com\\\\\\\\sql\\\\\\\\sql\\\\\\_create\\\\\\_table.asp](http:\\www.w3schools.com\\sql\\sql_create_table.asp)<span style=\"color: var(--vscode-foreground);\">)</span><span style=\"color: var(--vscode-foreground);\">. The </span> [W3Schools]()<span style=\"color: var(--vscode-foreground);\">(https:\\</span>[www.w3schools.com\\\\\\\\sql\\\\\\\\sql\\\\\\_foreignkey.asp](http:\\www.w3schools.com\\sql\\sql_foreignkey.asp)<span style=\"color: var(--vscode-foreground);\">)&nbsp;</span> <span style=\"color: var(--vscode-foreground);\">tutorial was used for all constraints in the Awesagah_2024 database for the project.</span>"
            ],
            "metadata": {
                "azdata_cell_guid": "8ed643fc-b9a7-4936-b44a-f7967099996e"
            },
            "attachments": {}
        },
        {
            "cell_type": "markdown",
            "source": [
                "Database Creation\n",
                "```\n",
                "CREATE DATABASE AWESAGAH_2024\n",
                "```"
            ],
            "metadata": {
                "azdata_cell_guid": "538c165f-3e34-412b-bf22-ea1ee1291fc3"
            },
            "attachments": {}
        },
        {
            "cell_type": "markdown",
            "source": [
                "Create the following Schemas in the Awesagah\\_2024 database\n",
                "\n",
                "Dim\n",
                "\n",
                "Fact\n",
                "\n",
                "Stage\n",
                "\n",
                "```\n",
                "/**********************************************************/\n",
                "/********************Schema DDL****************************/\n",
                "/**********************************************************/\n",
                "```\n",
                "```\n",
                "IF NOT EXISTS (SELECT * FROM sys.schemas WHERE NAME = 'dim')\n",
                "BEGIN\n",
                "    EXEC ('CREATE SCHEMA dim AUTHORIZATION dbo;')\n",
                "END;\n",
                "GO \n",
                "\n",
                "```\n",
                "```\n",
                "IF NOT EXISTS (SELECT * FROM sys.schemas WHERE NAME = 'stg')\n",
                "BEGIN \n",
                "    EXEC('CREATE SCHEMA stg AUTHORIZATION dbo;');\n",
                "END;\n",
                "GO\n",
                "\n",
                "```\n",
                "```\n",
                "IF NOT EXISTS (SELECT * FROM sys.schemas WHERE NAME = 'Fact')\n",
                "BEGIN\n",
                "    EXEC('CREATE SCHEMA Fact AUTHORIZATION dbo;');\n",
                "END;\n",
                "G0\n",
                "\n",
                "```"
            ],
            "metadata": {
                "azdata_cell_guid": "cc00c8da-3ebb-4063-9bd3-3a1c62ba1cbf"
            },
            "attachments": {}
        },
        {
            "cell_type": "markdown",
            "source": [
                "**Creation of Dimension**\n",
                "\n",
                "<span style=\"color: var(--vscode-foreground);\">The project followed the principles outlined by [</span>Ralph Kimball\\](https:\\\\[www.kimballgroup.com\\\\\\\\\\\\\\\\data-warehouse-business-intelligence-resources\\\\\\\\\\\\\\\\books\\\\\\\\\\\\\\\\data-warehouse-dw-toolkit\\\\\\\\\\\\\\\\](http:\\www.kimballgroup.com\\data-warehouse-business-intelligence-resources\\books\\data-warehouse-dw-toolkit\\) <span style=\"color: var(--vscode-foreground);\">to develop the following dimensions and Fact for the project:</span>\n",
                "\n",
                "- dim.CrimeCategory\n",
                "- dim.AgeCategory\n",
                "- dim.Calendar\n",
                "- dim.Gender\n",
                "- Fact"
            ],
            "metadata": {
                "azdata_cell_guid": "4d27f0db-0398-4ca1-88e9-d8bae98b3fe0"
            },
            "attachments": {}
        },
        {
            "cell_type": "markdown",
            "source": [
                "**Creation of Dim.CrimeCategory**\n",
                "\n",
                "```\n",
                "/**********************************************************/\n",
                "/********************Dim.CrimeCategory*********************/\n",
                "/**********************************************************/\n",
                "\n",
                "IF NOT EXISTS  (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = 'dim'  AND  TABLE_NAME = 'CrimeCategory' )\n",
                "BEGIN\n",
                "    CREATE TABLE dim.CrimeCategory (\n",
                "    ID_crimeCategory INT NOT NULL,\n",
                "    CrimeCategory NVARCHAR(50) NOT NULl\n",
                "        );\n",
                "END;\n",
                "GO\n",
                "\n",
                "----Modifying the Gender table to have a primary key\n",
                "ALTER TABLE dim.CrimeCategory\n",
                "ADD CONSTRAINT PK_CrimeCategory PRIMARY KEY (ID_CrimeCategory)\n",
                "\n",
                "```"
            ],
            "metadata": {
                "azdata_cell_guid": "ab026f0b-3ed9-482a-ab52-a77b379eb973"
            },
            "attachments": {}
        },
        {
            "cell_type": "markdown",
            "source": [
                "**Creation of Dim.AgeCategory**\n",
                "\n",
                "```\n",
                "/**********************************************************/\n",
                "/********************Dim.AgeCategory***********************/\n",
                "/**********************************************************/\n",
                "IF NOT EXISTS  (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = 'dim'  AND  TABLE_NAME = 'AgeCategory' )\n",
                "BEGIN\n",
                "CREATE TABLE dim.AgeCategory (\n",
                "    ID_Age_Category INT NOT NULL,\n",
                "    Age_Category NVARCHAR(50) NOT NULL,\n",
                "        );\n",
                "END;\n",
                "GO\n",
                "\n",
                "----Modifying the Gender table to have a primary key\n",
                "\n",
                "ALTER TABLE dim.AgeCategory\n",
                "ADD CONSTRAINT PK_AgeCategory PRIMARY KEY (ID_Age_Category)\n",
                "\n",
                "```"
            ],
            "metadata": {
                "azdata_cell_guid": "55a05a80-ea87-4c18-9e82-87079eef16e9"
            },
            "attachments": {}
        },
        {
            "cell_type": "markdown",
            "source": [
                "**Creation of Dim.Calender**\n",
                "\n",
                "```\n",
                "/**********************************************************/\n",
                "/********************Dim.Calender**************************/\n",
                "/**********************************************************/\n",
                "\n",
                "IF NOT EXISTS  (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = 'dim'  AND  TABLE_NAME = 'Calender')\n",
                "BEGIN\n",
                " CREATE TABLE dim.Calender\n",
                "    (\n",
                "    [Date] Date NOT NULL,\n",
                "    Month NVARCHAR(50) NOT NULL,\n",
                "    Year NVARCHAR(50) NOT NULL\n",
                "        );\n",
                "END;\n",
                "GO\n",
                "\n",
                "\n",
                "\n",
                "ALTER TABLE dim.Calender\n",
                "ADD CONSTRAINT PK_Date PRIMARY KEY ([Date])\n",
                "\n",
                "```"
            ],
            "metadata": {
                "azdata_cell_guid": "5d0949b0-8f35-4367-8e16-3d0adb59e920"
            },
            "attachments": {}
        },
        {
            "cell_type": "markdown",
            "source": [
                "**Creation of Dim.Gender**  \n",
                "\n",
                "```\n",
                "/*********************************************************/\n",
                "/********************Dim.Gender****************************/\n",
                "/**********************************************************/\n",
                "IF NOT EXISTS  (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = 'dim'  AND  TABLE_NAME = 'Gender')\n",
                "BEGIN\n",
                "    CREATE TABLE dim.Gender\n",
                "(\n",
                "    IDGender INT NOT NULL,\n",
                "    Gender NVARCHAR(6) NOT NULL\n",
                ");\n",
                "END;\n",
                "GO\n",
                "\n",
                "\n",
                "----Modifying the Gender table to have a primary key  \n",
                "\n",
                "ALTER TABLE Dim.Gender\n",
                "ADD CONSTRAINT PK_Gender_ID PRIMARY KEY (IDGender)\n",
                "\n",
                "\n",
                "```"
            ],
            "metadata": {
                "azdata_cell_guid": "ae279db6-08ee-4c0a-9895-fe0907b08f31"
            },
            "attachments": {}
        },
        {
            "cell_type": "markdown",
            "source": [
                "**Creation of Fact Table**\n",
                "\n",
                "```\n",
                "/**********************************************************/\n",
                "/********************  Fact.Fact **************************/\n",
                "/**********************************************************/\n",
                "IF NOT EXISTS  (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = 'fact'  AND  TABLE_NAME = 'fact')\n",
                "BEGIN\n",
                "   CREATE TABLE Fact.Fact\n",
                "\t(\n",
                "\tDR_NO Time(7) NOT NULL,\n",
                "\t[DATE] Date NOT NULL,\n",
                "\tID_CrimeCategory INT NOT NULL,\n",
                "\tID_Age_Category INT NOT NULL,\n",
                "\tIDGender INT NOT NULL,\n",
                "\tAreaName NVARCHAR(50) NOT NULL,\n",
                "\tCrm_Cd INT NOT NULL,\n",
                "\tTypeOfCrime NVARCHAR(100) NOT NULL,\n",
                "\tCrimeCategory NVARCHAR(100) NOT NULL,\n",
                "\tMocodes NVARCHAR(50) NULL,\n",
                "\tVictim_Age INT NOT NULL,\n",
                "\tAge_Category NVARCHAR(50) NOT NULL,\n",
                "\tGender NVARCHAR(50) NOT NULL,\n",
                "\tPremis_Cd INT NOT NULL,\n",
                "\tPremis_Desc NVARCHAR(100) NOT NULL,\n",
                "\tStatus_Desc NVARCHAR(50) NOT NULL,\n",
                "\t[LOCATION] NVARCHAR(50) NOT NULL,\n",
                "\tCross_Street NVARCHAR(50) NULL,\n",
                "\tLAT FLOAT NOT NULL,\n",
                "\tLON FLOAT NOT NULL,\n",
                "\t\t);\n",
                "END;\n",
                "GO\n",
                "\n",
                "ALTER TABLE Fact.Fact\n",
                "ADD CONSTRAINT FK_FttoAGECAT\n",
                "\tFOREIGN KEY (ID_Age_Category)              \n",
                "\t REFERENCES  dim.AgeCategory(ID_Age_Category) \n",
                ";\n",
                "\n",
                "ALTER TABLE Fact.Fact\n",
                "ADD CONSTRAINT FK_FttoCan\n",
                "\tFOREIGN KEY ([Date])              \n",
                "\t REFERENCES  dim.Calender([Date]) \n",
                ";\n",
                "\n",
                "\n",
                "ALTER TABLE Fact.Fact\n",
                "ADD CONSTRAINT FK_FttoCriCat\n",
                "\tFOREIGN KEY (ID_CrimeCategory)              \n",
                "\t REFERENCES  dim.Crimecategory(ID_CrimeCategory) \n",
                ";\n",
                "\n",
                "ALTER TABLE Fact.Fact\n",
                "ADD CONSTRAINT FK_FttoGen\n",
                "\tFOREIGN KEY (IDGender)             \n",
                "\t REFERENCES  dim.Gender(IDGender) \n",
                ";\n",
                "\n",
                "\n",
                "```"
            ],
            "metadata": {
                "azdata_cell_guid": "3fc300a4-9f70-4ed0-85d8-a5be16cd444c"
            },
            "attachments": {}
        },
        {
            "cell_type": "markdown",
            "source": [
                "**IMPORTING DATA FROM DATABASE**\n",
                "\n",
                "Importing datafrom SSMS, from Project database **Awesaagah\\_2024** and stg.schame into dim tables and  Fact Table\n",
                "\n",
                "- Importing from stg.Gender to Dim.Gender\n",
                "\n",
                "```\n",
                "INSERT INTO dim.Gender (IDGender, Gender)\n",
                "SELECT IDGender,\n",
                "       Gender  \n",
                "From Awesagah_2024.stg.Gender\n",
                ";\n",
                "```"
            ],
            "metadata": {
                "azdata_cell_guid": "20bbc5e2-dfc8-4469-be55-4407aaae120d"
            },
            "attachments": {}
        },
        {
            "cell_type": "markdown",
            "source": [
                "- Importing from stg.Calender to Dim.Calender\n",
                "\n",
                "```\n",
                "INSERT INTO dim.Calender ([Date], Month, Year)\n",
                "SELECT\tDate,\n",
                "\t    Month,\n",
                "\t     Year\n",
                "From Awesagah_2024.stg.Calender\n",
                "```"
            ],
            "metadata": {
                "azdata_cell_guid": "4b287a38-6a01-40ce-abcb-a9aa8e128e7c"
            },
            "attachments": {}
        },
        {
            "cell_type": "markdown",
            "source": [
                "- Importing from stg.CrimeCategory to Dim.CrimeCategory\n",
                "\n",
                "```\n",
                "INSERT INTO dim.CrimeCategory (ID_CrimeCategory, CrimeCategory)\n",
                "SELECT ID_CrimeCategory,\n",
                "\t   CrimeCategory \n",
                "From Awesagah_2024.stg.CrimeCategory\n",
                "```"
            ],
            "metadata": {
                "azdata_cell_guid": "d14c5f8b-e2ee-44a1-b3e4-cab43ba92a20"
            },
            "attachments": {}
        },
        {
            "cell_type": "markdown",
            "source": [
                "- Importing from stg.AgeCategory to Dim.AgeCategory\n",
                "\n",
                "```\n",
                "INSERT INTO dim.AgeCategory (ID_Age_Category, Age_Category)\n",
                "SELECT ID_Age_Category,\n",
                "\t   Age_Category \n",
                "From Awesagah_2024.stg.AgeCategory\n",
                "```"
            ],
            "metadata": {
                "azdata_cell_guid": "b60aedb3-0160-4bbe-ad10-bdfb7118b960"
            },
            "attachments": {}
        },
        {
            "cell_type": "markdown",
            "source": [
                "- Importing from stg.Fact to Fact.fact\n",
                "\n",
                "```\n",
                "INSERT INTO FACT.FACT (DR_NO, [DATE], ID_CrimeCategory,\tID_Age_Category, IDGender, AreaName, Crm_Cd, TypeOfCrime, CrimeCategory, Mocodes, Victim_Age, Age_Category, Gender, Premis_Cd, Premis_Desc, Status_Desc, [LOCATION], Cross_Street, LAT, LON)\n",
                "SELECT\tDR_NO,\n",
                "\t    [DATE],\n",
                "\tID_CrimeCategory,\n",
                "\tID_Age_Category,\n",
                "\tIDGender,\n",
                "\tAreaName,\n",
                "\tCrm_Cd,\n",
                "\tTypeOfCrime,\n",
                "\tCrimeCategory,\n",
                "\tMocodes,\n",
                "\tVictim_Age,\n",
                "\tAge_Category,\n",
                "\tGender,\n",
                "\tPremis_Cd,\n",
                "\tPremis_Desc,\n",
                "\tStatus_Desc,\n",
                "\t[LOCATION],\n",
                "\tCross_Street,\n",
                "\tLAT,\n",
                "\tLON\n",
                "From Awesagah_2024.stg.FACT\n",
                ";\n",
                "```"
            ],
            "metadata": {
                "azdata_cell_guid": "b0b2f4dd-9d18-448f-914f-846fbc13c3e0"
            },
            "attachments": {}
        }
    ]
}