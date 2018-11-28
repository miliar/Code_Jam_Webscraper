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

int T,k;
char str[10000];

void solve(int x,int k)
{
	for(int i=x;i<x+k;i++)
	{
		if(str[i]=='-') str[i]='+';
		else str[i]='-';
	}
}

int main()
{
//		freopen("input.in","r",stdin);
//	freopen("output.out","w",stdout);
	std::ios::sync_with_stdio(false);
	cin>>T;
	for(int ti=1;ti<=T;ti++)
	{
		printf("Case #%d: ",ti);
		cin>>str>>k;
		int res=0;
		for(int i=0;i<strlen(str)-k+1;i++)
		{
			if(str[i]=='-')
			{
				solve(i,k);
				res++;
			}
		}
		bool flag=true;
		for(int i=strlen(str)-k+1;i<strlen(str);i++)
		{
			if(str[i]=='-')
			{
				flag=false;
				printf("IMPOSSIBLE\n");
				break;
			}
		}
		if(flag)
		{
			printf("%d\n",res);
		}
	}
}

