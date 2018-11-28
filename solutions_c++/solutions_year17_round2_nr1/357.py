#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define ld double
#define vi vector<int>
#define pb push_back
#define mp make_pair
#define F first
#define S second
#define pii pair<int,int>
#define vll vector<ll >
#define rep(i, begin, end) for (__typeof(end) i = (begin) - ((begin) > (end)); i != (end) - ((begin) > (end)); i += 1)
#define all(a) (a).begin(), (a).end()
#define print(s) cerr<<#s<<" : ";for(auto i:(s))cerr<<i<<" ";cerr<<"\n";
#define sd(t) scanf("%d",&(t))
#define pd(t) printf("%d\n",(t))
#define endl "\n"
const int N = 1005;
int K[N], SP[N];
pair<int, double> P[N];
int main(){
	int t = 1, n, d;
	sd(t);
	for(int tt = 1; tt <= t; tt++){
		sd(d); sd(n);
		int ans = 0;
		rep(i, 1, n + 1) sd(K[i]), sd(SP[i]), P[i] = {K[i], SP[i]};
		sort(P + 1, P + n + 1);
		P[0] = {0, 1e18};
		for(int i = n - 1; i >= 0; i--){
			double speed_next = P[i + 1].S;
			int pos_next = P[i + 1].F;
			int pos = P[i].F;
			if(P[i].S <= speed_next) continue;
			else{
				P[i].S = min(P[i].S, speed_next + (pos_next - pos) * speed_next / (d - pos_next));
			}
		}
		printf("Case #%d: %.10lf\n", tt, P[0].S);
	}
}