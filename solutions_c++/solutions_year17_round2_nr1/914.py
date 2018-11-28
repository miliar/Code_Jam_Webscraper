#include <bits/stdc++.h>
using namespace std;

vector< pair<int,int> > horses;
int D;

double collision(double dp, int id){
    double dx = horses[id].first;
    double dspeed = dp - horses[id].second;
    if(dspeed <= 1E-10) return D + 1;
    double t = (dx / dspeed);
    return (dp * t);
}

bool ok(double sp, int N){
    double smallest = 1E20;

    for(int i = 0; i < N; i++){
	double pt = collision(sp, i);
	if(pt < (D-1E-10)) return 0;
    }

    return 1;
    }

double solve(){
    horses.clear();
    int N;
    cin >> D >> N;
    horses.resize(N);
    for(int i = 0; i < N; i++)
	cin >> horses[i].first >> horses[i].second;
    sort(horses.begin(), horses.end());

    double lo = 0, hi = 1E18;
    for(int i = 0; i <= 1000; i++){
	double mid = (lo + hi) / 2.0;
	if(ok(mid,N))
	    lo = mid;
	else
	    hi = mid;
    }

    return lo;
}

int main(){
    int t;
    cin >> t;
    for(int i = 1; i <= t; i++){
	printf("Case #%d: %.9f\n", i, solve());
    }
    return 0;
}
