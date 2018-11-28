#include <iostream>
#include <sstream>

using namespace std;

void fix(string &s, int pos)
{
	s[pos] = s[pos] - 1;
	for(int i = pos + 1; i < s.size(); i++)
		s[i] = '9';
}

int check(string &s)
{
	for(int j = 0; j < s.size()-1; j++)
	{
		if(s[j] > s[j+1])
		{
			return j;
		}
	}
	return -1;
}

int main()
{
	int t;
	long long n;
	cin >> t;
	for(int i=1; i <= t; i++)
	{
		cin >> n;
		ostringstream sout;
		sout<< n;
		string dig = sout.str();
		// cout<< dig << endl;
		int p;
		while((p = check(dig)) >= 0)
		{
			fix(dig, p);
		}
		cout<< "Case #" << i << ": ";
		int j = 0;
		while(dig[j] == '0')
		{
			j++;
		}
		for( ; j < dig.size(); j++)
		{
			cout<< dig[j];
		}
		cout<< endl;
	}
}