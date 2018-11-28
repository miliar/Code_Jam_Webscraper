#include<bits/stdc++.h>
using namespace std;
char S[20];

int main()
{
	freopen("testcase.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int T;
	long long int N;
	cin>>T;
	for(int t=1;t<=T;t++)
	{
		N=0;
		int flag=1;
		cin>>S;
		int L=strlen(S);
		while(flag==1)
		{
			flag=0;
			for(int i=0;i<L-1;i++)
			{
				if(S[i]>S[i+1])
				{
					flag=1;
					S[i]=S[i]-1;
					for(int j=i+1;j<L;j++)
					{
						S[j]='9';
					}
				}
			}
		}
		
		for(int i=0;i<L;i++)
		{
			N=N*10;
			N=N+(S[i]-48);
		}
		
		cout<<"Case #"<<t<<": "<<N<<endl;
	}
}
