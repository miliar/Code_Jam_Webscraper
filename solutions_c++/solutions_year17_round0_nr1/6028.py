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

char input[1100];
int list[1100];
int n,cnt,tc;

int main()
{
	freopen("A-large.in","r",stdin); 
	freopen("a-outlarge.out","w",stdout); 
	scanf("%d",&tc);
	repp(t,1,tc)
	{
		scanf("%s",input);
		scanf("%d",&n);
		int str=strlen(input);
		repp(y,1,str)
		{
			if(input[y-1]=='+')
			list[y]=1;
			else
			list[y]=-1;
		}
		printf("Case #%d: ",t);
		cnt=0;
		repp(x,1,str-n+1)
		{
			//printf("%d (%d): ",x,list[x]);
			if(list[x]<0)
			{
				cnt++;
				repp(y,x,x+n-1)
				{
					list[y]*=-1;
				}
			}
			/*printf("%d ",cnt);
			repp(xx,1,str)
			{
				printf("%d",list[xx]);
			}
			printf("\n");*/
		}
		bool cek=1;
		repp(x,1,str)
		{
			if(list[x]==-1)
			{
				cek=0;
				break;
			}
		}
		if(cek)printf("%d\n",cnt);
		else
		printf("IMPOSSIBLE\n");
	}
	return 0;
}
