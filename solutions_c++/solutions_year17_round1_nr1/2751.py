#include <set>
#include <map>
#include <list>
#include <cmath>
#include <queue>
#include <stack>
#include <cstdio>
#include <string>
#include <vector>
#include <cstdlib>
#include <cstring>
#include <sstream>
#include <iomanip>
#include <iostream>
#include <algorithm>
#include <ctime>
#include <deque>
#include <bitset>
#include <cctype>
#include <utility>

#define ULL unsigned long long
#define LL long long
#define FOR(i,a,b) for(int i = (a); i <= (int)(b); i++)
#define FO(i,a,b) for(int i = (a); i < (int)(b); i++)
#define FORD(i,a,b) for(int i= (a); i >= (int)(b); i--)
#define FOD(i,a,b) for(int i= (a); i > (int)(b); i--)
#define FORV(i,a) for(typeof(a.begin()) i = a.begin(); i != a.end(); i++)
#define SET(a,c) memset(a, c, sizeof(a))
#define sz(a) ((int)(a).size())
#define all(a) (a).begin(), (a).end()
#define fi first
#define se second
#define pb push_back
#define mp make_pair
#define FI first
#define SE second
#define PB push_back
#define MP make_pair
#define eps 1e-5
#define infi 1e9
#define PI 2*acos(0.0)
#define debug(k,F,n) FOR(i,1,n){FOR(j,1,n) cout << setw(k) << F[i][j]  ; cout << endl;}
using namespace std;

typedef pair<int,int>II;
typedef pair<int,II>PII;
typedef vector<int> VI;
typedef vector<II> VII;
typedef set<int> SI;
typedef map<string,int> MSI;
typedef map<int,int> MII;

template<class T> T gcd(T a, T b) {
    T r;
    while (b != 0) {
        r = a % b;
        a = b;
        b = r;
    }
    return a;
}
template<class T> T lcm(T a, T b) {
    return a / gcd(a, b) * b;
}
template<class T> T sqr(T x) {
    return x * x;
}
template<class T> T cube(T x) {
    return x * x * x;
}
template<class T> int getbit(T s, int i) {
    return (s >> i) & 1;
}
template<class T> T onbit(T s, int i) {
    return s | (T(1) << i);
}
template<class T> T offbit(T s, int i) {
    return s & (~(T(1) << i));
}
template<class T> T togglebit(T s, int i) {
    return s ^ (T(1) << i);
}
template<class T> int cntbit(T s) {
    return s == 0 ? 0 : cntbit(s >> 1) + (s & 1);
}
#define maxn  305
#define MOD 1000000005

int test, nTest = 0;
int r,c;
string s;
char a[100][100];
pair<int,int> min_[1000], max_[1000];
// first = dong
// second = cot

int apper[1000];
set<char> chars;
int need = 0;


int main()
{
    freopen("input.in","r",stdin);
    freopen("test.out","w",stdout);
    cin >> test;
    while (test--) {
        cin >> r >> c;
        FOR (i,1,100) apper[i] = 0;
        chars.clear();
        need = 0;

        FOR (i,1,r) {
            cin >> s;
            //cout  << s << endl;
            FO (j,0,s.length()) {
                a[i][j+1] = s[j];
                if (s[j] != '?') {
                    chars.insert(s[j]);
                    if (apper[s[j]] == 0) {
                        apper[s[j]] = 1;
                        min_[s[j]] = mp(i,j+1);
                        max_[s[j]] = mp(i,j+1);
                    }   else {
                        max_[s[j]].first = i;
                        max_[s[j]].second = max(max_[s[j]].second, j+1);
                        min_[s[j]].second = min(min_[s[j]].second, j+1);
                    }
                }
            }
        }

        FORV(it, chars) {
            char c = *it;
            FOR (i,min_[c].first, max_[c].first)
                FOR (j, min_[c].second, max_[c].second) {
                    a[i][j] = c;
                }
        }

        FOR (i,1,r)
            FOR (j,1,c)
                if (a[i][j] ==  '?') need ++;

//        while (need > 0) {
        FORV (it, chars) {
            char c  = *it;
            //cout << c << endl;
            int tren_trai_dong = min_[c].first;
            int tren_trai_cot = min_[c].second;
            int duoi_phai_dong = max_[c].first;
            int duoi_phai_cot = max_[c].second;

            while (true) {
                bool co_dich = false;
                bool dich_ok;

                // check dich trai
                dich_ok = true;
                if (tren_trai_cot > 1) {
                    FOR (i,tren_trai_dong, duoi_phai_dong)
                        if (a[i][tren_trai_cot-1] != '?') dich_ok = false;
                    if (dich_ok) {
                        FOR (i,tren_trai_dong, duoi_phai_dong)
                            a[i][tren_trai_cot-1] = c;
                        tren_trai_cot--;
                        co_dich = true;
                    }
                }

                // check dich phai
                dich_ok = true;
                if (duoi_phai_cot < c) {
                    FOR (i,tren_trai_dong, duoi_phai_dong)
                        if (a[i][duoi_phai_cot+1] != '?') dich_ok = false;
                    if (dich_ok) {
                        FOR (i,tren_trai_dong, duoi_phai_dong)
                            a[i][duoi_phai_cot+1] = c;
                        duoi_phai_cot++;
                        co_dich = true;
                    }
                }

                // check dich len tren

                dich_ok = true;
                if (tren_trai_dong > 1) {
                    FOR (j,tren_trai_cot, duoi_phai_cot)
                        if (a[tren_trai_dong-1][j] != '?') dich_ok = false;
                    if (dich_ok) {
                        FOR (j,tren_trai_cot, duoi_phai_cot)
                            a[tren_trai_dong-1][j] = c;
                        tren_trai_dong--;
                        co_dich = true;
                    }
                }


                // check dich xuong
                dich_ok = true;
                if (duoi_phai_dong < r) {
                    FOR (j,tren_trai_cot, duoi_phai_cot)
                        if (a[duoi_phai_dong+1][j] != '?') dich_ok = false;
                    if (dich_ok) {
                        FOR (j,tren_trai_cot, duoi_phai_cot)
                            a[duoi_phai_dong+1][j] = c;
                        duoi_phai_dong++;
                        co_dich = true;
                    }
                }

                if (co_dich == false)
                    break;
            }
        }
//        }

        printf("Case #%d:\n", ++nTest);

        FOR (i,1,r) {
            FOR (j,1,c) cout << a[i][j];
            cout << endl;
        }
        //cout << endl;

    }
    return 0;
}
