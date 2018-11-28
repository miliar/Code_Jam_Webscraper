#include <bits/stdc++.h>

using namespace std;

#define debug(x) cerr << "  - " << #x << ": " << x << endl;
#define debugs(x, y) cerr << "  - " << #x << ": " << x << "         " << #y << ": " << y << endl;

typedef long long ll;

#define fi first
#define se second
#define mp make_pair

vector <pair <int, int> > vv;
vector <pair <int, pair <int, int> > > vv2;
int n, k;


double formula(int idx, int last){
	double pi = acos(-1);
	int r = vv[idx].fi;
	int h = vv[idx].se;
	if(last == -1){
		return pi * (double) r * (double) r + 2.0 * pi * (double) r * h;
	}
	int r2 = vv[idx].fi;
	int h2 = vv[idx].se;
	return 2 * pi * (double) r2 * (double) h2; 
}

//double dp[1001][1001][1001];

double go(int idx, int last, int taken){
	cerr << fixed << setprecision(9);
	if(idx == n)
		return 0.0;
	if(taken == k)
		return 0.0;
	if(last == -1){
		return max(go(idx + 1, -1, taken), formula(idx, last) + go(idx + 1, idx, 1));
	}
	if(vv[idx].fi <= vv[last].fi){
		return max(go(idx + 1, last, taken), formula(idx, last) + go(idx + 1, idx, taken + 1));
	}
	else{
		return go(idx + 1, last, taken);
	}
}


int main(){
	int t;
	cin >> t;
	int tst = 0;
	cerr << fixed << setprecision(9);
	while(t--){
		cin >> n >> k;
		vv.clear();
		vv.resize(n);
		for(int i = 0; i < n; i++){
			cin >> vv[i].fi >> vv[i].se;
		}
		sort(vv.begin(), vv.end());
		reverse(vv.begin(), vv.end());	
		
		double res = go(0, -1, 0);
		cout << "Case #" << ++tst << ": " << fixed << setprecision(9) <<res << "\n";
	}
	return 0;
}