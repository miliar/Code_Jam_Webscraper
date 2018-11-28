#include<bits/stdc++.h>

#define s(a) scanf("%d",&a)
#define slf(a) scanf("%lf",&a)
#define ss(a) scanf("%s",a)

#define MP           make_pair
#define PB           push_back
#define REP(i, n)    for(int i = 0; i < n; i++)
#define INC(i, a, b) for(int i = a; i <= b; i++)
#define DEC(i, a, b) for(int i = a; i >= b; i--)
#define CLEAR(a)     memset(a, 0, sizeof a)

using namespace std;

typedef long long          LL;
typedef unsigned long long ULL;
typedef vector<int>        VI;
typedef pair<int, int>     II;
typedef vector<II>         VII;

double inp[55];
double solve(){
	int n,k;
	double U, mini=1.0;
	s(n);s(k);
	slf(U);
	REP(i,n){
		slf(inp[i]);
		mini = min(mini,inp[i]);
	}
	double f=mini, l=1.0, mid;
	while((l-f)>=1e-15){
		mid = (f+l)/2;
		double msum=0;
		for(int i=0;i<n;i++)
			msum += max(0.0,mid-inp[i]);
		if(msum>U)
			l=mid;
		else f = mid;
	}
	double ans = 1.0;
	REP(i,n){
		if(inp[i]>=f)
			ans = ans*inp[i];
		else
			ans = ans*f;
	}
	return ans;
}

int main()
{
	int t;
	s(t);
	REP(tt,t){
		printf("Case #%d: ",tt+1);
		printf("%.15lf\n",solve());
	}
    return 0;
}
