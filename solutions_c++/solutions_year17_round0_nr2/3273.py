#include <iostream>
#include <vector>
#include <map>
#include <cmath>

#include <sstream>

using namespace std;

bool is_tidy(int n)
{
	stringstream ss;
	ss << n;
	string s = ss.str();
	for(int i = 1; i < s.size(); i++)
	{
		if(s[i - 1] > s[i])
			return false;
	}
	return true;
}

string digits(int n)
{
	stringstream ss;
	ss << n;
	return ss.str();
}


int main()
{
	int c;
	cin >> c;
	for(int i = 1; i <= c; i++)
	{
		unsigned long long n;
		cin >> n;
		for(int p = 0; p < 18; p++)
		{
			unsigned long long d = n / pow((long double)10, p);
			if(d == 0) break;
			d %= 10;
			while((!is_tidy(n)) && d != 9)
			{
				n -= pow((long double)10, p);
				d = n / pow((long double) 10, p);
				d %= 10;
			}
		}
		cout << "Case #" << i << ": " << n << endl;
	}
	return 0;
}