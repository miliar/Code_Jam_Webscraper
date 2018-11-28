#include<iostream>
#include<string.h>
using namespace std;
void find(char *S, int e,int tc)
{
	int i;
	for(i=1;i<=e && S[i-1]-'0' < S[i]-'0';i++);
	
	if(i>e) //S is tidy number
	{
		cout<<"Case #"<<tc<<": ";
		for(int p=0;p<=e;p++)
		{
			cout<<S[p];
		}
		cout<<endl;
	}
	else if(S[i-1] > S[i])
	{
		cout<<"Case #"<<tc<<": ";
		
		for(int p=0;p<i-1;p++)
		{
			cout<<S[p];
		}
		
		if(!(S[i-1]-'0'==1 && i-1==0))
		{
			cout<<(char)(S[i-1]-1);
			//cout<<"\n Hello : "<<(S[i-1]-'0')<<"  "<<i-1;
		}
		for(int p=i;p<=e;p++)
		{
			cout<<"9";
		}
		cout<<endl;
	}
	else if(S[i-1]==S[i])
	{
		int s=i-1,p;
		for(p=i+1;p<=e && S[p] >=S[p-1];p++);
		if(p>e)
		{
			cout<<"Case #"<<tc<<": ";
			for(int k=0;k<=e;k++)
			{
				cout<<S[k];
			}
			cout<<endl;
		}
		else if(S[p]<S[p-1])
		{
			cout<<"Case #"<<tc<<": ";
			for(int k=0;k<s;k++)
				cout<<S[k];
			if(!(S[s]-'0'==1 && s==0))
				cout<<(char)(S[s]-1);
			for(int k=s+1;k<=e;k++)
				cout<<"9";
			cout<<endl;
		}
	}
}
int main()
{
	int t,k,len,i=0;
	char S[20];
	//test cases 
	cin>>t;
	while(i++<t)
	{
		cin>>S;
		len=strlen(S);
		find(S,len-1,i);
	}
	return 0;
}
