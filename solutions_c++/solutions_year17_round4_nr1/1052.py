#include<bits/stdc++.h>
#define REP(x,y,z) for(int x=y;x<=z;x++)
#define FORD(x,y,z) for(int x=y;x>=z;x--)
#define MSET(x,y) memset(x,y,sizeof(x))
#define FOR(x,y) for(__typeof(y.begin()) x=y.begin();x!=y.end();x++)
#define F first
#define S second
#define MP make_pair
#define PB push_back
#define SZ size()
#define M 
void RI(){}
template<typename... T>
void RI( int& head, T&... tail ) {
    scanf("%d",&head);
    RI(tail...);
}
using namespace std;
typedef long long LL;
int t,n,p,cnt[10];
int main()
{
	RI(t);
	REP(tt,1,t)
	{
		RI(n,p);
		MSET(cnt,0);
		REP(i,1,n)
		{
			int x;
			RI(x);
			cnt[x%p]++;
		}

		int ans=0;
		if(p==2)
		{
			ans = cnt[0] + (cnt[1]+1)/2;
		}
		if(p==3)
		{
			int x = min(cnt[1], cnt[2]);
			ans = cnt[0] + x;
			
			x = max(cnt[1]-x, cnt[2]-x);
			ans += (x+2)/3;
		}
		if(p==4)
		{
			int x = min(cnt[1], cnt[3]);
			int y = cnt[2]/2;
			int remain = max(cnt[1]-x, cnt[3]-x);
			
			ans = cnt[0] + x + y;
			if(y)
			{
				//2 at front
				//211 233
				int a1 = 1;
				int r2 = remain-2;
				if(r2>0) a1 += (r2+3)/4;

				//2 at back
				//1111 1111 2
				int a2 = remain/4;
				r2 = remain%4;
				if(r2==3) a2+=2;
				else  a2+=1;

				ans += max(a1,a2);
			}
			else
			{
				//1111 or 3333
				ans += (remain+3)/4;
			}
		}
		
		printf("Case #%d: %d\n",tt,ans);
	}
	return 0;
}

