#include <bits/stdc++.h>
using namespace std;

int t, k, wynik;
string a;

bool sameplusy(string x)
{
	bool ans=1;
	for(int i=0;i<x.size();i++)
	{
		if(x[i]=='-') ans=0;
	}
	return ans;
}

int main()
{
	scanf("%d",&t);
	for(int l=1;l<=t;l++)
	{
		cin >> a;
		scanf("%d",&k);
		wynik=0;
		for(int i=0;i<a.size()-k+1;i++)
		{
			if(a[i]=='-')
			{
				for(int j=i;j<i+k;j++)
				{
					if(a[j]=='-') a[j]='+';
					else a[j]='-';
				}
				wynik++;
			}
		}
		cout << "Case #" << l << ": ";
		if(sameplusy(a)) cout << wynik << endl;
		else cout << "IMPOSSIBLE" << endl;
	}
}
