#include<iostream>
#include<iomanip>
#include<cstring>
using namespace std;
int main()
{
	freopen("A-large.in","rt",stdin);
  	freopen("A-large-out.txt","wt",stdout);
	long long t,i,j,k,n,l,cnt;
	cin>>t;
	for(i=0;i<t;i++)
	{
		char s[1001];
		cin>>s>>k;
		cout<<"Case #"<<i+1<<": ";
		cnt=0;
		n=strlen(s)-1;
		for(j=0;j<=n-k+1;j++)
		{
			if(s[j]=='-')
			{
				cnt++;
				for(l=0;l<k;l++)
				{
					if(s[j+l]=='+')
						s[j+l]='-';
					else
						s[j+l]='+';
				}
			}
		}
		int flg=1;
		for(;j<=n;j++)
		{
			if(s[j]!='+')
			{
				flg=0;
				break;
			}
		}
		if(flg)
			cout<<cnt<<endl;
		else
			cout<<"IMPOSSIBLE"<<endl;		
	}
	return 0;
}

