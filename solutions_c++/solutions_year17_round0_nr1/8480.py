#include <bits/stdc++.h>
using namespace std;
const int oo = 0x3f3f3f3f;
const long long ooo = 0x3f3f3f3f3f3f3f3fll;
template<class T> T abs(T x) { return x > 0 ? x : -x;}
template<class T>  inline T sqr(T x) {return x*x; }
template<class T>  T lcm(T a, T b){return b*a/__gcd(a, b);}
#define fi first
#define se second
#define mk make_pair
#define pb push_back
#define rep(i, a, n) for(int i=a; i <n; ++i)
#define per(i, a, n) for(int i=n-1; i>=a; --i)
#define sz(x) ((int) (x).size())
#define all(x) (x).begin(), (x).end()
#define uniq(c) (c).resize(unique(all(c)) - (c).begin())
typedef long long ll;
typedef pair<int, int> ii;
typedef vector<vector<ll> >matrix;
map<string, int>mp;
const int MAX = 1010;
set<int>st;
char s[MAX];
vector<int>adj[MAX];
int dist[MAX];
int k, id;
void process(string ss){
	if(st.count(mp[ss]))return;
	st.insert(mp[ss]);
	int v = mp[ss];
	for(int i = 0; i+k-1 < sz(ss); ++i){
		string s2 = ss;
		for(int j = i; j < i+k; ++j){
			s2[j] = (s2[j] == '+') ? '-' : '+';
		}
		if(!mp.count(s2))mp[s2] = id++;
		adj[v].push_back(mp[s2]);
		adj[mp[s2]].push_back(v);
		process(s2);
	}
}
void solve(int tc){
	printf("Case #%d: ", tc);
	scanf(" %s %d", s, &k);
	string s1 = string(s);
	string s2 = string(sz(s1), '+');
	if(s1 == s2){
		puts("0");
		return;
	}
	st.clear();
	mp.clear();
	mp[s1] = 0;
	mp[s2] = 1;
	id = 2;
	process(s1);
	for(int i = 0; i < id; ++i)dist[i] = oo;
	dist[0] = 0;
	priority_queue<pair<int, int> >pq;
	pq.push({0, 0});
	while(!pq.empty()){
		int f = pq.top().se;
		pq.pop();
		for(auto v : adj[f]){
			if(dist[v] > dist[f]+1){
				dist[v] = dist[f] + 1;
				pq.push({-dist[v], v});
			}
		}
	}
	if(dist[1] == oo)puts("IMPOSSIBLE");
	else printf("%d\n", dist[1]);
	for(int i = 0; i < id; ++i)adj[i].clear();
}

int main() {
	int tc;
	scanf("%d", &tc);
	for(int i = 1; i <= tc; ++i)solve(i);
    return 0;
}
