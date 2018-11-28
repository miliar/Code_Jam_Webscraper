#include <iostream>
#include <algorithm>
#include <math.h>
#include <string>
#include <queue>
#include <set>
using namespace std;
#define rep(i, n) for (int (i) = 0; (i) < (n); (i) ++)
#define rep1(i, n) for (int (i) = 1; (i) <= (n); (i) ++)
#define FOR(i, a, b) for (int (i) = (a); (i) <= (b); (i)++)
#define db(x) {cout << #x << " = " << (x) << endl;}
#define dba(a, x, y) {cout<<#a<<" :";FOR(i123,x,y)cout<<setw(4)<<(a)[i123];cout<<endl;}
#define clr(x) memset(x,0,sizeof(x));
#define mp make_pair
#define pb push_back
#define sz(x) int((x).size())


int main() {
    int t;
    cin >> t;

    int n;
    int k;
    multiset< int, std::greater<int> > s;
    rep1(Yo, t) {
        cin >> n;
        cin >> k;
        s.clear();
        s.insert(n);
        rep(Yeah, k - 1) {
            n = *s.begin() - 1;
            s.erase( s.begin() );
            s.insert( n >> 1 );
            s.insert( n - (n >> 1) );
        }

        n = *s.begin() - 1;
        cout << "Case #" << Yo << ": " << n - (n >> 1) << " " << (n >> 1) << endl;
    }

    return 0;
}
