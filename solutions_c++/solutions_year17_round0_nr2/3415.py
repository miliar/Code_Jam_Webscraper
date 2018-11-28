#include<iostream>
#include<algorithm>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<string>
#include<cmath>
#include<ctime>
#include<ctime>
#include<vector>
#include<queue>
#include<stack>
#include<map>
#include<utility>

#define LL long long
#define pb push_back
#define mp make_pair
#define ft first
#define sd second
#define PII pair<int,int>
#define PPI pair< pair<int,int>,int >
#define PIP pair< int,pair<int,int> >
#define PLL pair<LL,LL>
#define L(x) (x<<1)
#define R(x) ((x<<1)+1)
#define LeftPart l,(l+r)>>1
#define RightPart ((l+r)>>1)+1,r
#define lb(x) (x&(-x))

using namespace std;

string str;

int check()
{
	for(int i=0;i<str.length()-1;i++)
	{
		if(str[i]>str[i+1])
		{
			return i;
		}
	}
	return -1;
}

void solve()
{
	int tmp=check();
	str[tmp]=str[tmp]-1;
	for(int i=tmp+1;i<str.length();i++) str[i]='9';
}

int T,i;

int main()
{
//	freopen("input.in","r",stdin);
//	freopen("output.out","w",stdout);
	std::ios::sync_with_stdio(false);
	cin>>T;
	for(int ti=1;ti<=T;ti++)
	{
		cout<<"Case #"<<ti<<": ";
		cin>>str;
		while(check()!=-1)
		{
			solve();
		}
		for(i=0;str[i]=='0';i++);
		for( ;i<str.length();i++) cout<<str[i];
		cout<<endl;
	}
	return 0;
}

