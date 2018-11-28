#include <bits/stdc++.h>
using namespace std;
#define DEBUG(x) cout << '>' << #x << ':' << x << endl;
#define FOR0(i,n) for(int i=0, _##i=(n); i<_##i; ++i)
#define FOR(i,l,r) for(int i=(l), _##i=(r); i<_##i; ++i)
#define FORD(i,l,r) for(int i=(r), _##i=(l); --i>=_##i; )
#define repi(i,a) for(__typeof((a).begin()) i=(a).begin(), _##i=(a).end(); i!=_##i; ++i)
#define dwni(i,a) for(__typeof((a).rbegin()) i=(a).rbegin(), _##i=(a).rend(); i!=_##i; ++i)
#define pb push_back
#define mp make_pair
#define INF (int)1e9
#define EPS 1e-9
#define SYNC std::ios::sync_with_stdio(false)
#define ff first
#define ss second
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef vector<int> vi;
typedef vector<vi> vvi;
char val[6] = {'R', 'O', 'Y', 'G', 'B', 'V'};
int main() {
	SYNC;
	int t, n, x;
	cin >> t;
	char output[1005];
	FOR(caseNum,1,t+1) {
		cin >> n;
		FOR0(i, n) output[i] = '\0';
		priority_queue<ii, vii, greater<ii>> pq;
		FOR0(i, 6) {
			cin >> x;
			if(x > 0) pq.push(mp(x, i));
		}
		int index = 1;
		int count = 0;
		while(!pq.empty() && count <= n) {
			if(index >= n) {index = 0; count++;}
			ii curr = pq.top(); pq.pop();
			if(output[index] != '\0' || (val[curr.ss] == output[(index+1)%n] || val[curr.ss] == output[(index+n-1)%n])) {
				index++; pq.push(curr); continue;
			}
			output[index] = val[curr.ss];
			if(curr.ff > 1) pq.push(mp(curr.ff-1, curr.ss));
			index += 2;
		}
		cout << "Case #" << caseNum << ": ";
		if(!pq.empty()) 
			cout << "IMPOSSIBLE" << endl;
		else {
			FOR0(i, n) cout << output[i];
			cout << endl;
		}
	}
}