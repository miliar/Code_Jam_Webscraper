#include <bits/stdc++.h>
using namespace std;
int main(){
//here the code begins
	int t,q=1;
	cin>>t;
	while(t--)
	{
		char n[20],flag=0,loc1=0;
		int i,m,loc=0;
		cin>>n;

		m=strlen(n);

		if(m==1)
		{
                       cout<<"Case #"<<q++<<": ";
			       cout<<n<<endl;
		}

		else
		{
//loop starts
			for(i=0;i<m-1;i++)
			{
			    if(n[i+1]<n[i] && n[i]!='1' && (n[i]-n[i-1])==0)
				{
				    n[0]-=1;
			for(int p=1;p<m;p++)
				    n[p]='9';
				}
				else if(n[i+1]<n[i] && n[i]!='1' && abs(n[i+1]-n[i])>0)
				{
				loc=i+1;
				n[i]-=1;
				for(i=loc;i<m;i++)
					n[i]='9';
			
}
				//some more conditions
				else if(n[i+1]<n[i] && n[i]=='1')
				{
					flag=1;
					for(int o=0;o<m;o++)
						n[o]='9';
				}
			}
//condition
			if(flag==0)
			{
			    cout<<"Case #"<<q++<<": ";
				for(int j=0;j<m;j++)
					cout<<n[j];
				cout<<endl;
			}
			else if(flag==1)
			{
			    cout<<"Case #"<<q++<<": ";
				for(int j=1;j<m;j++)
					cout<<n[j];
				cout<<endl;}
		}

	}
	return 0;
}
