from datetime import datetime

import feature_2

def main():
    start = datetime.now()
    feature_2.main()
    end = datetime.now()
    processing_time = (end-start).total_seconds() * 1000
    print(f"Start time: {start}.")
    print(f"End time: {end}.")
    print(f"Processing time: {processing_time} milliseconds.")

if __name__ == "__main__" : 
    main()