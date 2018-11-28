#include <iostream>
#include <string>
#include <algorithm>
#include <cstdlib>
#include <cstdio>
#include <sstream>
using namespace std;

string solve(string s)
{
	bool flag = false;
	while(!flag)
	{
		flag = true;
		for(int i = 0; i < s.size() - 1; i++)
		{
			if(s[i] > s[i + 1])
			{
				flag = false;
				//restar 1 a s[i]
				string aux = "";
				aux += s[i];
				stringstream ss;
				ss << aux;
				int aux2;
				ss >> aux2;
				aux2 -= 1;
				ss.clear();
				ss << aux2;
				ss >> aux;
				s[i] = aux[0];

				for(int j = i + 1; j < s.size(); j++)
				{
					s[j] = '9';
				}
			}
		}
	}

	int i = 0;
	while(s[i] == '0')
		i++;

	s = s.substr(i, s.size());

	return s;
}

int main() 
{
	freopen ("B-large.in","r", stdin);
	freopen ("b.out","w",stdout);
	int tt, k, res;
	string s;
	cin >> tt;
	for(int t = 1; t <= tt; t++)
	{
		cin >> s;

		cout << "Case #" << t << ": ";
		cout << solve(s) <<  endl;
	}
	return 0;
}