#include<bits/stdc++.h>
using namespace std;
int istidy(char N[],int n)
{
	for(int i=0;i<n-1;i++)
	{
		if(N[i]>N[i+1])
		return 0;
	}
	return 1;
}
int main()
{
	int t;
	cin>>t;
	int qno=1;
	while(t--)
	{
		char N[20];
		cin>>N;
		int n=strlen(N);
		int ch;
		while(!(istidy(N,n)))
		{
		for(int i=0;i<n-1;i++)
			{
				if(N[i]>N[i+1])
					{
						ch=i;
						if(N[i]=='1')
						N[i]='0';
						else if(N[i]=='2')
						N[i]='1';
						else if(N[i]=='3')
						N[i]='2';
						else if(N[i]=='4')
						N[i]='3';
						else if(N[i]=='5')
						N[i]='4';
						else if(N[i]=='6')
						N[i]='5';
						else if(N[i]=='7')
						N[i]='6';
						else if(N[i]=='8')
						N[i]='7';
						else if(N[i]=='9')
						N[i]='8';
						break;
					}
			}
			//cout<<ch<<endl;
			if(n!=1)
			for(int i=ch+1;i<n;i++)
			N[i]='9';
		}
		    if(n==1)
		    cout<<"case #"<<qno<<": "<<N<<endl;
			else if(N[0]=='0' && n!=1)
			{
				cout<<"case #"<<qno<<": ";
				for(int i=1;i<n;i++)
				cout<<N[i];
				cout<<endl;
			}
			else
		cout<<"case #"<<qno<<": "<<N<<endl;
		qno++;
	}
}
