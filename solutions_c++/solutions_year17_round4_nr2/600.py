#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef double ld;
typedef pair<int, int> pii;
#define mp make_pair
#define pb push_back

istream &operator >> (istream &cin, pii &t) {
	cin >> t.first >> t.second;
	return cin;
}

const int MAXN = 2000006;
const int MAXE = (int) (1e7) + 5;
const int inf = (int) (1e9 + 9);

int to[MAXE], cap[MAXE], nxt[MAXE], head[MAXN], E;
int head_temp[MAXN];
int dst[MAXN];
int Q[MAXN], Qh, Qt;
int S, T;

void addEdge (int a, int b, int c) {
	to[E] = b, cap[E] = c, nxt[E] = head[a], head[a] = E++;
	to[E] = a, cap[E] = 0, nxt[E] = head[b], head[b] = E++;
}

bool bfsDinic () {
	fill (dst, dst + MAXN, -1);
	dst[S] = 0;
	Qh = Qt = 0;
	Q[Qt++] = S;

	while (Qh < Qt) {
		int v = Q[Qh++];

		for (int id = head[v]; id != -1; id = nxt[id]) {
			int nv = to[id];
			if (-1 == dst[nv] && cap[id]) {
				dst[nv] = dst[v] + 1;
				Q[Qt++] = nv;
			}
		}
	}

	return dst[T] > 0;	
}

int dfsDinic (int v, int limit) {
	if (!limit)
		return 0;
	if (v == T)
		return limit;

	for (int &id = head_temp[v]; id != -1; id = nxt[id]) {
		int nv = to[id];
		if (dst[nv] != dst[v] + 1)
			continue;
		int ret = dfsDinic (nv, min (limit, cap[id]));
		
		if (ret) {
			cap[id] -= ret;
			cap[id ^ 1] += ret;
			return ret;
		}
	}
	return 0;
}

int Dinic (int limit = inf) {
	int flow = 0, add;

	while (bfsDinic () && limit > 0) {
		copy (head, head + MAXN, head_temp);

		while (add = dfsDinic (S, limit)) {
			flow += add;
			limit -= add;
		}
	}
	return flow;
}
      
int n, m, c;         
pii mas[1111];
vector<int> pos[3];
int A[1111], B[1111];

void load () {
	pos[1].clear ();
	pos[2].clear ();              
	memset (A, 0, sizeof (A));
	memset (B, 0, sizeof (B));                
	cin >> n >> c >> m;
	for (int i = 0; i < m; i++) {
		int a, b;
		cin >> a >> b;
		if (b == 1)
			A[a]++;
		else
			B[a]++;
		pos[b].pb (a);
	}
}

int bad[2222];

int check (int cnt) {         
	int B[1111];
	copy (::B, ::B + 1111, B);
	int A[1111];
	copy (::A, ::A + 1111, A);

	if (cnt < (int) pos[1].size ())
		return -1;

	if (cnt < (int) pos[2].size ())
		return -1;

    for (int i = 0; i < (int) pos[1].size (); i++) {
    	bad[i] = pos[1][i];
    }

   	for (int i = 0; i < cnt; i++) {
   		A[bad[i]]--;
   		bool in = false;
   		for (int j = 1; j <= n; j++) {
   			if (bad[i] == j) continue;
   			if (!B[j]) continue;
   			if (!A[j]) continue;
   			B[j]--;
   			bad[i] = -1;
   			in = true;
   			break;
   		}
   		if (in) continue;
   		for (int j = 1; j <= n; j++) {
   			if (bad[i] == j) continue;
   			if (!B[j]) continue;
   			B[j]--;
   			bad[i] = -1;
   			break;
   		}         
   	} 

   	if (!accumulate (B, B + 1111, 0))
   		return 0;

	int res = 0;

	for (int i = 0; i < cnt; i++) {
		if (-1 == bad[i]) continue;
		int lastfree = -1;
		for (int j = 1; j <= n; j++) {
			if (bad[i] == j) continue;
			lastfree = j;
			break;
		}
		for (int j = 1; j <= n; j++) {
			if (!B[j]) continue;
			if (j < lastfree) continue;
			B[j]--;
			res++;
			break;
		} 
	}
	if (accumulate (B, B + 1111, 0))
		return -1;
	return res;
}


void solve (int tc) {
	int ans1 = 0, ans2 = 0;
	
	int l = 1;
	int r = m;

	while (l <= r) {
		int m = l + r;
		m >>= 1;
		int a = check (m);
		if (a != -1) {
			ans1 = m;
			ans2 = a;
			r = m - 1;
		}
		else {
			l = m + 1;
		}             
	}

	pii ans (ans1, ans2);


	l = 1;
	r = m;

	for (int i = 0; i < m; i++) {
		swap (A[i], B[i]);
	}
	pos[1].swap (pos[2]);

	while (l <= r) {
		int m = l + r;
		m >>= 1;
		int a = check (m);
		if (a != -1) {
			ans1 = m;
			ans2 = a;
			r = m - 1;
		}
		else {
			l = m + 1;
		}             
	}

	ans = min (ans, mp (ans1, ans2));
	ans1 = ans.first;
	ans2 = ans.second;


	clog << tc << endl;

	cout << "Case #" << tc << ": " << ans1 << ' ' << ans2 << endl;
}
            

void clear () {
}

int main () {
#ifdef LOCAL
    freopen ("file.in", "r", stdin);
    freopen ("file.out", "w", stdout);
#endif 
	
	int T;
	cin >> T;

	for (int tc = 1; tc <= T; tc++) {
		load ();
		solve (tc);
		clear ();
	}

    return 0;
}