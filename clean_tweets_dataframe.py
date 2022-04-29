import pandas as pd
from textblob import TextBlob
class Clean_Tweets:
    """
    The PEP8 Standard AMAZING!!!
    """
    def __init__(self, df:pd.DataFrame):
        self.df = df
        print('Automation in Action...!!!')
        
    def drop_unwanted_column(self, df:pd.DataFrame)->pd.DataFrame:
        """
        remove rows that has column names. This error originated from
        the data collection stage.  
        """
        unwanted_rows = df[df['retweet_count'] == 'retweet_count' ].index
        df.drop(unwanted_rows , inplace=True)
        df = df[df['polarity'] != 'polarity']
        
        return df
    def drop_duplicate(self, df:pd.DataFrame)->pd.DataFrame:
        """
        drop duplicate rows
        """
        
        df = df.drop_duplicates()
        
        return df
    def convert_to_datetime(self, df:pd.DataFrame)->pd.DataFrame:
        """
        convert column to datetime
        """
        
        
        df['created_at'] = pd.to_datetime(df['created_at'])
        
        df['created_at'] = pd.to_datetime(df['created_at'])
        
        df.index = df['created_at']
        
        df = df['2020-12-31' :]
        
        df.drop('created_at', axis = 1, inplace = True)
        
        df = df.reset_index()
        
        
        
        return df
    
    def convert_to_numbers(self, df:pd.DataFrame)->pd.DataFrame:
        """
        convert columns like polarity, subjectivity, retweet_count
        favorite_count etc to numbers
        """
        df['polarity'] = df['polarity'].apply(pd.to_numeric)
        df['subjectivity'] = df['subjectivity'].apply(pd.to_numeric)
        df['retweet_count'] = df['retweet_count'].apply(pd.to_numeric)
        df['favorite_count'] = df['favorite_count'].apply(pd.to_numeric)
        
        return df
    
    def remove_non_english_tweets(self, df:pd.DataFrame)->pd.DataFrame:
        """
        remove non english tweets from lang
        """
        
        df = df[df['lang'] == 'en']
        
        return df