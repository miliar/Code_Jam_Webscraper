#include <iostream>
#include <tuple>
#include <sstream>
#include <vector>
#include <cmath>
#include <ctime>
#include <cassert>
#include <cstdio>
#include <queue>
#include <set>
#include <map>
#include <fstream>
#include <cstdlib>
#include <string>
#include <cstring>
#include <algorithm>
#include <numeric>
using namespace std;

void solve( string s)
{
	int n=s.length();
	bool change=true;
	string res,carry;
	int i;
	bool same=false;
	if(n==1)
		cout<<s;
	else
	{
	for(i=0;i<(n-1);i++)
	{
		if((int)s[i]>(int)s[i+1])
			{
				change=false;
				if(same==false)
					cout<<res;
				else
				{	
					cout<<res;
					int si=carry.length();
					if(((int)carry[0]-49)!=0)
						cout<<(int)carry[0]-49;
					while(si--)
					cout<<'9';
					break;
				}

				if(s[i]!='1')
				cout<<((int)s[i])-49;
				break;
			}
		else if ((int)s[i]==(int)s[i+1])	
			{
				same=true;
				carry+=s[i];
			}
		else
			{
				if(same==true)
				{
					res=res+carry;
					carry="";
					same=false;
				}
				res=res+s[i];
			}
	}

	if(change == true)
		cout<<res+carry<<s[i];
	else
	{
		while(i<(n-1))
		{
			cout<<"9";
			i++;
		}
	}
	}
	
}

int main()
{
	int t;
	cin>>t;
	for( int i=1;i<=t;i++)
	{
		string s;
		cin>>s;
		printf("Case #%d: ",i);
		solve(s);
		cout<<endl;
	}
	return 0;
}