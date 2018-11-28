#pragma comment(linker, "/STACK:16777216")
#define _CRT_SECURE_NO_WARNINGS
#define _USE_MATH_DEFINES
#include <cstdio>
#include <cmath>
#include <cctype>
#include <cassert>
#include <cstring>
#include <cstdlib>
#include <utility>
#include <string>
#include <map>
#include <set>
#include <vector>
#include <queue>
#include <ctime>
#include <stack>
#include <algorithm>
#include <numeric>
#include <complex>
#include <functional>
#include <list>
#include <iostream>
using namespace std;

#define C(_a, _v) memset(_a,_v,sizeof(_a))
#define ALL(_obj) (_obj).begin(),(_obj).end()
#define FORB(_i,_a,_b) for((_i)=(_a);(_i)<(_b);++(_i))
#define FORE(_i,_a,_b) for((_i)=(_a);(_i)<=(_b);++(_i))
#define FOR(_i,_n) FORB(_i,0,_n)
#define FORS(_i,_obj) FOR(_i,(_obj).size())
#define ADJ(_i,_v) for((_i)=kick[_v];(_i)>=0;(_i)=foll[_i])
#define X first
#define Y second
#define I64 "%lld"
#define pb push_back
#define ppb pop_back
#define mp make_pair

typedef long long i64;
typedef vector<int> vi;
typedef pair<int, int> pii;
typedef pair<i64, i64> pii64;
typedef vector<pii> vpii;

template<typename T>inline bool remin(T&c,const T&n){if(n<c){c=n;return 1;}return 0;}
template<typename T>inline bool remin2(T&c,const T&n){if(c<0||n<c){c=n;return 1;}return 0;}
template<typename T>inline bool remax(T&c,const T&n){if(c<n){c=n;return 1;}return 0;}
template<typename T>inline void addmod(T&c,const T&n,const T&m){c = (c + n) % m;}

int _in;int in(){scanf("%d",&_in);return _in;}

const double EPS = 1e-6;
const int INF = ~(1 << 31);
const i64 LINF = ~(1LL << 63);

#define sqr(x) (x)*(x)

// stuff cutline

int main(){
//#ifndef _DEBUG
    freopen("B-large.in", "r", stdin);
    freopen("test.out", "w", stdout);
//#endif
    //freopen("output.txt", "w", stdout);
//    ios_base::sync_with_stdio(false);
    
    int t;
    scanf("%d", &t);
    string s;
    getline(cin, s);
    for (int k = 1; k <= t; k++) {
        getline(cin, s);
        for (int i = s.size() - 1; i > 0; i--) {
            if (s[i] < s[i - 1]) {
                for (int j = i; j < s.size(); j++) {
                    s[j] = '9';
                }
                s[i - 1]--;
            }
        }
        printf("Case #%d: ", k);
        bool found = false;
        for (int i = 0; i < s.size(); i++) {
            if (s[i] != '0') {
                found = true;
                printf("%c", s[i]);
            } else {
                if (found) {
                    printf("%c", s[i]);
                }
            }
        }
        printf("\n");
    }
    
    return 0;
}



