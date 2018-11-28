#include <bits/stdc++.h>
using namespace std;

#define rep(i, f, t) for (int i = f; i < int(t); ++i)
#define all(x) x.begin(), x.end()
#define sz(x) (int)(x).size()
#define trav(x,a) for (auto& x : a)
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;

void solve(){
	int N, C, M;
	cin >> N >> C >> M;
	vector<vector<int> > tickets(C, vector<int>());
	vector<int> num(N);
	rep(i,0,M){
		int P, B;
		cin >> P >> B;
		--B;
		--P;
		tickets[B].push_back(P);
		++num[P];
	}
	int runs = 0;
	rep(i,0,C){
		runs = max(runs, (int)tickets[i].size());
	}
	int tot = 0;
	rep(i,0,N){
		tot += num[i];
		runs = max(runs, (tot+i)/(i+1));
	}
	int promotions = 0;
	rep(i,0,N){
		if(num[i] > runs)
			promotions += num[i]-runs;
	}
	cout << runs << " " << promotions << endl;
}

int main(){
	int N;
	cin >> N;
	rep(t,1,N+1){
		cout << "Case #" << t << ": ";
		solve();
	}
}
