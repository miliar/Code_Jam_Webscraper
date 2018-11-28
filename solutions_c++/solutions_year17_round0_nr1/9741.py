#include <bits/stdc++.h>
#define gc getchar_unlocked

using namespace std;

void scanint(int &x)
{
    register int c = gc();
    x = 0;
    int neg = 0;
    for(;((c<48 || c>57) && c != '-');c = gc());
    if(c=='-') {neg=1;c=gc();}
    for(;c>47 && c<58;c = gc()) {x = (x<<1) + (x<<3) + c - 48;}
    if(neg) x=-x;
}

//use scanint(variable) for integer input instead of scanf
int main()
{
	int t;
	scanf("%d", &t);
	for(int p=1;p<=t;p++)
	{
		string s;
		cin>>s;
		int k;
		cin>>k;
		int n=s.size();
		int i=0,count=0;
		for (i = 0; i <= n-k; ++i)
		{
			if (s[i]=='-')
			{
				for (int j = 0; j < k; ++j)
				{
					if (s[i+j]=='-')
					{
						s[i+j]='+';
					}
					else
						s[i+j]='-';
				}
				count++;
			}
		}
		int flag=1;
		for (; i < n; ++i)
		{
			if (s[i]=='-')
			{
				flag=0;
				break;
			}
		}
		if (flag)
		{
			cout<<"Case #"<<p<<": "<<count<<endl;
		}
		else
			cout<<"Case #"<<p<<": "<<"IMPOSSIBLE"<<endl;
	}
	return 0;
}