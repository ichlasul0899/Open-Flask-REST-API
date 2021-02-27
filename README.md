# Rest Full API with Flask
    Make API for my website 

----
**Post Message**
----
  Get data from user, and then validate, and then share to recipent email. 

* **URL**

  http://127.0.0.1:5000/api/v1/resources/mesages

* **Method:**
  
  `POST`

* **Request Headers**

   none
  
* **URL Params**

   none

* **Data Params**

  | key | value | required |
  | :---: | :---: | :---: |
  | email | STRING | true |
  | name | STRING | true |
  | message | STRING | true |



* **Success Response:**
  
  
  * **Code:** 201 CREATED <br />
    **Content:** 
    ```json
    { 
      "message": "Message created succesfully!", 
      "ok": true 
    }
    ```
 
<!-- * **Error Response:**

    * **Code:** 400 BAD REQUEST <br />
        **Content:** 
        ```json
        { "error" : ["Field Title Cannot Be Empty!"] }
        ```

        OR

        ```json
        { "error" : ["Field Description Cannot Be Empty"] }
        ```

        OR

        ```json
        { "error" : ["Must be in backlog, todo, doing, done."] }
        ```

        OR

        ```json
        { "error" : ["Field Title Null!"] }
        ```
        OR

        ```json
        { "error" : ["Field Category Null!"] }
        ```
        

    OR

    * **Code:** 404 UNAUTHORIZED <br />
        **Content:** 
        ```json
        { "error" : "You have Unauthorized token!" }
        ```

    OR

    * **Code:** 500 INTERNAL SERVER ERROR <br />
        **Content:** 
        ```json
        { "error" : "internal server error" }
        ``` -->
