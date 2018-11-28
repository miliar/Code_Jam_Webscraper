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
	for (int p = 1; p <=t; ++p)
	{
		string s;
		cin>>s;
		int len=s.size();
		// int flag=1;
		for (int i = 0; i < len-1; ++i)
		{
			if (s[i]>s[i+1])
			{
				// flag=0;
				char t=s[i];
				for (int j = i+1; j < len; ++j)
				{
					s[j]='9';
				}
				int d;
				for (d=i-1; d >= 0; --d)
				{
					if(s[d]==t)
					{
						s[d+1]='9';
						continue;
					}
					else{
						break;
					}
				}
				s[d+1]=s[d+1]-1;
				break;
			}
		}
		// cout<<s<<endl;
		cout<<"Case #"<<p<<": ";
		int i=0;
		while ((s[i]=='0')&&(i<len))
		{
			i++;
		}
		for (int j = i; j < len; ++j)
		{
			cout<<s[j];
		}
		cout<<endl;
	}
	return 0;
}