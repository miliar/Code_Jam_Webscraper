#include<bits/stdc++.h>

using namespace std;

int main()
{
	int test;
	cin>>test;
	int t=test;
	while(test--)
	{
		char S[10000];
		int K;
		cin>>S;
		cin>>K;
		int count=0,flag=0,k=0;
		int length = strlen(S);
		int temp = length-1;
		int index=0;
//		cout<<S<<" string "<<K<<" length of pan "<<endl;
		while(k<length)
		{
			for(int i=k;i<length;i++)
			{
				if(S[i]=='-')
				{
					index=i;
					flag=1;
					break;
				}
				else
				{
					flag=0;
				}
			}
			if(flag==1)
			{
				if((length-index)>=K)
				{
					for(int i=index;i<K+index;i++)
					{
						if(S[i]=='+')
							S[i]='-';
						else
							S[i]='+';
					}
					count++;
				}
				else
				{
					flag=2;
					break;
				}
			}
			k++;
		}
		cout<<"Case #"<<t-test<<": ";
		if(flag==2)
			cout<<"IMPOSSIBLE\n";
		else if(flag==1)
			cout<<count<<'\n';
		else
			cout<<count<<'\n';
	}
	return 0;
}
