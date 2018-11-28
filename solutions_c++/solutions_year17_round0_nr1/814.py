#include <iostream>
#include <cstring>

using namespace std;

string s;
int n,k,f[1010],ntest;

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	cin >> ntest;
	for (int __=1;__<=ntest;__++)
	{
		cin >> s >> k;
		n=s.length();
		int cur_st=0,res=0;
		for (int i=0;i<1010;i++)
			f[i]=0;
		for (int i=1;i<=n;i++)
		{
			cur_st+=f[i];
			int plus=1;
			if (s[i-1]=='-') plus=0;
			if (cur_st%2) plus^=1;
			if (i+k-1>n)
			{
				if (plus) s[i-1]='+';
				else s[i-1]='-';
				continue;
			}
			if (!plus)
			{
				s[i-1]='+';
				res++;
				cur_st++;
				f[i+k]--;
			} else s[i-1]='+';
		}
		for (int i=0;i<n;i++)
			if (s[i]=='-') res=-1;
		cout << "Case #" << __ << ": ";
		if (res>=0) cout << res;
		else cout << "IMPOSSIBLE";
		cout << "\n";
	}	
}