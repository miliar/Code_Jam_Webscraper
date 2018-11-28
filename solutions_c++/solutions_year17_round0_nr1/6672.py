#include<bits/stdc++.h>
using namespace std;


int main()
{
//	freopen("large.in","r",stdin);
//	freopen("largeout.txt","w",stdout);
	int t;
	cin>>t;
	for(int l=1;l<=t;l++)
	{
		int k;
		string s;
		cin>>s>>k;
		int len=s.length(),f=0,i,j,np=0;
		for(i=0;i<len;i++)
		{
			if(s[i]=='-')
			{
				if((len-i)<k)
				{
					np=1;
					break;
				}
				else
				{
					f++;
					for(j=i;j<i+k;j++)
					{
						if(s[j]=='+')
						s[j]='-';
						else
						s[j]='+';
					}
				}
			}
		}
		cout<<"Case #"<<l<<": ";
		if(np==1)
		{
			cout<<"IMPOSSIBLE"<<endl;
		}
		else
		{
			cout<<f<<endl;
		}
	}
}
