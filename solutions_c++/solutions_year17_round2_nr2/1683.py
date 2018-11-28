#include "bits/stdc++.h"

#ifdef WINT_MIN
#define __MAI
#endif

using namespace std;
typedef unsigned int uint;
typedef long long int ll;
typedef unsigned long long int ull;

#define debugv(v) printf("L%d %s => ",__LINE__,#v);for(auto e:v){cout<<e<<" ";}cout<<endl;
#define debugm(m) printf("L%d %s is..\n",__LINE__,#m);for(auto v:m){for(auto e:v){cout<<e<<" ";}cout<<endl;}
#define debuga(m,w) printf("L%d %s is => ",__LINE__,#m);for(int x=0;x<(w);x++){cout<<(m)[x]<<" ";}cout<<endl;
#define debugaa(m,w,h) printf("L%d %s is..\n",__LINE__,#m);for(int y=0;y<(h);y++){for(int x=0;x<(w);x++){cout<<(m)[x][y]<<" ";}cout<<endl;}
#define debugaar(m,w,h) printf("L%d %s is..\n",__LINE__,#m);for(int y=0;y<(h);y++){for(int x=0;x<(w);x++){cout<<(m)[y][x]<<" ";}cout<<endl;}
#define ALL(v) (v).begin(),(v).end()
#define repeat(l) for(auto cnt=0;cnt<(l);++cnt)
#define BIGINT 0x7FFFFFFF
#define E107 1000000007ll
void printbit(int u) { if (u == 0)cout << 0; else { int s = 0, k = 0; for (; 0<u; u >>= 1, k++)s = (s << 1) | (u & 1); for (; 0<k--; s >>= 1)cout << (s & 1); } }template<typename T1, typename T2>
    ostream& operator <<(ostream &o, const pair<T1, T2> p) { o << "(" << p.first << ":" << p.second << ")"; return o; }

#define TIME chrono::system_clock::now()
#define MILLISEC(t) (chrono::duration_cast<chrono::milliseconds>(t).count())

namespace {
    std::chrono::system_clock::time_point t;
    void tic() { t = TIME; }
    void toc() { fprintf(stderr, "TIME : %lldms\n", MILLISEC(TIME - t)); }
    std::chrono::system_clock::time_point tle = TIME;
#ifdef __MAI
    void safe_tle(int msec) { assert(MILLISEC(TIME - tle) < msec); }
#else
#define safe_tle(k) ;
#endif
}

#ifndef __MAI 
namespace {
    class MaiScanner {
    public:
        template<typename T>
        void input_integer(T& var) {
            var = 0;
            T sign = 1;
            int cc = getchar_unlocked();
            for (; cc<'0' || '9'<cc; cc = getchar_unlocked())
                if (cc == '-') sign = -1;
            for (; '0' <= cc&&cc <= '9'; cc = getchar_unlocked())
                var = (var << 3) + (var << 1) + cc - '0';
            var = var*sign;
        }
        void ign() { getchar_unlocked(); }
        MaiScanner& operator>>(int& var) {
            input_integer<int>(var);
            return *this;
        }
        MaiScanner& operator>>(long long& var) {
            input_integer<long long>(var);
            return *this;
        }
    };
}
MaiScanner scanner;
#else
#define scanner cin
#endif

int testcases;

int n;// , rr, oo, yy, gg, bb, vv;
pair<int,char> colors[6];

char name[6] = { 'R','O','Y','G','B','V' };

int main() {
    int i, j, k;
    int x, y, a, b;

    scanner >> testcases;

    repeat(testcases) {
        printf("Case #%d: ", cnt + 1);

        scanner >> n;
        repeat(6) { scanner >> colors[cnt].first; colors[cnt].second = name[cnt]; }

        sort(colors, colors + 6, [](auto l, auto r) {return l.first > r.first; });

        if (colors[2].first < colors[0].first - colors[1].first) {
            cout << "IMPOSSIBLE" << endl;
        }
        else {
            int l, c;
            int f = colors[0].second;
            colors[0].first++;
            l = -1;
            do {

                for (int i = 0; i < 6; ++i) {
                    if (l == colors[i].second) continue;
                    if (f == colors[i].second && colors[i].first == 1) { colors[i].first--; break; }

                    l = colors[i].second;
                    cout << colors[i].second;
                    --colors[i].first;
                    break;
                }
                sort(colors, colors + 6, [](auto l, auto r) {return l.first > r.first; });
                
            } while (colors[0].first);

            cout << endl;
        }
        

    }

    return 0;
}