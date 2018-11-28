#include <bits/stdc++.h>
#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <iomanip>
#include <vector>
#include <deque>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <algorithm>
#include <functional>
#include <utility>
#include <bitset>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstdio>
using namespace std;
#define ll long long int
#define mod 1000000007
#define rep(i,n) for(int i=0;i<n;i++)
#define ll long long int
#define f first
#define s second
#define pi pair<ll, ll>
#define pii pair<pi,int>
#define f first
#define s second
#define pb push_back
#define mp make_pair
#define pb push_back
using namespace std;
int main()
{
 freopen("/home/monu/Downloads/B-large.in","r",stdin);
 freopen("/home/monu/Desktop/out.txt","w",stdout);
ll t;
cin>>t;
for(ll k=1;k<=t;k++)
{
string str;
cin>>str;
ll l=str.length();
ll eq=0,curr=0;
for(ll i=0;i<l-1;i++)
{
	if(str[i]==str[i+1])
	{
	eq=i+1;
	curr=i+1;
	}
	else if(str[i] < str[i+1])
	{
	curr=i+1;
	}
	else
	{
		if(eq==curr and eq!=0)
		{
		for(ll j=i-1;j>=0;j--)
		{
			if(str[j]==str[j+1])
			i--;
			else
			break;
				
		}
			
			str[i]=char(int(str[i])-1);
			for(ll j=i+1;j<l;j++)
			str[j]='9';
			break;
		}
		else
		{
			str[i]=char(int(str[i])-1);
			for(ll j=i+1;j<l;j++)
			str[j]='9';
			break;
		}	
	
	}

}
cout<<"Case #"<<k<<": ";
if(str[0]=='0')
{
for(ll i=1;i<l;i++)
cout<<str[i];
cout<<endl;
}
else
cout<<str<<endl;
}
}
