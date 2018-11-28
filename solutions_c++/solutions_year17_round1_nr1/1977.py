
#pragma GCC optimize ("O3")
#pragma GCC target ("avx")

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


int nTestcase;

int width, height;
int m, n;

int main() {
    int i, j, k;
    int x, y, a, b;

    cin >> nTestcase;


    repeat(nTestcase) {
        vector<string> field;
        set<char> charset;

        cin >> height >> width;

        int hatena = 0;

        
        repeat(height) {
            field.emplace_back();
            cin >> field.back();
            repeat(width) {
                char c = field.back()[cnt];
                hatena += c == '?';
                //charset.insert(c);
            }
        }
        //charset.erase('?');

        // if (charset.size() == 1) {
        //     for (string& s : field) {
        //         fill(ALL(s), *charset.begin());
        //     }
        // }
        for (y = 0; y < height; ++y) {
            for (x = 0; x < width; ++x) {
                if (field[y][x] != '?') {
                    for (i = x - 1; 0 <= i && field[y][i] == '?'; --i) {
                        field[y][i] = field[y][x];
                    }
                    for (i = x + 1; i < width && field[y][i] == '?'; ++i) {
                        field[y][i] = field[y][x];
                    }
                }
            }
        }
        for (x = 0; x < width; ++x) {
            for (y = 0; y < height; ++y) {
                if (field[y][x] != '?') {
                    for (i = y - 1; 0 <= i && field[i][x] == '?'; --i) {
                        field[i][x] = field[y][x];
                    }
                    for (i = y + 1; i < height && field[i][x] == '?'; ++i) {
                        field[i][x] = field[y][x];
                    }
                }
            }
        }
        

        printf("Case #%d:\n", cnt + 1);

        for (string& s : field) {
            cout << s << endl;
        }
    }


    return 0;
}