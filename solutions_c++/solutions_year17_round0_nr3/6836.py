#include <bits/stdc++.h>
using namespace std;

#define st first
#define nd second
#define mp make_pair
#define pb push_back
#define BUFF ios::sync_with_stdio(false);
#define db(x) cerr << #x << " == " << x << endl
#define dbs(x) cerr << x << endl		//dbs(a _ b);
#define _ << ", " <<
#define endl '\n'
#define cl(x, v) memset((x), (v), sizeof(x))

typedef long long ll;
typedef long double ld;
typedef pair<int, int> pii;
typedef pair<int, pii> piii;
typedef pair<ll, ll> pll;
typedef vector<int> vi;

const double PI = acos(-1), EPS = 1e-9;
const long long LINF = 0x3f3f3f3f3f3f3f3fLL;
const int INF = 0x3f3f3f3f, MOD = 1e9+7, N = 1e5+5;

int n, k, T;
priority_queue<pii>pq; //dist, -esq

main(){
	scanf("%d",&T);
	for(int t=1; t<=T; t++){
		while(!pq.empty())
			pq.pop();
		scanf("%d%d",&n,&k);
		pq.push(mp(n,0));
		for(int i=1; i<=k; i++){
			int dist = pq.top().st;
			int esq = -pq.top().nd;
			pq.pop();
			int d1 = dist/2 +dist%2 - 1;
			int d2 = dist - d1 -1;
			int esq2 = esq + dist/2 +dist%2;
			pq.push(mp(d1,-esq));
			pq.push(mp(d2,-esq2));
			if(i == k){
				printf("Case #%d: %d %d\n", t, max(d1,d2), min(d1,d2));
			}
		}
	}
}