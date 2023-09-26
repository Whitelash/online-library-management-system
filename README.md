# Online Library Management System

A local library is in dire need of a web application to ease their work. The library management system must allow a librarian to track books and their quantity, books issued to members, book fees. (It is of assumption that the app will be used by the librarian only.)

The following functionalities are expected from the application:
Base Library System
Librarians must be able to maintain:
- Books with stock maintained
- Members
- Transactions - [ Borrowing, Returns, Member registration, Member dismissal]
  
The use cases included here are to:
- Perform general CRUD operations on Books and Members
-	Issue a book to a member
- Issue a book return from a member
- Search for a book by name and author
- Charge a rent fee on book returns

## UML Diagrams
A UML diagram is a diagram based on the UML (Unified Modeling Language) with the purpose of visually representing a system along with its main actors, roles, actions, artifacts or classes, in order to better understand, alter, maintain, or document information about the system.

### Flow Diagram
A flow diagram is a visualization of a sequence of actions, movements within a system and/or decision points.

![flow_diag](/olms_screenshots/flowdiagram.PNG)

### Use Case Diagram
Use Case diagrams are used to analyze the system’s high-level requirements.

![usecase_diag](/olms_screenshots/usecase.png)

### Class Diagram
Class diagrams contain classes, alongside with their attributes (also referred to as data fields) and their behaviors (also referred to as member functions).

![class_diag](/olms_screenshots/classdiag.png)

### Sequential Diagram
Sequence diagrams describe the sequence of messages and interactions that happen between actors and objects. Actors or objects can be active only when needed or when another object wants to communicate with them. All communication is represented in a chronological manner.
 
![seq_diag](/olms_screenshots/seqdiag.png)

### Activity Diagram
Activity diagrams are generally used to describe the flow of different activities and actions. These can be both sequential and in parallel. They describe the objects used, consumed or produced by an activity and the relationship between the different activities. 

![act_diag](/olms_screenshots/activitydiag.png)


## Screenshots

![landpg](/olms_screenshots/landpage.png)
 
Landing Page

![homepg](/olms_screenshots/homepage.png)
 
Home Page

![categpg](/olms_screenshots/categ1.png)
![categ2pg](/olms_screenshots/categ2.png)
Categories Page

![addcategpg](/olms_screenshots/addcateg.png)

Add New Category Page

![crudcateg](/olms_screenshots/crudcateg.png)

View, Edit, and Delete a category from list.

![viewcategpg](/olms_screenshots/viewcateg.png)

View Category Details

![editcategpg](/olms_screenshots/editcateg.png)

Edit Category Details

![deletecategpg](/olms_screenshots/deletecateg.png)
 
Deleting Category

![subcategpg](/olms_screenshots/subcateg.png)
 
Sub-Categories Page

![addsubcategpg](/olms_screenshots/addsubcateg.png)

Add new Sub Category

![crudsubcategpg](/olms_screenshots/crudsubcateg.png)

View, Edit & Delete a Sub Category from the list.

![bookspg](/olms_screenshots/bookspage.png)
 
Books Page

![addbook1pg](/olms_screenshots/addbook.png)
![addbook2pg](/olms_screenshots/addbook2.png)
![addbook3pg](/olms_screenshots/addbook3.png)
 
Add new book page

![crudbookpg](/olms_screenshots/crudbook.png)
 
View, Edit, & Delete Book from the list

![studentpg](/olms_screenshots/studentpage.png)
 
Students Page

![addstudpg](/olms_screenshots/addstudent1.png)
![addstud2pg](/olms_screenshots/addstudent2.png)
 
Add student page

![transpg](/olms_screenshots/transactionspage.png)
 
Transactions Page

![libprofpg](/olms_screenshots/librarianprofile.png)
 
Librarian Profile

![updlibprofpg](/olms_screenshots/updatelibprofile.png)
 
Update Librarian Profile

![updlibpasspg](/olms_screenshots/updatelilbpassword.png)

Update Librarian Password

![db1pg](/olms_screenshots/db1.png)
![db2pg](/olms_screenshots/db2.png)

Database – DB browser for sqlite 
 









## References
1. https://www.bookbeaver.co.uk/blog/different-types-of-books A comprehensive guide to the different types of books
2. https://lisportal.quora.com/How-to-arrange-books-in-the-school-library#:~:text=Sort%20books%20by%20category%3A%20Sort,books%20on%20a%20particular%20topic. How do I arrange books in the school library?
3. https://www.pexels.com/photo/texture-wall-white-colors-1843717/ Free Plain Backgrounds Photos

4. https://tallyfy.com/uml-diagram/ All You Need to Know About UML Diagrams: Types and 5+ Examples
5. https://getbootstrap.com/docs/5.3/ Bootstrap Documentation
6. https://color.adobe.com/My-Library-color-theme-15948806/#:~:text=This%20color%20theme%20consists%20of,Medium%20Roast%20and%20Metal%20Fringe. Library Color Theme
7. https://www.youtube.com/playlist?list=PLSQ0_m4bjdvzDbKt-W9NRNXNdGPIA6oN1 Building a web application with Python and Django
8. https://docs.djangoproject.com/en/4.2/topics/settings/ Django Documentation
9. https://masteringdjango.com/source/ Mastering Django
10. https://www.youtube.com/watch?v=h1fKWxs7A2c&pp=ygUgalF1ZXJ5IEFqYXggZGphbmdvICBtb3N0IHdhdGNoZWQ%3D Django+Ajax Tutorials



