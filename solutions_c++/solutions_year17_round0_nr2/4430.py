#include <bits/stdc++.h>
using namespace std;

int t;
string x;

bool ok(string x)
{
	bool ans = 1;
	for(int i=1;i<x.size();i++)
	{
		if(x[i]<x[i-1]) ans=0;
	}
	return ans;
}

string usunzerawiodace(string x)
{
	string ans;
	bool pocz=1;
	for(int i=0;i<x.size();i++)
	{
		if(x[i]!='0')
		{
			pocz=0;
			ans+=x[i];
		}
		if(x[i]=='0' && pocz==0) ans+=x[i];
	}
	return ans;
}

string rozwiazanie(string x)
{
	if(ok(x))
	{
		x = usunzerawiodace(x);
		return x;
	}
	else 
	{
		for(int i=1;i<x.size();i++)
		{
			if(x[i]<x[i-1])
			{
				x[i-1]--;
				for(int j=i;j<x.size();j++)
				{
					x[j]='9';
				}
				break;
			}
		}
		return rozwiazanie(x);
	}
}

int main()
{
	scanf("%d",&t);
	for(int i=1;i<=t;i++)
	{
		cin >> x;
		
		cout << "Case #" << i << ": " << rozwiazanie(x) << endl;
		
	}
}
