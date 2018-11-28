#include <iostream>
#include <algorithm>
#include <cmath>
#include <map>
#include <set>
#include <sstream>
#include <vector>
#include <queue>
#include <string>
#include <stdio.h>
#include <string.h>
#include <functional>    //for hash
#include <bitset>        //for binary
using namespace std;
int main(int argc, char *argv[])
{
	freopen("input.iN","r" , stdin);
	freopen("ans.txt","w" , stdout);
	int t,k;
	string s;
	cin>>t;
	for(int i=1;i<=t;i++)
	{
		cin>>s>>k;
		cout<<"Case #"<<i<<": ";
		int c=0;
		for(int y=s.length()-1;y>=k-1;y--)
		{
			if(s[y]=='-')
			{c++;
				for(int o=y;o>y-k;o--)
				{
					if(s[o]=='-')s[o]='+';
					else s[o]='-';
					//cout<<o<<" "<<s[o]<<endl;
				}
			}
		}
		int p;
		for( p=0;p<k;p++)
		{
			if(s[p]=='-'){cout<<"IMPOSSIBLE"<<endl;break;}
		}
		if(p==k)cout<<c<<endl;
	}
	
	return 0;
}
