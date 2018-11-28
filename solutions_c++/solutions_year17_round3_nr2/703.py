#include <bits/stdc++.h>

#define ll long long
#define ull unsigned long long
#define st first
#define nd second
#define pii pair<int, int>
#define pil pair<int, ll>
#define pli pair<ll, int>
#define pll pair<ll, ll>
#define pw(x) ((1LL)<<(x))
#define lson l, m, rt<<1
#define rson m+1, r, rt<<1|1
#define FIN freopen("input.txt","r",stdin);
#define FOUT freopen("output.txt","w+",stdout);
using namespace std;
/***********/
template <class T>
bool scan (T &ret) {
    char c;
    int sgn;
    if (c = getchar(), c == EOF) return 0; //EOF
    while (c != '-' && (c < '0' || c > '9') ) c = getchar();
    sgn = (c == '-') ? -1 : 1;
    ret = (c == '-') ? 0 : (c - '0');
    while (c = getchar(), c >= '0' && c <= '9') ret = ret * 10 + (c - '0');
    ret *= sgn;
    return 1;
}
template<typename N,typename PN>inline N flo(N a,PN b){return a>=0?a/b:-((-a-1)/b)-1;}
template<typename N,typename PN>inline N cei(N a,PN b){return a>0?(a-1)/b+1:-(-a/b);}
template<typename T>
inline int sgn(T a) {return a>0?1:(a<0?-1:0);}
template <class T1, class T2>
bool gmax(T1 &a, const T2 &b) { return a < b? a = b, 1:0;}
template <class T1, class T2>
bool gmin(T1 &a, const T2 &b) { return a > b? a = b, 1:0;}

template<class A, class B, class C>
struct Triple {
    A st; B nd; C rd;
    bool operator <(const Triple &rhs) const {
        return st == rhs.st? (nd == rhs.nd? rd < rhs.rd: nd < rhs.nd): st < rhs.st;
    }
};
typedef Triple<int, int, int> tiii;

template<class T1, class T2>
ostream& operator <<(ostream &out, pair<T1, T2> p) {
    return out << "(" << p.st << ", " << p.nd << ")";
}
template<class A, class B, class C>
ostream& operator <<(ostream &out, Triple<A, B, C> t) {
    return out << "(" << t.st << ", " << t.nd << ", " << t.rd << ")";
}
template<class T>
ostream& operator <<(ostream &out, vector<T> vec) {
    out << "("; for(auto &x: vec) out << x << ", "; return out << ")";
}
const int inf = 0x3f3f3f3f;
const ll INF = 1e18;
const ll mod = 1e9+7;
const double eps = 1e-5;
const int N = 1e6+5;
/***********/

const int cir = 24*60;
int val[cir*3];
int main(){
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
    int t, ca = 1, n, k;
    scanf("%d", &t);
    while(t--){
        printf("Case #%d: ", ca++);
        memset(val, 0, sizeof(val));
        int ac, aj, x, y, sum1 = 0, sum2 = 0;
        scanf("%d%d", &ac, &aj);
        //vector<pii> pcd, pjk;
        for(int i = 0; i < ac; i++){
            scanf("%d%d", &x, &y);
            for(int j = x; j < y; j++)
                val[j] = val[j+cir] = 2;
            sum2 += y-x;
        }
        for(int i = 0; i < aj; i++){
            scanf("%d%d", &x, &y);
            for(int j = x; j < y; j++)
                val[j] = val[j+cir] = 1;
            sum1 += y-x;
        }
        if(ac == 0&&aj == 0){
            puts("2");
            continue ;
        }

        int pos = 1, lpos;
        while(val[pos] == 0||val[pos] == val[pos-1]) pos++;
        pos %= cir;

        //cd[pos] != 0, pos != pos-1
        int first = val[pos];//1 -1
        for(int i = pos-1+cir; i; i--)
            if(val[i] != 0) {
                lpos = i;
                break;
            }

        vector<pii> seq;
        if((lpos+1)%cir != pos&&val[pos] == val[lpos])
            seq.push_back({lpos+1, pos+cir});

        for(int i = pos; i < lpos; i++) if(val[i] == 0){
            int j = i+1;
            while(j < lpos&&val[j] == 0) j++;
            //val[i-1]
            if(val[i-1] == val[j]) seq.push_back({i, j});
            i = j;
        }
        sort(seq.begin(), seq.end(), [](pii a, pii b){ return a.nd-a.st < b.nd-b.st;}   );
        for(auto x: seq){
            int l = x.st, r = x.nd, sum = r-l;
            if(val[r] == 1){
                for(int i = l; i < r&&sum1 < cir/2; i++){
                    val[i] = 1;
                    sum1++;
                }
            }
            else {
                for(int i = l; i < r&&sum2 < cir/2; i++){
                    val[i] = 2;
                    sum2++;
                }
            }
        }

        if(sum1 == cir/2){
            for(int i = pos; i < lpos; i++)
                if(val[i] == 0) val[i] = 2, sum2++;
        }
        else if(sum2 == cir/2){
            for(int i = pos; i < lpos; i++)
                if(val[i] == 0) val[i] = 1, sum1++;
        }
        for(int i = pos; i < pos+cir; i++) if(val[i] == 0){
            if(sum1 == cir/2) val[i] = 2, sum2++;
            else if(sum2 == cir/2) val[i] = 1, sum1++;
            else val[i] = val[i-1];
        }

        int ans = val[pos] != val[pos+cir-1];
        if(ans == 1) {
            //printf("%d: %d\n", pos, val[pos]);
        }
        for(int i = pos+1; i < pos+cir; i++) if(val[i] != val[i-1]) {
            ans++;
            //printf("%d: %d\n", i, val[i]);
        }
        printf("%d\n", ans);
    }
    return 0;
}


