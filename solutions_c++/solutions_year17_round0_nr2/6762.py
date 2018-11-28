#include<stdio.h>
#include<iostream>
#include<stdlib.h>
#include<algorithm>
#include<vector>
#include<list>
#include<math.h>
#include<utility>
#include<queue>
#include<set>
#include<functional>
#include<fstream>
#include<string.h>
#define fori(n) for(int i=0;i<n;i++)
#define forj(n) for(int j=0;j<n;j++)
#define foo(a,b,c) for(int i=a;i<b;i+=c)
#define fo(a,b) for(int i=a;i<b;i++)
#define get(x) scanf("%d",&x)
#define getll(x) scanf("%lld",&x)
#define ll long long 
#define cin fin
#define cout fout
using namespace std;

int main()
{
	ifstream fin;
	ofstream fout;
	fin.open("inputbl.in", ios::in);
	fout.open("outputbl.txt", ios::out);
	int tst;
	cin>>tst;
	
	for(int t=1;t<=tst;t++)
	{
	
	    char str[20];
	    cin>>str;
	    
	    int l=strlen(str);
	    
		
		
//		cout<<n<<" ";
	    int ind=l-1;
	    for(int i=l-1;i>0;i--)
	    {
	    	if((str[i-1]-'0')>(str[i]-'0'))
	    	{
	    		str[i-1]-=1;
	    	    ind=i-1;
			}
		}
//		cout<<"ind: "<<ind<<endl;
		ll res=0;
		
		for(int i=ind+1;i<l;i++)
		str[i]='9';
		
		for(int i=0;i<l;i++)
		res=res*10+(str[i]-'0');
		
		
	
		cout<<"Case #"<<t<<": "<<res<<endl;
	}
	
	
	return 0;
}
