#include <algorithm>
#include <cstring>
#include <cmath>
#include <set>
#include <cstdio>
#include <iostream>
#define S(x) scanf("%lld",&x)
#define P(x) printf("%lld",x)
#define LI long long int
using namespace std;




int main() {
	LI t;
	cin>>t;
	for(int k=1;k<=t;k++)
	{
		string s;
		LI size,len,flag=0,count=0;
		cin>>s>>size;
		len=s.length();
		for(int i=0;i<len;i++)
		{
			if(s.at(i)=='-')
			{
				count++;
				for(int j=i;j<i+size;j++)
				{
					if(j>=len)
					{
						flag=1;
						break;
					}
					if(s.at(j)=='-') s.at(j)='+';
					else s.at(j)='-';// fliped 
				}
			}
			if(flag==1) break;
		}
		if(flag==0) cout<<"Case #"<<k<<": "<<count<<endl;
		else cout<<"Case #"<<k<<": IMPOSSIBLE"<<endl;
	}
	return 0;
}
