#include <bits/stdc++.h>

#define rep2(x,fr,to) for(int (x)=(fr);(x)<(to);(x)++)
#define rep(x,to) for(int (x)=0;(x)<(to);(x)++)
#define repr(x,fr,to) for(int (x)=(fr);(x)>=(to);(x)--)
#define all(c) (c).begin(),(c).end()
#define sz(v) (int)(v).size()

using namespace std;
typedef long long ll; typedef vector<int> VI; typedef pair<int,int> pii;
const ll mod = 1e9+7;


void fnc00(int qt){
	
	int D,N;
	cin >>D >>N;
	vector<int> K(N), S(N);
	rep(i,N) cin >>K[i] >>S[i];
	
	double mx=0;
	rep(i,N) mx = max(mx, 1.0*(D-K[i])/S[i]);
	
	//printf("mx=%d\n", mx);
	double ans = D / mx;
	
	printf("Case #%d: %.15f\n", qt+1, ans);

}

int main()
{
	//cin.tie(0); ios_base::sync_with_stdio(false);
	int t; cin >> t;
	rep(i, t) fnc00(i);
	
	
	return 0;
}