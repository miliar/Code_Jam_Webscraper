#include<iostream>
#include<fstream>
#include<string.h>
using namespace std;
int main()
{
	int T;
//#	std::fstream IP("input.txt", std::ios_base::in);
	std::fstream IP("B-large.in", std::ios_base::in);
	IP>>T;
	std::fstream OP("OPlarge.txt", std::ios_base::out);
	int i,j,k,n;
	char N[25];
	for(i=0;i<T;i++)
	{
		IP>>N;
		n=strlen(N);
		OP<<"Case #";
		OP<<i+1;
		OP<<": ";
		for(j=1;j<n;j++)
			if(N[j]<N[j-1])
				break;
		while(j!=n)
		{
			j=j-1;
			N[j]=N[j]-1;
			if(j==0)
				break;
			if(N[j]>=N[j-1])
				break;
		}
		for(k=0;k<j;k++)
			OP<<N[k];
		if((N[j]!='0')&&(j<n))
			OP<<N[j];
		for(k=j+1;k<n;k++)
			OP<<"9";
		OP<<"\n";
	}
	return 0;
}
