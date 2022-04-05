# API TO GET INFORMATION FROM PDF


# OVERVIEW
API that receives and saves pdf file, extracts and saves its text and meta-data in local database.  
API allows to retrieve text and meta-data of a pdf-file previously uploaded via its id.  
No authentication required


# MORE DETAILS

## What it can 
It can receive and analyse 'PDF' and 'pdf' files. Other files are rejected.  
In case user starts to request empty database, the user receives an error message.  
In case user requests unsupported id like character or a digit which is not in database range, the user receives an error message. 


## What it can not

It can recieve only one file at a time.  


## Application structure  

```
API_reading_pdf/  
├── flaskr  
│   ├── init.py  
│   ├── controller.py  
│   └── model.py  
├── tests  
│   └── test_**.py   (files contain code to test the app)  
├── uploads          (pdf-files storage, created automatically after app launch)  
├── venv             (virtual environment folder)  
├── pdf.db           (database file, created automatically after app launch)  
├── readme.md  
├── requirements.txt (list of required libs and packages)  
├── sample.pdf       (pdf file for tests)  
└── wsgi.py          (application entry point)  
```


# INSTALLATION (UBUNTU OS)

The application requires Python installed.  

 * For more details about Python installation, check the following link:  
 https://www.python.org/downloads/  

In folder "API_reading_pdf" create vitual environment  

* You can create it from command line:  
  ```
  virtualenv <my_env_name>
  ```
  where <my_env_name> is the name of the virtual environment you would like to create.  

  As an example, to create a virtual environment 'venv' you should type in terminal: 
  ```
  virtualenv venv
  ```
* If you do not have virtual environment tool installed, you can install it from command line:    
  ```
  sudo apt install python3-virtualenv
  ```

Activate the virtual environment you have just created:  
In Ubuntu:
```
source <my_env_name>/bin/activate
```
* In case you created virtual environment "venv" you activate it as follows:  
  ```
  source ./venv/bin/activate
  ```

* For more details about virtual environment, check the following link:  
  https://docs.python.org/3/tutorial/venv.html  

Install the packages that application requires by typing in command line:  
```
pip install -r requirements.txt
```


# TUTORIAL

## Run the application  

To run the application after installation, stay in folder "flask_reading_pdf" and type the following in command line:  
```
python wsgi.py
```
The application runs while the command line window is open.  

* You can check in your web-browser that the application works by typing in address line of your browser:  

  http://localhost:5000/  

  You should see text "Index page" in your browser

## Upload a pdf-file  

Open a new terminal window, to let your application run in previous terminal window  

To upload a pdf-file "sample.pdf" using command line, you can use curl-command  

* In case curl tool is not installed you can do this in command line:  
  ```
  sudo apt install curl   
  ```

In terminal, go to the folder where the file you want to send is located.  

You can find a sample.pdf file in "flask_reading_pdf" folder.  

To send sample.pdf file to application, type:  
```
curl -sF file=@"sample.pdf" http://localhost:5000/documents
```
* Standard response returns in the following format:  
  ```
  {
      "id": 1
  }
  ```
  where 1 is id number of the record in database.  

* At this moment the pdf-file is saved in 'API_reading_pdf-develop/uploads' on your local machine, text and metadata are saved in local sqlite database.  

* You should use this id to retrieve the information about the file.  


## Get metadata  

To retrive metadata about a file, you need its id (which is document_id) that you got from on the previous step.  
```
curl -s http://localhost:5000/documents/<document_id>
```
* where document_id should be replaced by a number.  

* In case you sent at least one file, you can retrieve metadata related to the record 1 in database by typing:  
  ```
  curl -s http://localhost:5000/documents/1
  ```
  
The standard response is in the following format:
```
{
  "author": "GPL Ghostscript SVN PRE-RELEASE 8.62",
  "creation_date": "D:20080201104827-05'00'",
  "creator": "dvips(k) 5.86 Copyright 1999 Radical Eye Software",
  "file_id": "tpvtajdvrlrqdecv",
  "link_to_content": "http://localhost:5000/text/1.txt",
  "modification_date": "D:20080201104827-05'00'",
  "status": "success"
}
```

Instead of curl, you can also retrieve metadata via web-browser  

Type in address line http://localhost:5000/documents/<document_id>  

* where document_id should be replaced by a number.  

* In case you sent at least one file, you can retrieve metadata related to the record 1 in database by typing:  

  http://localhost:5000/documents/1  


## Get text  

To retrive text from database, you need its document_id. Type the following in command line to retrieve it:  
```
curl -s http://localhost:5000/text/<document_id>.txt
```
* where document_id should be replaced by a number.  

* In case you sent at least one file, you can retrieve metadata related to the record 1 in database by typing:  
  ```
  curl -s http://localhost:5000/text/1.txt
  ```
* Keep in mind ".txt" after <document_id>

Standard response returns in the following format:  
```
{
    "text": "text from pdf"
}
```

Instead of curl, you can also retrieve text via web-browser  

Type in address line http://localhost:5000/text/<document_id>.txt 

* where document_id should be replaced by a number.  

* In case you sent at least one file, you can retrieve metadata related to the record 1 in database by typing:  

  http://localhost:5000/text/1.txt  


## Stop the application

To stop the application, type "ctr + C" in terminal window where it was launched or close the terminal window.  


## Test the application

To launch tests, go to the project's top-level directory "API_reading_pdf"  
and launch the following commands
Tests cover 97-98% of code    
```
export PYTHONPATH="venv/lib/python3.9/site-packages/"
```
```
coverage run -m pytest
```
```
coverage report
```
For more details, you can check what are the line numbers that were not covered in tests
```
coverage report -m
```
To create a detailed html report in "API_reading_pdf/htmlcov/index.html", type the following
```
coverage html
```

## Check code quality with Pylint

To check if the style of code in files is pythonic you can use Pylint.  
To do that stay in top-level directory "API_reading_pdf" and type
```
pylint ./flaskr
```
You can also check each file using  
```
pylint model.py
```