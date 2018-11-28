#include<iostream>
#include<fstream>
#include<string.h>
using namespace std;
int main()
{
	int T;
//#	std::fstream IP("input123a.txt", std::ios_base::in);
	std::fstream IP("A-large.in", std::ios_base::in);
	IP>>T;
	std::fstream OP("OPlarge.txt", std::ios_base::out);
	int i,j,K,count,n;
	char S[1005];
	for(i=0;i<T;i++)
	{
		IP>>S;
		IP>>K;
		cout<<T<<"\n";
		cout<<i+1<<" :"<<K<<" "<<S<<"\n";
		count=0;
		n=strlen(S);
		OP<<"Case #";
		OP<<i+1;
		OP<<": ";
		while(1)
		{
			for(j=n-1;j>=0;j--)
				if(S[j]=='-')
					break;
			n=j+1;
			if(j<0)
				break;
			if(n<K)
			{
				OP<<"IMPOSSIBLE";
				break;
			}
			S[n]='\0';
			for(j=n-1;j>=n-K;j--)
			{
				if(S[j]=='+')
					S[j]='-';
				else if(S[j]=='-')
					S[j]='+';
			}
			count++;
			cout<<"check "<<S<<"\n";
		}
		if(n==0)
			OP<<count;
		OP<<"\n";
	}
	return 0;
}
