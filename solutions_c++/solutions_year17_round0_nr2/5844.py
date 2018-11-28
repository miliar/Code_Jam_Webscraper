#// BISMILLAHIR RAHMANIR RAHIM
#include <bits/stdc++.h>
#include <algorithm>
using namespace std;
 
#define inf 0x3f3f3f3f
 
#define PI acos(-1)
#define eps 1e-9
//#define inf 100000000
#define MOD 1000000007
//#define harmonic(n) 0.57721566490153286l+log(n)
 
#define mem(a,b) memset(a, b, sizeof(a) )
#define gcd(a,b) __gcd(a,b)
#define lcm(a,b) (a*(b/gcd(a,b)))
#define sqr(a) ((a) * (a))
 
int dx[] = {0, 0, +1, -1};
int dy[] = {+1, -1, 0, 0};
//int dx[] = {+1, 0, -1, 0, +1, +1, -1, -1};
//int dy[] = {0, +1, 0, -1, +1, -1, +1, -1};
 
inline bool EQ(double a, double b) { return fabs(a-b) < eps; }
//
//debug
#ifdef asif
template < typename F, typename S >
ostream& operator << ( ostream& os, const pair< F, S > & p ) {
            return os << "(" << p.first << ", " << p.second << ")";
}
 
template < typename T >
ostream &operator << ( ostream & os, const vector< T > &v ) {
            os << "{";
                for(auto it = v.begin(); it != v.end(); ++it) {
                                if( it != v.begin() ) os << ", ";
                                        os << *it;
                                            }
                    return os << "}";
}
 
template < typename T >
ostream &operator << ( ostream & os, const set< T > &v ) {
            os << "[";
                for(auto it = v.begin(); it != v.end(); ++it) {
                                if( it != v.begin() ) os << ", ";
                                        os << *it;
                                            }
                    return os << "]";
}
 
template < typename F, typename S >
ostream &operator << ( ostream & os, const map< F, S > &v ) {
            os << "[";
                for(auto it = v.begin(); it != v.end(); ++it) {
                                if( it != v.begin() ) os << ", ";
                                        os << it -> first << " = " << it -> second ;
                                            }
                    return os << "]";
}
 
#define dbg(args...) do {cerr << #args << " : "; faltu(args); } while(0)
 
void faltu () {
            cerr << endl;
}
 
template <typename T>
void faltu( T a[], int n ) {
            for(int i = 0; i < n; ++i) cerr << a[i] << ' ';
                cerr << endl;
}
 
template <typename T, typename ... hello>
void faltu( T arg, const hello &... rest) {
            cerr << arg << ' ';
                faltu(rest...);
}
#else
#define dbg(args...)
#endif // asif
 
int biton(int N, int pos) {return N = N | (1 << pos);}
int bitoff(int N, int pos) {return N = N & ~(1 << pos);}
bool check(int N, int pos) {return (bool)(N & (1 << pos));}
 
#define ll long long int
#define F first
#define S second
#define sc(a)           scanf("%d", &a)
#define sc2(a, b)       scanf("%d%d", &a, &b)
#define sc3(a, b, c)    scanf("%d%d%d", &a, &b, &c)
#define SS(a) scanf("%lli", &a)
#define P(a) printf("%i", a)
#define PP(a) printf("%lli", a)
#define FOR(i, a, b) for (int i = (a); i < (b); ++i)
#define REP(i, n) FOR(i, 0, n)

string s;

bool check( string st ){
	for(int i = 0; i < st.size() - 1; i++)
		if( st[i] > st[i+1] ) return false;
	return true;
}

string build( string st ){
	bool fool = true;
	for(int i = st.size() - 1; i >= 1; i--){
		if(fool == false) break;
 		if(st[i] < st[i-1]){
			st[i-1]--;
			for(int j = i; j < st.size(); j++){
				st[j] = '9';
			}
			fool = false;
		}
	}
	return st;
}

int main()
{
	freopen("B-large.in","r",stdin);
    freopen("TidyNumbers.txt","w",stdout);
	int t, cs = 0;
	string s;
	scanf("%i", &t);
	while(t--){
		cin >> s;
		while(1){
			if(check(s)) break;
			s = build(s);
		}
		bool ok = false;
		printf("Case #%i: ", ++cs);
		for(int i = 0; i < s.size(); i++){
			if(s[i] == '0' and ok == false) continue;
			cout << s[i];
			ok = true;
		}
		printf("\n");
	}
}