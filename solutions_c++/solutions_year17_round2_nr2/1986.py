// {{{
#include <bits/stdc++.h>
#define MP make_pair
#define PB push_back
#define ALL(x) begin(x),end(x)
#define SZ(x) ((int)x.size())
#define FOR(i,n) for(int i=0;i<n;i++)
#define REP(i,a,b) for(int i=a;i<=b;i++)
using namespace std;
using LL=long long;
using PII=pair<int,int>;
using VI=vector<int>;

#ifdef FEI
template<typename T>
void _dump(const char* s, T&& head) { cerr<<s<<"="<<head<<endl; }
template<typename T, typename... Args>
void _dump(const char* s, T&& head, Args&&... tail) {
    int c=0;
    while (*s!=',' || c!=0) {
        if (*s=='(' || *s=='[' || *s=='{') c++;
        if (*s==')' || *s==']' || *s=='}') c--;
        cerr<<*s++;
    }
    cerr<<"="<<head<<", ";
    _dump(s+1, tail...);
}

#define dump(...) do { \
    fprintf(stderr, "%s:%d - ", __PRETTY_FUNCTION__, __LINE__); \
    _dump(#__VA_ARGS__, ##__VA_ARGS__); \
} while(0);

template<typename Iter>
ostream& _out(ostream &s, Iter b, Iter e) {
    s<<'[';
    for (auto it=b; it!=e; it++) s<<(it==b?"":",")<<*it;
    s<<']';
    return s;
}

template<typename A, typename B>
ostream& operator <<(ostream &s, const pair<A,B> &p) { return s<<"("<<p.first<<","<<p.second<<")";}
template<typename T>
ostream& operator <<(ostream &s, const vector<T> &x) { return _out(s,ALL(x)); }
template<typename T, size_t N>
ostream& operator <<(ostream &s, const array<T,N> &x) { return _out(s,ALL(x)); }
template<typename T>
ostream& operator <<(ostream &s, const set<T> &x) { return _out(s,ALL(x)); }
template<typename A, typename B>
ostream& operator <<(ostream &s, const map<A,B> &x) { return _out(s,ALL(x)); }
#else
#define dump(...)
#endif

template<typename T>
void _R(T &x) { cin>>x; }
void _R(int &x) { scanf("%d",&x); }
void _R(LL &x) { scanf("%" PRId64,&x); }
void _R(double &x) { scanf("%lf",&x); }
void _R(char &x) { scanf(" %c",&x); }
void _R(char *x) { scanf("%s",x); }

void R(){}
template<typename T, typename... X>
void R(T& head, X&... tail) { _R(head); R(tail...); }
// }}}

int main() {
    int T;
    R(T);
    for (int t=1; t<=T; t++) {
        int n, r, o, y, g, b, v;
        R(n, r, o, y, g, b, v);
        // 001 = r, 010 = y, 100 = b, 011 = o, 101 = v, 110 = g
        const int R = 1, O = 3, Y = 2, G = 6, B = 4, V = 5;
        int clr[10] = {0, r, y, o, b, v, g};
        int half = n/2;

        clr[B] -= clr[O];
        clr[R] -= clr[G];
        clr[Y] -= clr[V];

        n = clr[B] + clr[R] + clr[Y];

        VI order;

        if (clr[B]>=clr[R] && clr[B]>=clr[Y]){
            if (clr[R]>=clr[Y]) order = {B, R, Y};
            else order = {B, Y, R};
        }
        else if (clr[R]>=clr[B] && clr[R]>=clr[Y]){
            if (clr[B]>=clr[Y]) order = {R, B, Y};
            else order = {R, Y, B};
        }
        if (clr[Y]>=clr[R] && clr[Y]>=clr[B]){
            if (clr[R]>=clr[B]) order = {Y, R, B};
            else order = {Y, B, R};
        }

        int ans[1005]={}, flag = 0;
        for (int i=0; clr[B]||clr[R]||clr[Y]; i++) {
            if (i == 10000) {
                flag = 1;
                break;
            }
        //    dump(i, clr[B], clr[Y], clr[R]);
            if (ans[i%n]) continue;
            if (clr[order[0]]) {
                int c = order[0];
                if (!(ans[(i-1+n)%n]&c) && !(ans[(i+1)%n]&c)) {
                    ans[i%n] = c;
                    clr[c]--;
                }
            }
            else if (clr[order[1]]) {
                int c = order[1];
                if (!(ans[(i-1+n)%n]&c) && !(ans[(i+1)%n]&c)) {
                    ans[i%n] = c;
                    clr[c]--;
                }
            }
            else if (clr[order[2]]) {
                int c = order[2];
                if (!(ans[(i-1+n)%n]&c) && !(ans[(i+1)%n]&c)) {
                    ans[i%n] = c;
                    clr[c]--;
                }
            }
        }

        printf("Case #%d: ", t);
        if (flag) {
            puts("IMPOSSIBLE");
            continue;
        }

        for (int i=0; i<n; i++) {
            assert(ans[i]);
            if (ans[i] == B) {
                printf("B");
                while (clr[O]) {
                    printf("OB");
                    clr[O]--;
                }
            }
            else if (ans[i] == R) {
                printf("R");
                while (clr[G]) {
                    printf("GR");
                    clr[G]--;
                }
            }
            else if (ans[i] == Y) {
                printf("Y");
                while (clr[V]) {
                    printf("VY");
                    clr[V]--;
                }
            }
        }
        puts("");


    }

    return 0;
}
