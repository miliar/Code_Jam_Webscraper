#include<bits/stdc++.h>
#define _ ios_base::sync_with_stdio(0);cin.tie(0);
using namespace std;
#define all(x)      (x).begin(), (x).end()
#define re(i,s,n)  	for(int i=s;i<(n);++i)
#define fr(i,n)     re(i,0,n)
#define tr(i,x)     for(typeof(x.begin()) i=x.begin();i!=x.end();++i)
#define mp make_pair
#define SSTR( x ) dynamic_cast< std::ostringstream & >( \
        ( std::ostringstream() << std::dec << x ) ).str()
#define StartTime          clock_t begin = clock()
#define EndTime            clock_t end = clock()
#define DisplayTime        (double(end - begin) / CLOCKS_PER_SEC)

typedef vector<int> vi;
typedef vector<string> vs;
typedef long long ll;
typedef unsigned long long ull;
typedef double db;
typedef long double ldb;
template<class T> T gcd(T a, T b) {
    return b ? gcd(b, a % b) : a;
}
const double EPS = 1e-7;
const ll MOD = 1000000007;
const db PI = acos(-1);

const int BASE = 10;

bool checkTidy(ull n){    
    int last = BASE, d;
    while(n){
        d = n % BASE;
        if(d>last){
            return false;
        }
        last = d;
        n /= BASE;
    }
    return true;
}

ull solve(ull n){
    for(ull cur=n;cur>=1;cur--){
        if(checkTidy(cur)){
            return cur;
        }
    }
}

int main() {
    int t;
    cin >> t;

    for(int _t=1;_t<=t;_t++){
        ull n;
        cin >> n;
        
        cout << "Case #" << _t << ": " << solve(n) << endl;
    }
    return 0;
}
