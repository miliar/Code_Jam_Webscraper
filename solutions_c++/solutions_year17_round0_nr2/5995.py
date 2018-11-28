#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <algorithm>
#include <cstring>
#include <string.h>
#include <bitset>
#include <queue>
#include <map>
#include <string>
#include <stack>
#include <utility>
#include <queue>
#include <cmath>
#define mp make_pair
#define pb push_back
#define pii pair<int,int> 
#define ff first
#define ss second
#define ll long long 
#define ull unsigned long long
#define vi vector<int>
#define vii vector<pii>
#define vvi vector <vi>
#define rep(x,a,b,c) for(int x=a;x<=b;x+=c)
#define repp(x,a,b) rep(x,a,b,1)
#define rev(x,a,b,c) for(int x=a;x>=b;x-=c)
#define revv(x,a,b) rev(x,a,b,1)
#define OO (int)2e9
#define INF (ll)9e18

using namespace std;

int tc,str;
char input[100];
void reduce(int idx)
{
	if(idx==0)return;
	input[idx]='9';
	input[idx-1]--;
	if(input[idx-1]<='0')
	reduce(idx-1);
}

int main()
{
	freopen("B-large.in","r",stdin); 
	freopen("outlarge.out","w",stdout); 
	scanf("%d",&tc);
	repp(t,1,tc)
	{
		scanf("%s",input);
		printf("Case #%d: ",t);
		str=strlen(input);
		if(str==1)
		{
			printf("%s\n",input);
			continue;
		}
		bool done=0;
		while(!done)
		{
			repp(x,0,str-1)
			{
				if(x==str-1)
				done=1;
				else if(input[x]>input[x+1])
				{
					input[x]--;
					if(input[x]<='0')
					reduce(x);
					repp(y,x+1,str-1)
					input[y]='9';
					break;
				}
			}
		}
		bool cek=0;
		repp(x,0,str-1)
		{
			if(cek==0&&input[x]=='0')
			continue;
			else
			{
				cek=1;
				printf("%c",input[x]);
			}
		}
		printf("\n");
	}
	return 0;
}
