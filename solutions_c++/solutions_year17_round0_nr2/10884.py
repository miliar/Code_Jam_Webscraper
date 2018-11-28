/*
 ID: mh-sher1
 PROG: gift1
 LANG: C++11
 */
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef vector<int> vi;
typedef vector<vi> vvi;
#define MP make_pair
#define all(v)			((v).begin()), ((v).end())
#define sz(v)			((int)((v).size()))
#define clr(v, d) memset(v, d, sizeof(v))
#define rep(i, v)       for(int i=0;i<sz(v);++i)
#define fa(a,n)   for(int i = 0; i < n; i++){cin>>a[i];}  //fill array /* Sherbini :P */
#define fa2(a,n,m)   for(int i = 0; i < n; i++){for(int j = 0; j < m; j++){cin>>c[i][j];}}
#define f(i,x,n) for(int i=x;i<n;i++)
#define FI(n) for(int i=0;i<n;++i)
#define FJ(n) for(int j=0;j<n;++j)
#define FK(n) for(int k=0;k<n;++k)
#define rd(n) ll n;scanf("%I64d",&n);
#define set(arr,n,x) for(int i = 0; i < n; i++){arr[i]=x;}
#define rd2(n,k) ll n, k;scanf("%I64d %I64d",&n,&k);
#define rd3(n,k,l) ll n, k,l;scanf("%I64d %I64d %I64d",&n,&k,&l);
#define pb(x) push_back(x)
#define min3(x,y,z) min(min(x,y),z)
int s, f = 0;/*
 void solve(string x) {
 for (int i = 1; i < x.size(); i++) {
 if (x[i] < x[i - 1]) {
 f = 1;
 break;
 }
 }
 if (f) {
 for (int i = x.size() - 1; i >= 0; i--) {
 if (x[i] < x[i - 1]) {
 f = 1;
 break;
 }
 }
 f = 0;
 }

 }*/
string x;
void mnus(int i) {
	for (; i >= 0; i--) {
		if (x[i] > '0') {
			x[i]--;
			break;
		} else
			x[i] = '9';
	}

}
void solve(int i) {
	f = 0;
	for (int i = 1; i < x.size(); i++) {
		if (x[i] < x[i - 1]) {
			x[i] = '9';
			if (!f)
				mnus(i - 1), f = 1;
			//cout << x << endl;
		}

	}

}
int main() {
	freopen("t.in", "r", stdin);
	freopen("tidy.out", "w", stdout);
	int n, c = 1;
	cin >> n;
	while (n--) {
		cin >> x;
		if (x[x.size() - 1] == '0')
			mnus(x.size() - 1);
		solve(x.size());
		solve(x.size());
		for (unsigned int i = 0; i < x.size(); i++) {
			if (x[i] == '0')
				x.erase(x.begin() + i);
			else
				break;
		}
		cout << "case #" << c++ << ": " << x << endl;
	}
	return 0;
}

/*
 vector<vector<int>> v(100007);
 int vis[100007];
 int n, s, t;
 int cont = 0;
 void dfs(int node) {

 vis[node] = 1;
 for (auto a : v[node]) {
 if (!vis[a]) {
 cont++;
 if (a == t) {
 vis[t] = 1;
 return;
 }
 dfs(a);

 }
 }
 }
 int main() {
 int x;
 cin >> n >> s >> t;
 FI(n)
 {
 cin >> x;
 v[i].pb(x-1);
 }
 dfs(s - 1);
 if (vis[t-1])
 cout << cont;
 else
 cout << "-1";
 return 0;
 }*/
/*int error;
 struct wtvr {

 string pos;
 int val;

 };
 ll ToASCII(string s) {
 int y = 0;
 for (int i = 0; i < s.length(); i++) {
 char x = s[i];
 y += int(x);
 }
 return y;
 }
 bool cmp(const wtvr &first, const wtvr &second) {

 return ToASCII(first.pos) < ToASCII(second.pos);
 }

 int main() {

 int x, y, f = 1, next = 0, z = 0;
 string in, s, ss;
 wtvr ww[256];
 while (cin >> in) {
 if (in[0] == '(' && in[1] == ')') {
 sort(ww, ww + z, cmp);
 FI(z)
 {
 if ((i + 1) != z)
 if (ToASCII(ww[i].pos) >= ToASCII(ww[i + 1].pos)) {

 }
 }
 FI(z)
 {
 cout << ww[i].val;
 if (i != z - 1)
 cout << ' ';
 }
 next = 0;
 z = 0;
 s = "";
 ss = "";
 continue;
 }

 FI(in.size())
 {

 if (in[i] == '(' || in[i] == ')' || in[i] == ' ')
 continue;
 if (in[i] == ',') {
 f = 0;
 continue;
 }
 f ? s += in[i] : ss += in[i];
 }

 f = 1;
 if (s != " ")
 x = stoi(s);
 ww[z].val = x;
 ww[z].pos = ss;
 s = "";
 ss = "";
 z++;
 }

 //cout << x << ss;

 return 0;
 }*/
int isprime[1000005];

void sieve(int n) {
	isprime[0] = isprime[1] = 1;
	for (int i = 2; i <= n; i++) {
		if (!isprime[i]) {
			for (int j = 2 * i; j <= n; j += i) {
				isprime[j] = 1;
			}
		}
	}
}
/*vector<ll> facts(ll n) {
 vector<ll> v;
 ll i;
 for (i = 2; i * i <= n; i++) {
 while (n % i == 0)
 v.pb(i), v.pb(n/i);

 }
 if (i * i == n)
 v.pb(i);

 return v;
 }
 int main() {
 //ll x, y;

 *while (cin >> x >> y) {
 if (x > y)
 cout << 'no' << endl;
 for (ll i = y; i > 1; i--) {
 if (y % x)
 ;

 }




 }

 vector<ll> v = facts(9);
 for (auto a : v)
 cout << a << endl;
 return 0;
 }
 */

/*
 set<int> v;
 int main() {
 freopen("output.txt", "w", stdout);
 sieve(32000);
 int x, y;
 while (cin >> x >> y) {
 if (x == y && y == 0)
 break;
 int n = 0, nn = 0, f = 0;
 for (int i = x; i <= y; i++) {

 if (!isprime[i]) {
 if (!n) {
 n = i;

 } else if (!nn) {
 nn = i;

 } else {
 if (abs(i - nn) == abs(nn - n)) {
 v.insert(n);
 v.insert(nn);
 v.insert(i);
 n = i;
 nn = 0;
 f = 1;
 } else {
 if (!v.empty()) {

 for (auto m : v) {
 cout << m;
 }

 cout << endl;
 v.clear();
 }

 n = nn;
 nn = i;

 }
 }

 }
 }
 if (!v.empty()) {
 for (auto m : v) {
 cout << m << ' ';
 }

 cout << endl;
 v.clear();
 }
 }
 return 0;
 }*/

