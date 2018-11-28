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

int main()
{
	ifstream fin;
	ofstream fout;
	fin.open("C:\\Users\\Sh\\Desktop\\B-large (1).in", ios::in);
	fout.open("C:\\Users\\Sh\\Desktop\\output.txt", ios::out);
	int t;
	cin>>t;
	
	fnt(t)
	{
		cout<<"Case #"<<in+1<<": ";
		char s[25];
		cin>>s;
		int l=strlen(s);
		//cout<<s<<"\n";
		if(l==1)
		{
			cout<<s<<"\n";
		}
		else
		{
			int ii=-1;
			fn(l-1)
		{
			if(s[l-1-i]<s[l-1-i-1])
			{
				s[l-1-i]=48+9;
				s[l-1-i-1]-=1;
				ii=l-i-1;
			}		
		}
		if(ii!=-1)
		{
			for(int i=ii;i<l;i++)
		       s[i]=48+9;
		}
		
		fn(l)
		{
			if(s[i]!='0')
			cout<<s[i];
		}
		cout<<"\n";
		}
		
	}
}
