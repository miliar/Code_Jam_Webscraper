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
int main()
{
	set<LL> s;
	map<LL,LL> cnt;
	int t;
	LL n,k,a1,a2;


	RI(t);
	REP(tt,1,t)
	{
		cnt.clear();
		s.clear();
		scanf("%lld %lld",&n,&k);

		cnt[n]=1;
		s.insert(n);
		while(k>0)
		{
			LL num = *s.rbegin();
			k -= cnt[num];
			s.erase(num);

			if(num%2==1)
			{
				a1 = num/2;
				a2 = num/2;
			}
			else
			{
				a1 = (num-1)/2;
				a2 = num/2;
			}
			cnt[a1] += cnt[num];
			cnt[a2] += cnt[num];
			if(a1) s.insert(a1);
			if(a2) s.insert(a2);
		}

		printf("Case #%d: %lld %lld\n",tt,a2,a1);
	}

	return 0;
}

