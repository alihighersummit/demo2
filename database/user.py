import mysql as mysql
import database_properties
import mysql.connector


class User:

    @staticmethod
    def get_user():
        try:
            connection = mysql.connector.connect(host=database_properties.database_server_ip,
                                                 database=database_properties.database_name,
                                                 user=database_properties.database_server_username,
                                                 password=database_properties.database_server_password)

            cursor = connection.cursor(dictionary=True)
            sql = "Select * from user "
            cursor.execute(sql)

            # data is committed to the database
            result = cursor.fetchall()

            return result
        except mysql.connector.Error as error:
            print('error',error)

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

        return -1