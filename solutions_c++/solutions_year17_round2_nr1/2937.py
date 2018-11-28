
// Created by bhuvi -->>

#include <iostream>
#include <sstream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <cctype>
#include <string>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <algorithm>
#include <functional>
using namespace std; 

#define PI 3.141592653589793
#define CLR(a) memset( a, 0, sizeof a )
#define DEBUG(x) cout << '>' << #x << ':' << x << endl;
#define REP(i,n) for(int i=0;i<(n);i++)
#define FOR(i,a,b) for(int i=(a);i<=(b);i++)
#define sz(x) ((int)x.size())
#define fill(a,x) memset(a,x,sizeof a)
#define all(x) (x).begin(),(x).end()
#define gcd(a,b)  __gcd(a,b)
#define EPS (double)(1e-9)
#define MOD 1000000007
#define pb push_back
#define mp make_pair
const int dr [] = {-1, -1, 0, 1, 1, 1, 0, -1};
const int dc [] = {0, 1, 1, 1, 0, -1, -1, -1};
const int px[] = {1, 0, -1, 0};
const int py[] = {0, 1, 0, -1};
const int INF = 1<<29;

inline bool EQ(double a,double b) { return fabs(a-b) < 1e-9 ;}
typedef long long ll;
inline int two(int n) { return 1 << n; }
inline int test(int n, int b) { return (n>>b)&1; }
inline void set_bit(int & n, int b) { n |= two(b); }
inline void unset_bit(int & n, int b) { n &= ~two(b); }
inline int last_bit(int n) { return n & (-n); }
inline int ones(int n) { int res = 0; while(n && ++res) n-=n&(-n); return res; }
template<class T> void chmax(T &a ,const T &b) {a=max(a,b) ;}
template<class T> void chmin(T & a, const T & b) {a=min(a,b) ;}

// Convert int to string
template<typename T> 
string to_str(T str)
{ 
	stringstream stream;
	stream << str;
	return stream.str();
}

// Convert string to int
template<typename T>
int to_int(T num)
{
    int val;
    stringstream stream;
    stream << num;
    stream >> val;
    return val;
}

// Split String by Single Character Delimiter
vector<string> split(const string &s,char delim)
{
    vector<string> elems;
    stringstream ss(s);
    string item;
    while(getline(ss,item,delim))
	    elems.push_back(item);
    return elems;
}
ll power(ll a, ll n) {ll p = 1;while (n > 0) {if(n%2) {p = p * a;} n >>= 1; a *= a;} return p;}
ll power(ll a, ll n, ll mod) {ll p = 1;while (n > 0) {if(n%2) {p = p * a; p %= mod;} n >>= 1; a *= a; a %= mod;} return p % mod;}

int main()
{
    
    int test;
    scanf("%d",&test);

    FOR(q,1,test){

        long long dist;
        int n;

        cin>>dist;
        cin>>n;
        double maxi=0.000000;
        for(int p=0;p<n;p++){
            long long k,s;
            cin>>k>>s;

            maxi=max(maxi,(double(dist-k)/s));


        }

        double ans=(double)dist/maxi;

        printf("Case #%d: %0.6f\n",q,ans);

    }

	
    return 0;
}
