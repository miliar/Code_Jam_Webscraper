#include<iostream>
#include<algorithm>
#include<string>
using namespace std;

// 213

int main(){
	int t;
	cin >> t;
	for (int i = 0; i < t; i++)
	{
		string array;
		cin >> array;
		bool arr[19] = {false};
		int j = array.size()-1;
		for (;j >= 1; j--)
		{
			if (array[j] < array[j-1])
			{
				//cout << "hi "<<j << endl;
				int x = (int)(array[j-1]-'0');
				//cout << x-1 << endl;
				array[j-1] = (char)((x-1)+'0');
				//cout << array[j-1] <<endl;
				arr[j-1] = true;
			}
		}
		
		for (int j = 0; j < 19; j++)
		{
			if (arr[j])
			{
				for (int k = j+1; k < array.size(); k++)
					array[k] = '9';
				break;
			}
		}
		cout << "Case #" << i+1 << ": " ;
		 j = 0;
		for ( ; j < array.size();j++)
		{
			if (array[j] != '0')
				break;
		}
		cout << array.substr(j, array.size()+1-j) << endl;
	}
}
