#include<bits/stdc++.h>
#define ll long long
#define ld long double
#define pi pair<int,int>
#define pll pair<ll,ll>
#define vl vector< ll >
#define bug(a) cout<<a<<endl;
#define bug2(a,b) cout<<a<<" "<<b<<endl;
#define bug3(a,b,c) cout<<a<<" "<<b<<" "<<c<<endl;
using namespace std;
int main()
{
	int test;
	scanf("%d",&test);
	ofstream out("out.txt");
	for(int t=1;t<=test;t++)
	{
		string s;
		int k;
		cin>>s>>k;
		int len=s.length();
		int res=0;
		for(int i=0;i<len;i++)
		{
			if(s[i]=='-')
			{
				int j=i;
				if((i+k)>len)
				{
					res=-1;
					break;
				}
				while(j<i+k)
				{
					s[j]=(s[j]=='-')?'+':'-';
					j++;
				}
				res++;
			}
		}
		if(res==-1)
			out<<"Case #"<<t<<": IMPOSSIBLE"<<endl;
		else
			out<<"Case #"<<t<<": "<<res<<endl;
	}
	return 0;
}


