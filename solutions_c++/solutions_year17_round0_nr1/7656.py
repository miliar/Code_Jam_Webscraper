#include<bits/stdc++.h>
#define max(x, y) x>y?x:y
#define min(x, y) x<y?x:y
typedef long long int lli;
using namespace std;

void cakeflip(int param)
{
	string s;
	int k;
	cin >> s >> k;
	int counter=0, flag=0, i, j;
	for(i=0; i<s.size()-k; i++)
	{
		if(s[i] == '-')
		{
			flag++;
			for(j=i; j<i+k; j++)
			{
				s[j] = s[j] == '-' ? '+' : '-';
			}
		}
	}
	if(s[s.size()-k] == '-')
	{
		flag++;
		for(j=s.size()-k; j<s.size(); j++)
		{
			s[j] = s[j] == '-' ? '+' : '-';
		}
	}
	for(i=0; i<s.size(); i++)
		if(s[i] == '+')
			counter++;
	cout << "Case #" << param << ": ";
	if(counter == s.size())
	{
		cout << flag;
	}
	else
	{
		cout << "IMPOSSIBLE";
	}
	cout << endl;
}

int main()
{
	int o=1;
	if(o)
	{
		freopen("input.txt", "r", stdin);
		freopen("output.txt", "w", stdout);
	}
	int t;
	cin >> t;
	for(int i=1; i<=t; i++)
		cakeflip(i);
		return 0;
}
