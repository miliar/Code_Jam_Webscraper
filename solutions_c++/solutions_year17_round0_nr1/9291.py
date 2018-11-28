#include <bits/stdc++.h>
using namespace std;

#define f0(i,n) for(int i=0;i<n;i++)
typedef signed long long int sll;
typedef long long int ll;
 
int main()
{
	ofstream out("file1.out");
	freopen("A-large.in", "r", stdin);
	int t; cin >> t;
	sll p;;
	for (int i = 0; i < t; i++)
	{
		string s; int lim,len,count=0,k;
		cin >> s;
		cin>>lim;
		p=s.find('-');
		if(p!=-1)
		{
			len = s.length();
			for(int j=len-1;j>=0;j--)
			{
						
				if(s[j]=='-')
				{
					for(k = 1;k<=lim;k++,j--)
						if(j>=0)
						s[j] = s[j]=='-' ? '+' : '-';
						else break;
				j+=lim;
				count++;	
				}
			}
			
		p=s.find('-');
		if(p==-1 && k==lim+1)
			out<<"Case #"<<i+1<<": "<<count<<"\n";
			else
				out<<"Case #"<<i+1<<": IMPOSSIBLE\n";
		}
		else
			out<<"Case #"<<i+1<<": 0\n";
	}
}
