#include <bits/stdc++.h>
using namespace std;
int main()
{
	int t,q=1;
	cin>>t;
	while(t--)
	{
		char n[20],k=0,loc1=0;
		int i,m,loc=0;
		cin>>n;
		m=strlen(n);
		if(m==1)
		{cout<<"Case #"<<q++<<": ";
			cout<<n<<endl;
		}
		else
		{
			for(i=0;i<m-1;i++)
			{
			    if(n[i+1]<n[i] && n[i]!='1' && (n[i]-n[i-1])==0)
				{
				    n[0]-=1;
				    for(i=1;i<m;i++)
				    n[i]='9';
				}
				else if(n[i+1]<n[i] && n[i]!='1' && abs(n[i+1]-n[i])>0)
				{
					loc=i+1;
					n[i]-=1;
					for(i=loc;i<m;i++)
						n[i]='9';
				}
				
				else if(n[i+1]<n[i] && n[i]=='1')
				{
					k=1;
					for(i=0;i<m;i++)
						n[i]='9';
				}
			}
			if(k==0)
			{
			    cout<<"Case #"<<q++<<": ";
				for(i=0;i<m;i++)
					cout<<n[i];
				cout<<endl;
			}
			else if(k==1)
			{
			    cout<<"Case #"<<q++<<": ";
				for(i=1;i<m;i++)
					cout<<n[i];
				cout<<endl;
			}
		}

	}
	return 0;
}
