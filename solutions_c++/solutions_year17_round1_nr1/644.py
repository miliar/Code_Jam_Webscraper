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
char A[50][50];
int main()
{
	lli T,r,c,cas=0,ind;char ch;
	cin>>T;
	while(T--)
	{
		cin>>r>>c;
		FOR(i,1,r)
		FOR(j,1,c)
		cin>>A[i][j];
		FOR(i,1,r)
		{
			ch='?';
			FOR(j,1,c)
			if(A[i][j]!='?')
			{
				ch=A[i][j];
				break;
			}
			FOR(j,1,c)
			if(A[i][j]!='?')
				break;
			else A[i][j]=ch;
			FOR(j,1,c)
			if(A[i][j]=='?')
				A[i][j]=ch;
			else ch=A[i][j];
			// if(A[i][1]=='?')
				// s.insert(i);
		}
		FOR(i,1,r)
		if(A[i][1]!='?')
		{
			ind=i;break;
		}
		FOR(i,ind+1,r)
		if(A[i][1]=='?')
		{
			FOR(j,1,c)
			A[i][j]=A[i-1][j];
		}
		for(lli i=ind-1;i>=1;i--)
			if(A[i][1]=='?')
			{
				FOR(j,1,c)
				A[i][j]=A[i+1][j];
			}
		Case;cout<<endl;
		FOR(i,1,r)
		{
			FOR(j,1,c)
			cout<<A[i][j];
			cout<<endl;
		}
	}
}