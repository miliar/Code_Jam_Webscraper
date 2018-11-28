#include <bits/stdc++.h>
#include <unordered_map>
#include <utility>
#include <tuple>

#define ll long long int
#define vi vector<int>
#define vl vector<ll>
#define pi pair<int>
#define tiii tuple<int,int,int> >
#define tiiii tuple<int,int,int,int>
#define pl pair<ll> pl
#define vpi vector< pair<int,int> >>

#define pb push_back
#define mp make_pair
#define F first
#define S second
#define mt make_tuple

#define DEBUG(x) cout << '>' << #x << ':' << x << endl;
#define REP(i,n) for(ll i=0;i<(n);i++)
#define FOR(i,a,b) for(ll i=(a);i<=(b);i++)
#define FORD(i,a,b) for(ll i=(a);i>=(b);i--)

#define all(v) (v).begin(),(v).end()

inline bool EQ(double a, double b) { return fabs(a-b) < 1e-9; }
const ll INF = 1<<29;
inline ll two(ll n) { return 1 << n; }
inline ll test(ll n, ll b) { return (n>>b)&1; }
inline void setBit(ll & n, ll b) { n |= two(b); }
inline void unsetBit(ll & n, ll b) { n &= ~two(b); }
inline ll last_bit(ll n) { return n & (-n); }
inline ll ones(ll n) { ll res = 0; while(n && ++res) n-=n&(-n); return res; }

inline int parent(int x){return floor((x-1)/2);};
inline int left(int x) {return 2*x+1;};
inline int right(int x){return 2*x+2;};

inline bool sortDown(ll x,ll y){return x>y;}
inline bool sortPairSecondInc( std::pair< ll,ll > p1, std::pair< ll,ll > p2){ return p1.S<p2.S;}
inline bool sortPairSecondDec( std::pair< ll,ll > p1, std::pair< ll,ll > p2){ return p1.S>p2.S;}
inline bool sortPairFirstDec( std::pair< ll,ll > p1, std::pair< ll,ll > p2){ return p1.F>p2.F;}

inline bool sortDownByLen( std::pair< ll,ll > p1, std::pair< ll,ll > p2 ){ return p1.S-p1.F > p2.S-p2.F;}


const int mod = 1000000007;
const int N = 4e5+5;
const int ifact_n_minus_1 = 977041169;
using namespace std;
/////////////////////////////////////////////////////////////////////

int t;
ll n;
bool ok;
ll dig[100];

int main()
{
    std::ios::sync_with_stdio(false);
    cin.tie(0);

    cin>>t;
    FOR(z,1,t){
    	cin>>n;

    	ok=false;
    	ll index=0;
    	ll remember=n;
    	ll rem;
    	while(n!=0){
    		rem = n%10;
    		n /=10;
    		dig[index++]=rem;
    	}

    	// DEBUG(index);
    	// FOR(i,0,index-1){
    	// 	cout<<dig[i]<<" ";
    	// }
    	// cout<<endl;


    	ll start=index-1;
    	FORD(i,index-2,0){
    		if(dig[i+1]<dig[i]){
    			start=i;
    		}
    		else if(dig[i+1]>dig[i]){
    			ok=true;
    			// DEBUG(start);
    			cout<<"Case #"<<z<<": ";
    			FORD(i,index-1,start+1){
    				cout<<dig[i];
    			}
    			if(dig[start]!=1){
    				cout<<dig[start]-1;
    			}

    			FORD(i,start-1,0){
    				cout<<9;
    			}
    			cout<<endl;
    			break;
    		}
    	}

    	if(!ok){
    		cout<<"Case #"<<z<<": "<<remember<<endl;
    	}

    }

}

