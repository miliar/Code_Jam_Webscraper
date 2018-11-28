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

int cnt[1005];
int seat_cnt[1005];
int N,C,M;

int solve(vector< pair<int,int> > & tickets, int rides)
{
    int free = 0;
    int promo = 0;
    int seat = 1;
    for (; seat<=N; seat++) {
        if (seat_cnt[seat] > rides) {
            if (free + rides < seat_cnt[seat])
                return -1;
            else {
                free -= seat_cnt[seat]-rides;
                promo += seat_cnt[seat]-rides;
            }
        }
        else {
            free += rides-seat_cnt[seat];
        }
        //pr(seat) pr(seat_cnt[seat]) pr(free) pr(promo) nl
    }
    return promo;
}

int main()
{
    freopen("B_large.in","r",stdin);
    freopen("B.out","w",stdout);

    int cases;
    scanf("%d",&cases);
    for (int casen=0; casen<cases; casen++){
        printf("Case #%d: ",casen+1);

        scanf("%d %d %d",&N,&C,&M);
        ms(cnt,0);
        ms(seat_cnt,0);
        vector<pair<int,int> > tickets;
        int low = 0;
        for0(i,M) {
            read(seat); read(customer);
            tickets.pb(mp(seat,customer));
            cnt[customer]++;
            seat_cnt[seat]++;
            low = max(low,cnt[customer]);
        }
        sort(all(tickets));
        //prl(low)
        //printa(seat_cnt,N+1)

        int res = solve(tickets, low);
        //prl(res)
        int high = M;
        while (low < high) {
            int mid = (low+high)/2;
            res = solve(tickets, mid);
            //pr(low) pr(high) pr(res) nl
            if (res == -1){
                low = mid+1;
            }
            else {
                high = mid;
            }
        }
        //prl(high) prl(res)
        res = solve(tickets, high);

        printf("%d %d",high,res);
        printf("\n");
    }
    return 0;
}
