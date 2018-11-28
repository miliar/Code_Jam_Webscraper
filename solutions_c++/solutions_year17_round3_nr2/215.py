#include<bits/stdc++.h>

#define s(a) scanf("%d",&a)
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

const int T = 1440;
bool cav[T+5];
bool jav[T+5];
int dp[T+5][T+5][2];
inline int update(int currVal, int val){
	if(currVal==-1)
		return val;
	if(currVal>=0 && val==-1)
		return currVal;
	return min(currVal, val);
}
// Start with Jamie
int s1(){
	if(!jav[0])
		return -1;
	dp[0][0][1] = 0;
	for(int tt=1;tt<=T;tt++)
	for(int jh=0;jh<=tt;jh++){
		// Go to jamie
		if(jav[tt%T]){
			// Earlier with Jamie
			if(jh-1>=0)
				dp[tt][jh][1] = update(dp[tt][jh][1], dp[tt-1][jh-1][1]);
			// Earlier not with Jamie
			if(dp[tt-1][jh][0]!=-1)
				dp[tt][jh][1] = update(dp[tt][jh][1], dp[tt-1][jh][0]+1);
		}
		// Go to cameron
		if(cav[tt%T]){
			// Earlier with Jamie
			if(jh-1>=0 && dp[tt-1][jh-1][1]!=-1)
				dp[tt][jh][0] = update(dp[tt][jh][0], dp[tt-1][jh-1][1]+1);
			// Earlier not with Jamie
			dp[tt][jh][0] = update(dp[tt][jh][0], dp[tt-1][jh][0]);
		}
	}
	return dp[T][T/2][1];
}
// Start with Cameron
int s2(){
	if(!cav[0])
		return -1;
	dp[0][0][0] = 0;
	for(int tt=1;tt<=T;tt++)
	for(int jh=0;jh<=tt;jh++){
		// Go to jamie
		if(jav[tt%T]){
			// Earlier with Jamie
			if(jh-1>=0)
				dp[tt][jh][1] = update(dp[tt][jh][1], dp[tt-1][jh-1][1]);
			// Earlier not with Jamie
			if(dp[tt-1][jh][0]!=-1)
				dp[tt][jh][1] = update(dp[tt][jh][1], dp[tt-1][jh][0]+1);
		}
		// Go to cameron
		if(cav[tt%T]){
			// Earlier with Jamie
			if(jh-1>=0 && dp[tt-1][jh-1][1]!=-1)
				dp[tt][jh][0] = update(dp[tt][jh][0], dp[tt-1][jh-1][1]+1);
			// Earlier not with Jamie
			dp[tt][jh][0] = update(dp[tt][jh][0], dp[tt-1][jh][0]);
		}
	}
	return dp[T][T/2][0];
}
void clearDP(){
	REP(i,T+1)REP(j,T+1)REP(k,2)dp[i][j][k] = -1;
}
int solve(){
	int ac, aj, start, end;
	s(ac);s(aj);
	REP(i,T+1)
		cav[i] = jav[i] = true;
	REP(i,ac){
		s(start);s(end);
		for(int j=start;j<end;j++)
			cav[j] = false;
	}
	REP(i,aj){
		s(start);s(end);
		for(int j=start;j<end;j++)
			jav[j] = false;
	}
	int ans = -1;
	clearDP();
	ans = update(ans, s1());
	clearDP();
	ans = update(ans, s2());
	return ans;
}

int main()
{
	int t;
	s(t);
	REP(tt,t){
		printf("Case #%d: ",tt+1);
		printf("%d\n",solve());
	}
    return 0;
}
