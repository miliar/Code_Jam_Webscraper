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

LL T,n,k,tmp,tmpl,tmpr,i,res,cnt;
map<LL,LL> m;

int main()
{
//	freopen("input.in","r",stdin);
//	freopen("output.out","w",stdout);
	std::ios::sync_with_stdio(false);
	cin>>T;
	for(int ti=1;ti<=T;ti++)
	{
		cin>>n>>k;
		m.clear();
		m[n]=1;
		tmp=k;
		tmpl=n;
		tmpr=n;
		cnt=0;
		while(tmp>1)
		{
			cnt++;
			tmp>>=1;
			for(i=tmpl;i<=tmpr;i++)
			{
				m[i>>1]+=m[i];
				m[(i-1)>>1]+=m[i];
			}
			tmpl=(tmpl-1)>>1;
			tmpr=(tmpr>>1);
		}
		k=k-(1<<cnt);
		res=0;
		for(i=tmpr;i>=tmpl;i--)
		{
			res+=m[i];
			if(res>k)
			{
				printf("Case #%d: %lld %lld\n",ti,i>>1,(i-1)>>1);
				break;
			}
		}
	}
	return 0;
}

