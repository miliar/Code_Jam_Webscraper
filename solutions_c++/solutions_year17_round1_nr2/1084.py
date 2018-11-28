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
const int N = 55;
int Q[N][N], R[N];
pii Range[N][N];
const int MAXK = 1.11e6;
pair<int, int> valid[MAXK];
set<pair<int, int> > sets;
int main(){
	int t = 1, n, p;
	sd(t);
	while(t--){
		sd(n); sd(p);
		for(int i = 0; i < n; i++) sd(R[i]);
		for(int i = 0; i < n; i++){
			for(int j = 0;  j < p; j++){
				sd(Q[i][j]);
				// k >= Q[i][j]/(1.1 * R[i])
				// k <= Q[i][j] / (0.9 * R[i])
				Range[i][j].F = 1 + (Q[i][j] * 10 - 1) / (11 * R[i]);
				Range[i][j].S = (10 * Q[i][j]) / (9 * R[i]);
				for(int k = Range[i][j].F; k <= Range[i][j].S; k++) valid[k].push_back({i, j});
			}
		}
	}
	for(int k = 1; k <= MAXK; k++){
		for(int i = 0; i < n; i++)
			for(int j = 0; j < )
	}
}