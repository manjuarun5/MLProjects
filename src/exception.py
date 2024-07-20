import sys
import logging
def error_message_details(error,error_details:sys):
    _,_,exc_tb = error_details.exc_info() 
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno 
    error_message = ("Error has occurred in file:{0} at line number {1} and error is as follows: {2}".format(file_name,line_number,str(error)))
    return error_message

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_details(error_message,error_detail)
    def __str__(self): 
        return self.error_message

if __name__=="__main__":
    try:
        a = 1/0
    except Exception as ex:
        logging.info("Divide by Zero")
        raise CustomException(ex, sys)