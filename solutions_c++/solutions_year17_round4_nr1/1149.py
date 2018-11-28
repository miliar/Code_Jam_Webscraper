#define _CRT_SECURE_NO_WARNINGS
#define ll long long

#define MAX 100100
#define LOG2MAX 20
#define MAXs 1001

#define oo 1e9

#include <iostream>
#include <cstdio>
#include <iomanip>
#include <cmath>
#include <algorithm>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <stack>
#include <sstream>

using namespace std;

ll CeilArithmeticSeq(ll s) {
	return ll((-1 + sqrt(1 + 8 * s)) / 2);
}

ll gcd(ll a, ll b) { if (b == 0) return a; return gcd(b, a % b); }
ll lcm(ll a, ll b) { return a / gcd(a, b) * b; }
ll pow(ll a, ll b) { ll ans = 1; while (b--) ans *= a; return ans; }

#define printdec(d,i) cout << fixed << setprecision(i) << d;

// Fast power algorithm
inline ll power(ll base, ll exp, ll mod) {
	ll ans = 1;
	base %= mod;

	while (exp > 0) {
		if (exp & 1) ans = (ans * base) % mod;
		exp >>= 1;
		base = (base * base) % mod;
	}

	return ans;
}

// Check if the given number-n is prime of not
inline bool isPrime(ll n) {
	if (n < 2) return false;
	for (ll i = 2; i * i <= n; ++i) if (n % i == 0) return false;
	return true;
}

// Sieve of Eratosthenes' algorithm for generating prime numbers
inline void generatePrimes(int n) {
	vector<bool> p(n + 1, true);
	vector<pair<int,int>> factors[MAX];
	p[0] = p[1] = false;
	factors[1].push_back({ 1,1 });

	for (int i = 2; i * i <= n; ++i)
		if (p[i])
			for (int j = i * i; j <= n; j += i) {
				p[j] = false;
				int e = 0, d = j;
				while (d%i == 0)d /= i, ++e;
				factors[j].push_back({ i,e });
			}
		else factors[i].push_back({ i,1 });

	vector<int> primes;

	for (int i = 2; i <= n; ++i)
		if (p[i])
			primes.push_back(i);
}

// Returns the shortest path between the source and destination nodes for the given unweighted graph
inline int bfs(int src, int dst, vector<int> *edges[MAX]) {
	vector<int> sp(MAX, -1);
	queue<int> q;
	q.push(src);
	sp[src] = 0;

	while (!q.empty()) {
		int u = q.front();
		q.pop();

		if (u == dst) return sp[u];

		for (int v : *edges[u]) {
			if (sp[v] == -1) {
				sp[v] = sp[u] + 1;
				q.push(v);
			}
		}
	}

	return sp[dst];
}

// Structure holds the last node in the path from the source along with the total weight
struct edge {
	int id;
	int weight;

	edge(int i, int w) : id(i), weight(w) {}

	bool operator<(const edge& rhs) const {
		return weight > rhs.weight;
	}
};

// Returns the shortest path between the source and destination nodes for the given weighted graph
inline int dijkstra(int src, int dst, vector<edge>* edges[MAX]) {
	int u, v, w;
	vector<int> sp(MAX + 1, -1);
	priority_queue<edge> q;
	q.push(edge(src, 0));

	while (!q.empty()) {
		u = q.top().id;
		w = q.top().weight;
		q.pop();

		if (sp[u] != -1) continue;

		sp[u] = w;

		for (auto p : *edges[u]) {
			v = p.id;

			if (sp[v] == -1) {
				q.push(edge(v, w + p.weight));
			}
		}
	}

	return sp[dst];
}

// Find the shortest path between any pair of nodes in the given graph
inline void floyd_warshall(int n, int adjMatrix[MAXs][MAXs]) {
	int i, j, k;

	for (k = 0; k < n; ++k)
		for (i = 0; i < n; ++i)
			for (j = 0; j < n; ++j)
				adjMatrix[i][j] = min(adjMatrix[i][j], adjMatrix[i][k] + adjMatrix[k][j]);

	bool negative_cycle = false;

	for (i = 0; i < n; ++i)
		for (j = 0; j < n; ++j)
			negative_cycle = negative_cycle || adjMatrix[i][j] != oo;
}


// Find the shortest path between the source and all other node with the detection of negative cycles
inline vector<int> bellman_ford(int src, int n, vector<pair<int, int>> *edges[MAX]) {
	int i, j, k, v, w;
	bool done = false;
	vector<int> sp(n, oo);
	sp[src] = 0;

	for (k = 0; k < n && !done; ++k) {
		done = true;

		for (i = 0; i < n; ++i) {
			for (auto p : *edges[i]) {
				v = p.first;
				w = p.second;

				if (sp[v] > sp[i] + w) {
					sp[v] = sp[i] + w;
					done = false;
				}
			}
		}
	}

	bool negative_cycle = (k == n && !done);

	return sp;
}

// Sort nodes in the given graph in topological order using Khan algorithm
inline void topological_sort_khan(int n, vector<int> *edges[MAX], vector<int>& nodes) {
	int i, u;
	queue<int> nxt;		// nodes of indegree zero
	vector<int> indegree(n, 0);

	for (i = 0; i < n; ++i) for (int v : *edges[i]) ++indegree[v];
	for (i = 0; i < n; ++i) if (indegree[i] == 0) nxt.push(i);

	while (!nxt.empty()) {
		u = nxt.front();
		nxt.pop();

		nodes.push_back(u);

		for (int v : *edges[u]) if (--indegree[v] == 0) nxt.push(v);
	}
}

// Build sparse table for computing min/max/gcd/lcm/etc. for every interval in the given array in O(n.log n)
inline void build_sparse_table(int n, int a[MAX], int st[MAX][LOG2MAX], int LOG[MAX]) {
	int x, y, i, j;

	for (i = 0, LOG[0] = -1; i < n; ++i) {
		st[i][0] = a[i];
		LOG[i + 1] = LOG[i] + !(i & (i + 1));
	}

	for (j = 1; (1 << j) <= n; ++j) {
		for (i = 0; (i + (1 << j)) <= n; ++i) {
			x = st[i][j - 1];
			y = st[i + (1 << (j - 1))][j - 1];
			st[i][j] = min(x, y);
		}
	}
}

// Get the min value from spase table in O(1)
inline int getMin_st(int l, int r, int st[MAX][LOG2MAX], int LOG[MAX]) {
	int s = r - l + 1;
	int g = LOG[s];

	int a = st[l][g];
	int b = st[r - (1 << g) + 1][g];

	return min(a, b);
}

// Returns the longest common suffix of string starting from i-th character and the whole string
inline vector<int> z_function(const string& str) {
	int n = (int)str.size();
	vector<int> z(n);

	for (int i = 1, l = 0, r = 0; i < n; ++i) {
		if (i <= r)
			z[i] = min(r - i + 1, z[i - l]);

		while (i + z[i] < n && str[z[i]] == str[i + z[i]])
			++z[i];

		if (i + z[i] - 1 > r)
			l = i, r = i + z[i] - 1;
	}

	return z;
}

class DisjointSetsUnion {
private:
	int setsCount;
	int *parent, *setsLen;

public:
	DisjointSetsUnion(int n) {
		setsCount = n;
		parent = new int[n];
		setsLen = new int[n];

		for (int i = 0; i < n; ++i) {
			parent[i] = i;
			setsLen[i] = 1;
		}
	}

	~DisjointSetsUnion() {
		delete[] parent;
		delete[] setsLen;
	}

	inline int getSetsCount() {
		return setsCount;
	}

	inline int getSetLength(int a) {
		return setsLen[getSetId(a)];
	}

	inline int getSetId(int a) {
		return a == parent[a] ? a : parent[a] = getSetId(parent[a]);
	}

	inline bool isSameSet(int u, int v) {
		return getSetId(u) == getSetId(v);
	}

	inline void unionSets(int u, int v) {
		if (!isSameSet(u, v)) {
			setsCount--;
			setsLen[getSetId(v)] += setsLen[getSetId(u)];
			parent[getSetId(u)] = getSetId(v);
		}
	}

	inline void moveElement(int u, int v) {
		if (!isSameSet(u, v)) {
			if (getSetLength(u) == 1) setsCount--;
			setsLen[getSetId(v)]++;
			setsLen[getSetId(u)]--;
			parent[u] = getSetId(v);
		}
	}
};

template<class T>
class monotonic_queue {
	struct node {
		T val, min, max;

		inline node(T v = 0) {
			val = min = max = v;
		}
	};

	stack<node> s1, s2;

	inline void flip() {
		while (!s1.empty()) {
			node n(s1.top().val);
			if (!s2.empty()) {
				n.min = std::min(n.min, s2.top().min);
				n.max = std::max(n.max, s2.top().max);
			}
			s1.pop();
			s2.push(n);
		}
	}

public:
	inline void push(int val) {
		node n(val);
		if (!s1.empty()) {
			n.min = std::min(n.min, s1.top().min);
			n.max = std::max(n.max, s1.top().max);
		}
		s1.push(n);
	}

	inline void pop() {
		if (s2.empty() == 1) flip();
		if (s2.empty() == 0) s2.pop();
	}

	inline T min() const {
		T mn = 2e9;
		if (!s1.empty()) mn = std::min(mn, s1.top().min);
		if (!s2.empty()) mn = std::min(mn, s2.top().min);
		return mn;
	}

	inline T max() const {
		T mx = -2e9;
		if (!s1.empty()) mx = std::max(mx, s1.top().max);
		if (!s2.empty()) mx = std::max(mx, s2.top().max);
		return mx;
	}

	inline int size() const {
		return s1.size() + s2.size();
	}
};

class binary_indexed_tree {
	int n;
	int bit[MAX];

	inline void update(int idx, int val) {
		while (idx <= n) {
			bit[idx] += val;
			idx += idx & -idx;
		}
	}

	inline int getSum(int idx) {
		int sum = 0;
		while (idx > 0) {
			sum += bit[idx];
			idx -= idx & -idx;
		}
		return sum;
	}
};

class segment_tree {
	static int n;
	int arr[100100];
	int seg[400400];
	int lzy[400400];

	int build(int id = 1, int l = 0, int r = n) {
		if (l == r - 1) return seg[id] = arr[l];

		int lChild = id * 2;
		int rChild = id * 2 + 1;
		int mid = (l + r) / 2;

		return seg[id] = build(lChild, l, mid) + build(rChild, mid, r);
	}

	inline void updateNode(int v, int id, int l, int r) {
		lzy[id] += v;
		seg[id] += (r - l) * v;
	}

	inline void shift(int id, int l, int r) {
		int lChild = id * 2;
		int rChild = id * 2 + 1;
		int mid = (l + r) / 2;

		updateNode(lzy[id], lChild, l, mid);
		updateNode(lzy[id], rChild, mid, r);

		lzy[id] = 0;
	}

	int update(int x, int y, int v, int id = 1, int l = 0, int r = n) {
		if (x >= r || y <= l) return seg[id];

		if (x <= l && y >= r) {
			updateNode(v, id, l, r);
			return seg[id];
		}

		shift(id, l, r);

		int lChild = id * 2;
		int rChild = id * 2 + 1;
		int mid = (l + r) / 2;

		return seg[id] = update(x, y, v, lChild, l, mid) + update(x, y, v, rChild, mid, r);
	}

	int getSum(int x, int y, int id = 1, int l = 0, int r = n) {
		if (x >= r || y <= l) return 0;
		if (x <= l && y >= r) return seg[id];

		shift(id, l, r);

		int lChild = id * 2;
		int rChild = id * 2 + 1;
		int mid = (l + r) / 2;

		return getSum(x, y, lChild, l, mid) + getSum(x, y, rChild, mid, r);
	}
};

class trie {
#define ALPHA_SIZE 200

	struct node {
		node* edges[ALPHA_SIZE] = {};
		int prefixCount = 0;
		bool wordEnd = false;
	};

	node* root;
	int nodesCount;
	int distinctWordsCount;

public:
	trie() {
		root = new node();
		nodesCount = 0;
		distinctWordsCount = 0;
	}

	~trie() {
		_clear(root);
	}

	inline void insert(const char* str) {
		node* n = root;

		for (int i = 0; str[i]; ++i) {
			if (n->edges[str[i]] == NULL) {
				n->edges[str[i]] = new node();
				++nodesCount;
			}

			++n->prefixCount;
			n = n->edges[str[i]];
		}

		++n->prefixCount;

		if (!n->wordEnd) {
			n->wordEnd = true;
			++distinctWordsCount;
		}
	}

	inline void remove(const char* str) {
		node* n = root;

		for (int i = 0; str[i]; ++i) {
			--n->prefixCount;
			n = n->edges[str[i]];
		}

		--n->prefixCount;
	}

	inline void clear() {
		_clear(root);
		root = new node();
		nodesCount = 0;
		distinctWordsCount = 0;
	}

	inline int getNodesCount() const {
		return nodesCount;
	}

	inline int getWordsCount() const {
		return distinctWordsCount;
	}

private:
	void _clear(node* n) {
		if (n == NULL) return;
		for (int i = 0; i < ALPHA_SIZE; ++i) _clear(n->edges[i]);
		delete n;
		n = NULL;
	}
};

void kmp(string s) {
	int pi[MAX];
	int n = s.length(), ret = 0;
	for (int i = 1, j = 0; i < n; ++i) {
		while (s[i] != s[j] && j) {
			j = pi[j];
		}
		if (s[i] == s[j])pi[i] = ++j;
		else pi[i] = 0;
	}
}

ll C(long double n, long double r) {
	r = min(r, n - r);
	long double x = 1;
	while (r)x *= n-- / r--;
	return x;
}

ll permutation(int n, int r)
{
	ll x = n;
	while (--n > r)x *= n;
	return x;
}














int n, p, g[5], x, s, k;




int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int testCases, testC = 0;
	cin >> testCases;

	while (testC++ < testCases) {
		cout << "Case #" << testC << ": ";

		cin >> n >> p;
		memset(g, 0, sizeof g);

		for (int i = 0; i < n; ++i) {
			cin >> x;
			g[x%p]++;
		}

		s = g[0];

		if (p == 2)s += (1+g[1]) / 2;

		if (p == 3) {
			k = min(g[1], g[2]);
			g[1] -= k;
			g[2] -= k;
			s += k + (g[1]+2) / 3 + (2+g[2]) / 3;
		}

		if (p == 4) {
			k = min(g[1], g[3]);
			g[1] -= k;
			g[3] -= k;
			s += k + g[2] / 2 + g[1] / 4 + g[3] / 4;
			if (g[2] & 1) {
				s++;
				if (g[1] % 4 == 3)s++;
				if (g[3] % 4 == 3)s++;
			}
			else {
				s += (g[1] % 4 != 0) + (g[3] % 4 != 0);
			}
		}

		cout << s << endl;
	}
}
