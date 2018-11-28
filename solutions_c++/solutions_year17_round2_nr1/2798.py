#include <bits/stdc++.h>
using namespace std;

#define INF INT_MAX
#define LINF LLONG_MAX
#define MOD 1000000007
#define fi first
#define se second
#define mp make_pair
#define pb push_back
#define fl float
#define ll long long
#define ull unsigned long long
#define SZ(x) ((int)((x).size()))
#define clr(a,x) memset(a,x,sizeof(a))
#define IOS ios_base::sync_with_stdio(0)
#define F(ii,L,R) for (int ii = L; ii < R; ii++)
#define FE(ii,L,R) for (int ii = L; ii <= R; ii++)
#define FF(ii,L,R) for (int ii = L; ii > R; ii--)
#define FFE(ii,L,R) for (int ii = L; ii >= R; ii--)
#define FOREACH(i,t) for (__typeof__(t.begin()) i=t.begin(); i!=t.end(); i++)
#define ALL(c) (c).begin(),(c).end()
#define wez(n) int (n); scanf("%d",&(n))
#define wez2(n,m) int (n),(m); scanf("%d %d",&(n),&(m))
#define wez3(n,m,k) int (n),(m),(k); scanf("%d %d %d",&(n),&(m),&(k))
#define getI(a) scanf("%d", &a)
#define getII(a,b) scanf("%d%d", &a, &b)
#define getIII(a,b,c) scanf("%d%d%d", &a, &b, &c)
#define getS(x) cin >> x;
#define printA(a,L,R) FE(i,L,R) cout << a[i] << (i==R?'\n':' ')
#define printV(a) printA(a,0,a.size()-1)
#define FIN(x) freopen(x,"r",stdin)
#define FOUT(x) freopen(x,"w",stdout)
#define print(t) cout << t << ' ';

typedef vector<int> vi;
typedef vector<bool> vb;
typedef vector<vi> vvi;
typedef pair<int, int> pii;
typedef map<char, int> mci;
typedef map<int, int> mii;

void DEB() {cout << endl;}
template <typename T, typename...Ts>
void DEB(T first, Ts... rest) {
    print(first);
    DEB(rest...); 	
}

void solve(vector<pii> &a, int d, int n){
	vector<fl> time;
	F(i, 0, n)	time.pb(fl(d-a[i].fi)/fl(a[i].se));
	sort(ALL(time));
	/*F(i, 0, n)	cout << a[i].fi << ' ' << a[i].se;
	cout << endl;*/
	printf("%.6f\n", fl(d)/time[n-1]);
}

void work(){
	FIN("A-large.in");
	FOUT("A-large.out");
	wez(t);
	FE(q, 1, t){
		wez2(d, n);
		vector<pii> a;
		int x, y;
		F(i, 0, n){
			getII(x, y);
			a.pb(mp(x, y));
		}
		printf("Case #%d: ", q);
		solve(a, d, n);
	}
}

int main(){
	work();
	return 0;
}