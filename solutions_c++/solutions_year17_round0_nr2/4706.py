#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
	string str,sortedStr;
	long T = 0;
	cin>>T;

	for(int t=1; t<=T; t++)
	{

		cin>>str;
		
		cout<<"Case #"<<t<<": ";
		sortedStr = str;
		//cout<<str<<"\n";
		sort(sortedStr.begin(),sortedStr.end());
		//cout<<sortedStr<<"\n";

		long strLen = sortedStr.length();
		//cout<<"SortedStr length = "<<strLen<<"\n";

		if ( sortedStr[0] == '0' && sortedStr[strLen-1] == '1')
		{
			for(int i=0; i < strLen -1 ; i++)
				cout<<"9";
			cout<<"\n";	
		}
		//else if ( sortedStr[0] <= sortedStr[strLen-1]  )
		//	cout<<str<<"\n";	
		else
		{
			strLen = str.length();
			long large = 0;
			long index = 0;
			bool flag = true;
			for(int i=1; flag && i<strLen; i++)
			{
				if( str[i] < str[i-1] )
				{
					index = i-1;
					flag = false;

				}
				
					
			}

			if(flag == false )
			{
				long start = 0;
				
				for( int i=0; i< index ; i++)
				{
					if( str[start] < str[index] )
						start++;
				}

				for(int i=0; i < start ; i++)
				{
					cout<<str[i];
				}
				
				if( str[start] != '1')	
					cout<<(str[start]-'0' - 1 );

				for( int i=start+1; i< strLen; i++)
					cout<<"9";
			}
			else
				cout<<str;

			cout<<"\n";


		}
	}// end of for loop



	return 0;
}
