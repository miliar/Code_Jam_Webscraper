#include<iostream>
#include<vector>
#include<string>
#include<set>
#include<algorithm>
#include<sstream>
#include<cstdlib>
#include<cstdio>

using namespace std;

int isTidy(string &num)
{
	char last = '0';
	for(int i=0; i<num.size(); i++)
	{
		if(num[i] < last)
		{
			return 0;
		}
		last = num[i];
	}
	return 1;
}

int main()
{
	int count;
	cin >> count;
	for(int i=1; i<=count; i++)
	{
		string number;
		cin >> number;
		while(!isTidy(number))
		{
			long long at = number.size() - 1;
			long long strength = 1;
			while(at >= 0)
			{
				if(number[at] == '9')
				{
					at--;
					strength *= 10;
					continue;
				}
				long long val;
				stringstream in(number);
				in >> val;
//				cout << val << endl;;
				val -= (strength * (number[at] - '0' + 1));
//				cout << "Changed: " << val << endl;
				stringstream out;
				out << val;
//				cout << "Old: " << number << endl;
				out >> number;
//				cout << "New: " << number << endl;
				break;
			}

//			while((number.size() > 1) && (number[0] == '0'))
//			{
//				number.erase(number.begin());
//			}
		}

		cout << "Case #" << i << ": ";
		cout << number;
		cout << endl;
	}

	return 0;
}
