#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef long double ld;
typedef pair<double,double> dd;
typedef pair<ll,ll> pll;
typedef pair<string,int> psi;
typedef pair<int,int> ii;
typedef vector<int> vi;
typedef vector<ll> vll;
typedef vector<pll> vpll;
typedef vector<vector<int> > vvi;
typedef vector<vector<ll> > vvll;
typedef vector<vector<ii> > vvip;
typedef vector<ii> vii;
typedef map<int,int> mpi;
#define pb push_back
#define F first
#define S second
//#define MOD 1000000007
#define NA -1
#define ALL(v) v.begin(),v.end()
#define mp make_pair
#define rep(i, n) for (int (i) = 0; (i) < (n); (i) ++)
#define rep1(i, n) for (int (i) = 1; (i) <= (n); (i) ++)
#define FOR(i, a, b) for (int (i) = (a); (i) <= (b); (i)++)
#define db(x) {cout << #x << " = " << (x) << endl;}
#define dba(a, x, y) {cout<<#a<<" :";FOR(i123,x,y)cout<<setw(4)<<(a)[i123];cout<<endl;}
#define foreach(e, x) for (__typeof(x.begin()) e = x.begin(); e != x.end(); e++) 
#define clr(x) memset(x,0,sizeof(x));
#define sz(x) int((x).size())
#define endl '\n'
const int INF = INT_MAX;
const ll INFL = LLONG_MAX;
const ld pi = acos(-1);
#define sc(t) scanf("%d",&t)
// vector<string> split(const string &s, char delim) {
//     stringstream ss(s);
//     string item;
//     vector<string> tokens;
//     while (getline(ss, item, delim)) {
//         tokens.push_back(item);
//     }
//     return tokens;
// }

typedef pair<pll,ll> ppll;
int dx[] = {1, -1, 0, 0};
int dy[] = {0, 0, 1, -1};
#define re return
#define MAX 100
int a[100000+1];

int main()
{
	// #ifndef ONLINE_JUDGE
	// 	freopen("input.txt","r",stdin);
	//     freopen("output.txt","w",stdout);;
	// #endif
	// freopen("input.txt","r",stdin);
	// freopen("output.txt","w",stdout);
	//ios_base::sync_with_stdio(0); cout.tie(0); cin.tie(0);
	ios_base::sync_with_stdio(0); cout.precision(15); cout << fixed; cout.tie(0); cin.tie(0);
	int t;
	cin>>t;
	int  cas = 0;
	while(t--)
	{
		++cas;
		cout<<"Case #"<<cas<<": "; 
		int n,k;
		cin>>n>>k;
		int a[n+3];
		clr(a);
		for(int j = 1; j<= k; j++)
		{
			int Ls[n+3];clr(Ls);
			int Rs[n+3];clr(Rs);
			int leftmostocc = 1, rightmostocc = n+2;
			for(int p = 2; p<= n+1; p++)
			{
				if( a[p] == 1)
				{
					leftmostocc = p ;
				}
				else
				{
					Ls[p] = p- leftmostocc - 1; 
				}

			}
			for(int p = n+1 ; p>=2; p--)
			{
				if( a[p] == 1)
				{
					rightmostocc = p ;
				}
				else
				{
					Rs[p] = rightmostocc -p - 1; 
				}

			}
			vi v;
			// dba(Ls,2,n+1);
			// dba(Rs,2,n+1);
			for(int p = 2; p<= n+1;p++)
			{
				if( a[p] == 0)
				{
					v.pb( min(Ls[p],Rs[p] ));
				}
			}
			int mx = *max_element(ALL(v));
			v.clear();
			for(int p = 2; p<= n+1; p++)
			{
				if( a[p] == 0 && min(Ls[p],Rs[p] ) == mx)
				{
					v.pb( p);
				}

			}
			vi w;
			foreach(e,v)
			{
				w.pb( max(Ls[*e],Rs[*e]));
			}
			int al = *max_element(ALL(w));
			w.clear();
			foreach(e,v)
			{
				if( max(Ls[*e],Rs[*e]) == al)
					w.pb(*e);
			}
			int ans = *min_element(ALL(w));
			a[ans]=1;
			if( k == j)
			{
				cout<<max(Ls[ans],Rs[ans])<<" "<<min(Ls[ans],Rs[ans])<<endl;
				break;
			}
		}
	}
}
	
