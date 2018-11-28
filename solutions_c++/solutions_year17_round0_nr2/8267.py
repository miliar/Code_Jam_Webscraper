#include <iostream>
#include <cstring>
#include <string>
using namespace std;

int main() {
	// your code goes here
	int t;
	cin >> t;
	for(int i = 1; i <= t; i++)
	{
		string number;
		cin >> number;
		string::iterator sil;
		if( number.length() == 1 )
		{
			cout << "Case #" << i << ": " << number;
			cout << endl;
			continue;
		}
		int flag = 0;
		bool flag1 = false;
		for( sil = number.begin(); sil != number.end(); sil++ )
		{
			string::iterator ril = sil + 1;
			
			if( ril != number.end() && *sil == *ril )
			{
				while( *sil == *ril && ril != number.end() )
				{
					ril++;
				}
			}
			
			if( ril == number.end() )
				break;
			
			if( *sil > *ril )
			{
				*sil = (*sil) - 1;
				flag1 = *sil == '0';
				sil++;
				flag = 1;
				break;
			}
		}
		
		if( flag1 )
		{
			sil = number.begin();
			while( sil != number.end() )
			{
				*sil = '9';
				sil++;
			}
			
			number.erase(number.begin());
		}
		else if( flag )
		{
			while( sil != number.end() )
			{
				//cout << *sil << " ";
				*sil = '9';
				sil++;
			}
		}
		
		cout << "Case #" << i << ": " << number;
		cout << endl;
	}
}