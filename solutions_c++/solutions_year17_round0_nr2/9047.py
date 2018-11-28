#include<bits/stdc++.h>

using namespace std;

int main()
{
	int t;
	cin>>t;
	for(int k=1 ; k<=t ; k++ )
	{	
		char s[200];
		cin>>s;
		int len = strlen(s)-1;
		int no[200];
		for( int i=0 ; i<=len ; i++ )
			no[i] = s[len-i]-48;
		for( int i=0 ; i<len ; i++ )
		{
			if(no[i]<no[i+1])
			{
				for( int j=i ; j>=0 && no[j]!=9 ; j-- )
					no[j]=9;
				i++;
				no[i]--;
				if(no[i]==-1)
				{
					no[i]=9;
					for( int j=i+1 ; j<=len ; j++ )
					{
						no[j]--;
						if(no[j]==-1)
							no[j]=9;
						else
							break;
					}
				}
				i--;
			}
		}
		int f=0;
		cout<<"Case #"<<k<<": ";
		for( int i=len ; i>=0 ; i-- )
		{
			if(no[i]!=0)
				f=1;
			if(f==1)
				cout<<no[i];
		}
		if(f==0)
			cout<<"0";
		cout<<endl;
	}
	return 0;
}
