# Project 2: Database Interaction and Dashboard Visualization

Data overview
The U.S. Department of Transportation's (DOT) Bureau of Transportation Statistics tracks the on-time performance of domestic flights operated by large air carriers. 
Summary information on the number of on-time, delayed, canceled, and diverted flights is published in DOT's monthly Air Travel Consumer Report and in this dataset of 2015 flight delays and cancellations.

## Google Drive Link

You can find additional resources and files on my [Google Drive](https://drive.google.com/drive/folders/1TifXhB__dN8cevwN88kywFwqkGrD7OKB?usp=sharing)


## Using Python's SQLAlchemy ORM to connect to a PostgreSQL database
This part demonstrates how to use Python's SQLAlchemy ORM to connect to a PostgreSQL database, retrieve data from a specific table, and visualize the data using Dash, a web application framework for Python.

Technologies Used
SQLAlchemy: An ORM (Object Relational Mapper) that allows you to interact with the database using Python objects.
PostgreSQL: The database system used to store and manage data.
Dash: A Python framework for building analytical web applications.
Features
Database Connection and Data Retrieval:

Connect to a PostgreSQL database using SQLAlchemy.
Define an ORM model for the 'airports' table within the 'project_2' schema.
Fetch data from the 'airports' table and convert it to a Pandas DataFrame for further processing.

Data Visualization: http://127.0.0.1:8050/


