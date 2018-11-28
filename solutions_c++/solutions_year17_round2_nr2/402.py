#include <bits/stdc++.h>
#include <ext/hash_map>
#include <ext/hash_set>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
#include <ext/pb_ds/priority_queue.hpp>
using namespace std;
using namespace __gnu_cxx;
using namespace __gnu_pbds;
#define XINF INT_MAX
#define INF 0x3F3F3F3F
#define MP(X,Y) make_pair(X,Y)
#define PB(X) push_back(X)
#define REP(X,N) for(int X=0;X<N;X++)
#define REP2(X,L,R) for(int X=L;X<=R;X++)
#define DEP(X,R,L) for(int X=R;X>=L;X--)
#define CLR(A,X) memset(A,X,sizeof(A))
#define IT iterator
#define RIT reverse_iterator
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int,int> PII;
typedef vector<PII> VII;
typedef vector<int> VI;
typedef tree<int, null_type, greater<int>, rb_tree_tag, tree_order_statistics_node_update > rb_tree_set;
typedef tree<int, int, greater<int>, rb_tree_tag, tree_order_statistics_node_update > rb_tree;
#define PQ std::priority_queue
#define HEAP __gnu_pbds::priority_queue
#define X first
#define Y second
#define lson(X) ((X)<<1)
#define rson(X) ((X)<<1|1)

#define FILE_NAME "B-small-attempt0"

int bit[6] = {1,3,2,6,4,5};
char str[7] = "ROYGBV";

string gao(int c, char c1, char c2) {
    string s = "";
    s += c2;
    REP(i,c)
        s = (s + c1) + c2;
    return s;
}

int main()
{
#ifdef LOCAL
    freopen(FILE_NAME ".in","r",stdin);
    freopen(FILE_NAME ".out","w",stdout);
#endif // LOCAL
    ios::sync_with_stdio(false);
    int t,cs=1;
    cin>>t;
    while(t--) {
        //int a,ab,b,bc,c,ac;
        int a[6];
        int s = 0;
        int n;
        cin>>n;
        REP(i,6) cin>>a[i];
        int nc = 0;
        REP(i,6) if(a[i]) nc++;
        //cin>>a>>ab>>b>>bc>>c>>ac;
        //s = a+b+c+ab+bc+ac;
        string ans = "IMPOSSIBLE";
        if(nc == 2) {
            int x = -1, y = -1;
            REP(i,6) {
                if(a[i]) {
                    if(x==-1) x = i;
                    else y = i;
                }
            }
            if((bit[x]&bit[y])==0 && a[x] == a[y]) {
                ans = "";
                REP(i,a[x]) {
                    ans = ans + str[x] + str[y];
                }
            }
        }else if(nc > 2) {
            if(a[1] < a[4] && a[3] < a[0] && a[5] < a[2]) {
                int c1 = a[4] - a[1];
                int c2 = a[0] - a[3];
                int c3 = a[2] - a[5];
                int mx = max(max(c1, c2), c3);
                if(mx == c3 && c1 + c2 >= c3) {
                    //cout<<1<<endl;
                    ans = "";
                    REP(i,c3) {
                        if(!i==0) ans = ans + gao(a[5], str[5], str[2]);
                        else ans = ans + str[2];
                        if(i < c2) {
                            if(!i) ans = ans + gao(a[3], str[3], str[0]);
                            else ans = ans + str[0];
                        }
                        if(i + c1 >= c3) {
                            if(i + c1 == c3) ans = ans + gao(a[1], str[1], str[4]);
                            else ans = ans + str[4];
                        }
                    }
                }else if(mx == c1 && c2 + c3 >= c1) {
                    //cout<<2<<endl;
                    ans = "";
                    REP(i,c1) {
                        if(!i) ans = ans + gao(a[1], str[1], str[4]);
                        else ans = ans + str[4];
                        if(i < c2) {
                            if(!i) ans = ans + gao(a[3], str[3], str[0]);
                            else ans = ans + str[0];
                        }
                        if(i + c3 >= c1) {
                            if(i + c3 == c1) ans = ans + gao(a[5], str[5], str[2]);
                            else ans = ans + str[2];
                        }
                    }
                }else if(mx == c2 && c1 + c3 >= c2) {
                    //cout<<3<<endl;
                    ans = "";
                    REP(i,c2) {
                        if(!i) ans = ans + gao(a[3], str[3], str[0]);
                        else ans = ans + str[0];
                        if(i < c1) {
                            if(!i) ans = ans + gao(a[1], str[1], str[4]);
                            else ans = ans + str[4];
                        }
                        if(i + c3 >= c2) {
                            if(i + c3 == c2) ans = ans + gao(a[5], str[5], str[2]);
                            else ans = ans + str[2];
                        }
                    }
                }
            }
        }
        
        cout<<"Case #"<<cs++<<": "<<ans<<endl;
    }
    return 0;
}

