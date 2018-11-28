#define _CRT_SECURE_NO_DEPRECATE
#pragma comment(linker, "/STACK:16777216")
#include <ctime>
#include <string>
#include <vector>
#include <map>
#include <list>
#include <set>
#include <queue>
#include <iostream>
#include <sstream>
#include <stack>
#include <deque>
#include <cmath>
#include <memory.h>
#include <cstdlib>
#include <cstdio>
#include <cctype>
#include <algorithm>
#include <utility>
using namespace std;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int,int> pii;
typedef long long ll;
typedef istringstream iss;
#define FOR(i,f,n) for(int i=f; i<n; ++i)
#define sz(a) ((int)a.size())
#define fill(w,v) memset(w,v,sizeof(w))
#define pb push_back
#define all(a) a.begin(),a.end()
#define mp make_pair
#define inf 1000000000
#define X first
#define Y second
template<class T> inline T gcd(T a, T b){T t; while (a && b) t = a, a = b%a, b = t; return a+b; }
template<class T> inline T power(T a, int p) {T r = T(1); while (p) { if (p&1) r = r*a; a = a*a; p >>= 1; } return r; }
template<class T> T extgcd(T a, T b, T& x, T& y) { if (b==0) return x=1, y=0, a; T x1, y1, g; g = extgcd(b, a%b, x1, y1); x = y1; y = x1 - a/b*y1; return g; }
template<class T> inline T Floor(T a, T b) { if (b<0) a=-a, b=-b; if (a<0) return (a-b+1)/b; return a/b; }
template<class T> inline T Ceil(T a, T b) { if (b<0) a=-a, b=-b; if (a<0) return a/b; return (a+b-1)/b; }

int N, M, K;

int main()
{
        freopen("inB.txt", "r", stdin);
        freopen("outB.txt", "w", stdout);
        clock_t startTime = clock();

        int Cases;
        scanf("%d", &Cases);
        FOR(Case,0,Cases)
        {
                printf("Case #%d: ", Case+1);
                fprintf(stderr, "Case #%d :\n", Case+1);

                char ss[50];
                scanf("%s", ss);
                char *s = ss;

                int i=0;
                for (i=1; s[i]; i++) {
                        if (s[i-1]>s[i]) break;
                }
                if (s[i]) {
                        for (i--; i>=0 && (s[i]<='1' || (i>0 && s[i-1]==s[i])); i--) {
                        }
                        if (i == -1) {
                                s++;
                                i=0;
                        } else {
                                s[i]--;
                                i++;
                        }
                        for (; s[i]; i++) {
                                s[i] = '9';
                        }
                }
                puts(s);
        }

        clock_t endTime = clock();
        fprintf(stderr, "\nTime: %.3lf\n", double(endTime-startTime)/CLOCKS_PER_SEC);
        return 0;
}
