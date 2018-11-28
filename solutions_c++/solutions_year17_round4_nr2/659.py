#include<bits/stdc++.h>
using namespace std;
#define FOR(i,a,b) for(lli i=(lli)a;i<=(lli)b;i++)
#define endl "\n"
#define mp make_pair
#define X first
#define Y second
#define inf 1e18
#define mod 1000000007
#define pb push_back
#define pi 3.14159265359
#define gc getchar
#define Case cout<<"Case #"<<++cas<<": ";
#define fastio ios::sync_with_stdio(false);cin.tie(0);cout.tie(0);
#define all(v) v.begin(),v.end()
// #define lli int
typedef long long int lli;
typedef pair<int,int> pii;
typedef pair<lli,int> pli;
typedef vector<pii> vii;
typedef pair<lli,lli> pll;
typedef vector<lli> vl;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<vl> vvl;

#define pr(...) dbs(#__VA_ARGS__, __VA_ARGS__)
template <class T> void dbs(string str, T t) {cerr << str << " : " << t << "\n";}
template <class T, class... S> void dbs(string str, T t, S... s) {int idx = str.find(','); cerr << str.substr(0, idx) << " : " << t << ","; dbs(str.substr(idx + 1), s...);}
template <class S, class T>ostream& operator <<(ostream& os, const pair<S, T>& p) {return os << "(" << p.first << ", " << p.second << ")";}
template <class T>ostream& operator <<(ostream& os, const vector<T>& p) {os << "[ "; for (auto& it : p) os << it << " "; return os << "]";}
template <class T>ostream& operator <<(ostream& os, const set<T>& p) {os << "[ "; for (auto& it : p) os << it << " "; return os << "]";}
template <class S, class T>ostream& operator <<(ostream& os, const map<S, T>& p) {os << "[ "; for (auto& it : p) os << it << " "; return os << "]";}
template <class T> void prc(T a, T b) {cerr << "["; for (T i = a; i != b; ++i) {if (i != a) cerr << ", "; cerr << *i;} cerr << "]\n";}

lli A[1009],C[1009];

int main()
{
	lli T,n,c,m,p,b,cas=0,ans1,ans2,a;bool flag;
	cin>>T;
	while(T--)
	{
		lli mi=0;
		cin>>n>>c>>m;
		Case;
		memset(A,0,sizeof(A));
		memset(C,0,sizeof(C));		
		FOR(i,1,m)
		{
			cin>>p>>b;
			C[b]++;
			A[p]++;
		}
		FOR(i,1,c)
		mi=max(mi,C[i]);
		FOR(i,mi,1000)
		{
			a=0;flag=1;ans2=0;
			FOR(j,1,n)
			{
				if(A[j]<=i)
					a+=i-A[j];
				else
				{
					if(A[j]-a>i) {flag=0;break;}
					else {a-=A[j]-i;ans2+=A[j]-i;}
				}
			}
			if(flag) {ans1=i;break;}
		}
		cout<<ans1<<" "<<ans2<<endl;
	}
}