
# cherriesForPC
 API for [pcrumbly.github.io](https://pcrumbly.github.io) give cherries

# TODO/Things to try
*Use a Configuration File: Instead of hardcoding values like cherries.json, consider using a configuration file where you can store such settings. This makes it easier to manage and change these settings in the future without modifying the code.
*Error Handling: Implement proper error handling to provide meaningful responses when something goes wrong. For instance, handle cases where the JSON data is missing or invalid in the POST request.
*Logging: Add logging to your application to help you diagnose issues and monitor its behavior. You can use Python's built-in logging module to achieve this.
*Data Validation: Ensure that the data you receive from the client is valid before using it. For example, in the POST request, you should validate that the increment value is a number.
*Use HTTP Status Codes: Return appropriate HTTP status codes with your responses. For example, return a 400 Bad Request status when the client provides invalid data, and 201 Created after a successful POST.
*Persistent Storage: Consider using a proper database system instead of JSON files for storing data. Databases are designed for efficient data storage and retrieval, making your application more scalable and reliable.
*Separation of Concerns: As your application grows, it's a good practice to separate different components into separate files or modules. This makes your codebase more organized and easier to manage.
*Caching: Depending on the use case, you might consider using caching mechanisms to reduce the load on your server and improve response times for frequently accessed data.
