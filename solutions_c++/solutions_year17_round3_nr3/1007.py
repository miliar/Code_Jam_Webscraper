#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

#define REP(a, b, c) for(int a=(b); a<(c); a++)
#define dREP(a, b, c) for(int a=(b); a>=(c); a--)

int T, N, K;
double U;
vector<double> P;

bool check(double a){
	double rem = 0.0;
	REP(i, 0, N)
		if((a-P[i])>1e-7) rem += a-P[i];
	if((rem-U)>1e-9) return false;
	return true;
}

double b_search(){
	double lo = 0.0, hi = 1.0, md;
	if(check(hi)) return hi;
	REP(_i, 0, 100){
		if((hi-lo)<1e-8) return lo;
		md = lo+(hi-lo)/2;
		if(check(md)) lo = md;
		else hi = md;
	}
	return lo;
}

int main(){
	cin >> T;
	for(int t=1; t<=T; t++){
		cin >> N >> K;
		P.clear();
		P.resize(N);
		cin >> U;
		REP(i, 0, N) cin >> P[i];
		double ans = b_search();
		double fin_ans = 1.0;
		REP(i, 0, N){
			if((ans-P[i])>1e-7) fin_ans *= ans;
			else fin_ans *= P[i];
		}
		printf("Case #%d: %.9f\n", t, fin_ans);
	}
	return 0;
}
