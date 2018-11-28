#include <bits/stdc++.h>
using namespace std;

bool isValid(unsigned long long int n)
{
	string s=to_string(n);
	for(int i=1;i<s.length();i++)
	{
		if(s[i]<s[i-1])
			return false;
	}
	return true;
}

int main()
{
	freopen("in.in","r",stdin);
	freopen("out.out","w",stdout);
	int t;
	cin >> t;
	for(int i=1;i<=t;i++)
	{
		unsigned long long int n;
		cin >> n;
		while(!isValid(n))
		{
			n--;
		}
		cout << "Case #" << i << ": " << n << endl;
	}
	return 0;
}
