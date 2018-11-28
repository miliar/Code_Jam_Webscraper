#include <iostream>
#include <algorithm>
#include <math.h>
#include <string>
#include <sstream>
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
#define ll long long

namespace patch
{
    template < typename T > std::string to_string( const T& n )
    {
        std::ostringstream stm ;
        stm << n ;
        return stm.str() ;
    }
}

bool isTidy(ll n)
{
    string s = patch::to_string(n);
    rep(i, s.length() - 1)
        if (s[i] > s[i + 1]) return false;
    return true;
}

ll TidyNum(ll n)
{
    ll mul = 1;
    while (n > 0)
    {
        // I am ~lazy~ so I sacrificed a bit of time complexity for code readibility
        if (isTidy(n)) return n;
        n -= ((n / mul) % 10 + 1) * mul;
        mul *= 10;
    }
    return 1;
}

int main()
{
    int t;
    cin >> t;

    ll n;
    rep1(Yo, t)
    {
        cin >> n;
        cout << "Case #" << Yo << ": " << TidyNum(n) << endl;
    }

    return 0;
}
