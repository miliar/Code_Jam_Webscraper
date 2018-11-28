#include<bits/stdc++.h>
using namespace std;
const bool DBG = 1;

#define TRACE(x)    x
#define WATCH(x)    TRACE(cout << #x" = " << x << endl)
#define WATCHR(a,b) TRACE(for(auto it=a; it!=b;) cout<<*(it++)<<" ";cout<<endl)
#define WATCHC(V)   TRACE({cout << #V" = "; WATCHR(V.begin(), V.end());})
#define all(x) (x).begin(), (x).end()

typedef long long ll;
typedef pair<int,int> pii;
typedef vector<bool> vb;
typedef vector<int> vi;
typedef vector<vi> vii;
typedef vector<ll> vll;
typedef vector<vll> vvll;
typedef vector<pair<int,int>> vpii;

int bs(int nride, vector<vector<int>> tickets) {
	int prom = 0;
	int space = 0;
	int N = tickets.size();
	for(int pos = N-1; pos >= 0; pos--) {
		int over = max(0, (int)(tickets[pos].size() - nride));
		int under = max(0, (int)(nride - tickets[pos].size()));
		prom  += over;
		space += over;
		space -= under;
		if(space < 0) space = 0;
	}
	//cout << nride << ": " << prom << " " << space << endl;
	if(space > 0) return -1;
	else return prom;
}

int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);
	cout << fixed << setprecision(15);

	int T, N, C, M, p, b;
	cin >> T;
	for(int t = 1; t <= T; t++) {
		cout << "Case #" << t << ": ";
		cin >> N >> C >> M;
		vector<vector<int>> tickets(N);
		vector<int> cust(C);
		for(int i = 0; i < M; i++) {
			cin >> p >> b;
			tickets[p-1].push_back(b);
			cust[b-1]++;
		}
		for(int i = 0; i < N; i++) {
			sort(tickets[i].begin(), tickets[i].end());
		}
		int nrideh = M;
		int nridel = 1;
		for(auto i : cust) nridel = max(i, nridel);
		//cout << "NN: " << nridel << " " << nrideh << endl;
		while(nrideh - nridel > 1) {
			int nridem = nridel + (nrideh-nridel)/2;
			if(bs(nridem, tickets) != -1) nrideh = nridem;
			else nridel = nridem+1;
		}
		if(bs(nridel, tickets) != -1) nrideh = nridel;
		cout << nrideh << " " << bs(nrideh, tickets) << endl;
	}

	return 0;
}
