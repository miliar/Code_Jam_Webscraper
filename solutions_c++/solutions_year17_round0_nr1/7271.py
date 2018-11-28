#include <bits/stdc++.h>
using namespace std;
template <class T> int size(const T &x) { return x.size(); }

#define SCD(t) scanf("%d",&t)
#define forl(i,a,b) for (__typeof(a) i=(a); i<(b); ++i)
#define iter(it,c) for (__typeof((c).begin()) it = (c).begin(); it != (c).end(); ++it)

typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;

const int INF = ~(1<<31); // 2147483647
typedef long long ll;
typedef unsigned long long ull;
typedef long int li;   //int32
typedef unsigned long int uli;
typedef long long int lli;    //int64
typedef unsigned long long int ulli;

const double EPS = 1e-9;
const double pi = acos(-1);
typedef vector<vi> vvi;
typedef vector<vii> vvii;
template <class T> T smod(T a, T b) { return (a % b + b) % b; }
template<typename T, typename U> inline void amin(T &x, U y) { if(y < x) x = y; }
template<typename T, typename U> inline void amax(T &x, U y) { if(x < y) x = y; }


int main()
{

	#ifndef ONLINE_JUDGE
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	#endif
	int t;
	cin>>t;
	forl(u,0,t){
		string s;
		int k,c=0;
		cin>>s>>k;
		int n = s.length();
		forl(i,0,n-k+1){
			//string str = s.substr(i,k)
			if(s[i]=='-'){
				forl(p,0,k){
					if(s[i+p]=='+') s[i+p]='-';
					else s[i+p]='+';
				}
				c++;
			}
			
		}
		int h=0;
		forl(j,0,n){
			if(s[j]=='-'){
				h++;
			}
		}
		if(h) cout<<"Case #"<<u+1<<": IMPOSSIBLE"<<endl;
		else cout<<"Case #"<<u+1<<": "<<c<<endl;
	}

	return 0;
}

