#include <iostream>
#include <string>
#include <math.h>
using namespace std;

int main()
{


	int t;
	cin >> t;
	for (int i = 0; i< t; i++)
	{


		string s;int k;
		cin >>s;
		cin >>k;

		int n = 0;

		int index = 0;
		int flag = 0;
		while (index != s.length())
		{

			if (s[index] == '+')
				index ++;
			else
			{
				if (index+k-1 > s.length()-1)
				{
					flag = 1;
					cout <<"Case #"<<i+1<<": "<<"IMPOSSIBLE"<<endl;
					break;
				}
				for (int j = 0; j< k;j ++)
				{
					if (s[index+j] == '-')
						s[index+j] = '+';
					else s[index+j] = '-';
				}
				n++;
			}

		}
		if (flag == 0)
			cout<<"Case #"<<i+1<<": " << n<<endl;
	}

	return 0 ;
}