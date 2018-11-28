#include<bits/stdc++.h>
using namespace std;
int main()
{
	int t;
	cin>>t;
	int qno=1;
	while(t--)
	{
		char S[1001];
		int k;
		cin>>S>>k;
		int n=strlen(S);
		int cnt=0;
		for(int i=0;i<n-k+1;i++)
		{
			if(S[i]=='-')
			{
				cnt++;
				for(int j=i;j<i+k;j++)
				{
					if(S[j]=='+')
					S[j]='-';
					else
					S[j]='+';
			    }
			    //cout<<S<<endl;
			}
		}
		int flag2=0;
		for(int i=0;i<n;i++)
		{
			if(S[i]=='-')
			flag2=1;
		}
		if(flag2)
		cout<<"case #"<<qno<<": "<<"IMPOSSIBLE"<<endl;
		else
		cout<<"case #"<<qno<<": "<<cnt<<endl;
	//	cout<<"f_s "<<S<<endl;
		qno++;
	}
	return 0;
}
