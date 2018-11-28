#include<bits/stdc++.h>
using namespace std;
typedef long long int ll;
typedef pair<int,int> ipair;
#define MOD 1000000007
#define INF INT_MAX
int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	freopen("A-large.in","r",stdin);
	freopen("output.txt","w",stdout);
 	int t,tt;
	cin>>t;
	tt=t;
	while(t--)
	{
		string s;
		int k;
		cin>>s>>k;
		int flag=1,count=0,len=s.length();
		for(int i=0;i<len;)
		{
			if(s[i]=='-')
			{
				count++;
				int s1=0,last=i;
				for(int j=0;j<k && (i+j)<len;j++)
				{
					if(s[i+j]=='-')
					{
						s[i+j]='+';
					}
					else
					{
						if(s1==0)
						last=i+j,s1++;
						s[i+j]='-';
					}
					if(j==(k-1))
					flag=1;
					else
					flag=0;
				}
				i=last;
				if(flag==0)
				break;
			}
			else
			{
				i++;
			}
		}
		if(flag==1)
		{
			cout<<"Case #"<<(tt-t)<<":"<<" "<<count<<'\n';
		}
		else
		{
			cout<<"Case #"<<(tt-t)<<":"<<" "<<"IMPOSSIBLE"<<'\n';
		}
	}
	
	return 0;
}

