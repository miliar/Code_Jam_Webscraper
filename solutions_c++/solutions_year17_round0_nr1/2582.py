#include<stdio.h>
#include<iostream>
#include<algorithm>
#include<vector>
#include<math.h>
#include<utility>
#include<queue>
#include<set>
#include<iomanip>
#include<functional>
#include<fstream>
#include<string.h>
#define fnt(t) for(int in=0;in<t;in++)
#define fn(n) for(int i=0;i<n;i++)
#define fnj(n) for(int j=0;j<n;j++)
#define foo(a,b,c) for(int i=a;i<b;i+=c)
#define fo(a,b) for(int i=a;i<b;i++)
#define get(x) scanf("%d",&x)
#define getll(x) scanf("%lld",&x)
#define lli long long int
#define cin fin
#define cout fout
using namespace std;
char  flip(char x)
{
	if(x=='+')
	return '-';
	else
	return '+';
}
int main()
{
	ifstream fin;
	ofstream fout;
	fin.open("C:\\Users\\Sh\\Desktop\\A-large.in", ios::in);
	fout.open("C:\\Users\\Sh\\Desktop\\output.txt", ios::out);
	int t;
	cin>>t;
	
	fnt(t)
	{
		cout<<"Case #"<<in+1<<": ";
		char s[1005];
		int k;
		cin>>s>>k;
		int l=strlen(s);
		int sum=0;
		fn(l-k+1)
		{
			if(s[i]=='-')
			{
				fnj(k)
				s[i+j]=flip(s[i+j]);
				sum+=1;
			}
		}
		int d=1;
		fn(l)
		{
			if(s[i]=='-')
			d=0;
		}
		if(d)
		cout<<sum<<"\n";
		else
		cout<<"IMPOSSIBLE\n";
	}
}
