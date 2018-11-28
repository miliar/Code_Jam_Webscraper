#include <iostream>
#include <fstream>
#include <sstream>
#include <string.h>
#include <algorithm>
#include <cmath>
#include <assert.h>
#include <stack>
#include <queue>
#include <list>
#include <vector>
#include <map>
#include <set>

#define DEBUG 1

#define for0(i,n) for (int i=0; i<n; i++)
#define forr(i,n) for (int i=n-1; i>=0; i--)
#define fori(i,a,b) for (int i=a; i<=b; i++)
#define iter(c) for(auto it=c.begin(); it!=c.end(); it++)
#define vec(x) vector< x >
#define pb push_back
#define ms(a,z) memset(a,z,sizeof(a));
#define mp make_pair
#define X first
#define Y second
#define sqr(x) 1LL*(x)*(x)
#define max(a,b) ((a)>(b)?(a):(b))
#define min(a,b) ((a)<(b)?(a):(b))
#define all(a) a.begin(),a.end()
#define size(x) (int)(x).size()
#define read(x) int x; scanf("%d",&x);
#ifdef DEBUG
#define nl cout<<"\n";
#define pr(x) cout<<(x)<<" ";
#define prl(x) cout<<#x " = "<<x<<endl;
#define prp(x) cout<<"("<<(x).first<<" "<<(x).second<<") ";
#define printv(v) {for(int _=0; _<size(v); _++) cout<<v[_]<<" "; cout<<"\n";}
#define printa(a,s) {for (int _=0; _<s; _++) cout<<a[_]<<" "; cout<<"\n";}
#define print2D(a,m,n) {for (int _=0; _<m; _++) {for (int __=0; __<n; __++) cout<<a[_][__]<<" "; cout<<"\n";} cout<<"\n";}
#define debug cout<<"ok at line "<<__LINE__<<endl;
#else
#define nl
#define pr(x)
#define prl(x)
#define prp(x)
#define printv(v)
#define printa(a,s)
#define print2D(a,m,n)
#define debug
#endif

using namespace std;

typedef long long ll;

const int INF = 2147483647;
const long long INFL = 9223372036854775807LL;
const double EPSILON = 0.00000001;
const long long MOD = 1000000007;

int cnt[5];

int main()
{
    freopen("A_large.in","r",stdin);
    freopen("A.out","w",stdout);

    int cases;
    scanf("%d",&cases);
    for (int casen=0; casen<cases; casen++){
        printf("Case #%d: ",casen+1);
        ms(cnt,0);
        read(n); read(p);
        for0(i,n) {
            read(x);
            cnt[x%p]++;
        }

        int bad = 0;
        if (p == 2) {
            bad = cnt[1]/2;
        }
        else if (p == 3){
            int m = min(cnt[1],cnt[2]);
            int M = max(cnt[1],cnt[2]) - m;
            int cur = 0;
            bad += m;
            for0(i,M) {
                if (cur)
                    bad++;
                cur = (cur+1)%3;
            }
        }
        else if (p == 4) {
            int m = min(cnt[1],cnt[3]);
            bad += m;
            cnt[1] -= m;
            cnt[3] -= m;
            bad += cnt[2]/2;
            cnt[2] %= 2;
            //prl(bad)
            int cur = 0;
            while (cnt[1] > 0 || cnt[2] > 0 || cnt[3] > 0){
                if (cur)
                    bad++;
                //prl(cur)
                //printa(cnt,p)
                if (cur == 2 && cnt[2] > 0){
                    cur = (cur+2)%4;
                    cnt[2]--;
                }
                else if (cnt[1] > 0){
                    cur = (cur+1)%4;
                    cnt[1]--;
                }
                else if (cnt[3] > 0){
                    cur = (cur+3)%4;
                    cnt[3]--;
                }
                else {
                    cur = (cur+2)%4;
                    cnt[2]--;
                }
            }
            //prl(bad)
        }

        printf("%d",n-bad);
        printf("\n");
    }
    return 0;
}
