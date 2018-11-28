//Aleksander Łukasiewicz
#include<bits/stdc++.h>
using namespace std;

#define fru(j,n) for(int j=0; j<(n); ++j)
#define tr(it,v) for(typeof((v).begin()) it=(v).begin(); it!=(v).end(); ++it)
#define x first
#define y second
#define pb push_back
#define mp make_pair
#define ALL(G) (G).begin(),(G).end()

typedef long long LL;
typedef pair<int,int> PII;
typedef vector<int> VI;

const int INF = 1000000009;

pair<LL, LL> Solve(LL n, LL k){
	LL left = (n-1)/2;
	LL right = n/2;
	k--;
	if(k==0)
		return mp(right, left);
	if(k%2==1)
		return Solve(right, k/2+1);
	else
		return Solve(left, k/2);
}

int main(){
	int t;
	scanf("%d", &t);
	for(int pp=1; pp<=t; pp++){
		LL n, k;
		scanf("%lld %lld", &n, &k);
		pair<LL, LL> ans = Solve(n, k);
			
		printf("Case #%d: %lld %lld\n", pp, ans.x, ans.y);
	}
    
    
return 0;
}