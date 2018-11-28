#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
#include <bits/stdc++.h>

using namespace std;
using namespace __gnu_pbds;

typedef long long LL;

typedef tree<
    int,
    null_type,
    less<int>,
    rb_tree_tag,
    tree_order_statistics_node_update>
ordered_set;
//find_by_order
//order_of_key

#define FO(i,a,b) for (int i = (a); i < (b); i++)

#define PB push_back
#define FRO freopen("in.txt","r",stdin);

#define CLR(arr) memset( (arr),0,sizeof(arr) );
#define NEG(arr) memset( (arr),-1,sizeof(arr) );
#define ALL(v) v.begin(),v.end()

#define X first
#define Y second
#define MP make_pair

typedef pair<int,int> pint;
typedef map<int,int> mint;

void show() {cout<<'\n';}
template<typename T,typename... Args>
void show(T a, Args... args) { cout<<a<<" "; show(args...); }
template<typename T>
void show_c(T& a) { for ( auto &x:a ){ cout<<x<<" ";}cout<<endl;  }



int dp[1500][2][750][2];

bool mom[1500];
bool dad[1500];


int dayend = 24 * 60;

const int inf = (1<<29);

int func(int timer,int per,int momshare, int st) {
    if ( timer == dayend ){
        if ( momshare != 720 )return inf;
        if ( per == st )return 0;
        else return 1;
    }
    if ( momshare > 720 )return inf;

    int &ret = dp[timer][per][momshare][st];
    if ( ret != -1 )return ret;

    if ( per == 0 )momshare++;

    ret = inf;
    if ( !mom[timer+1] ){
        ret = min( ret, (per!=0) + func(timer+1,0,momshare,st) );
    }
    if ( !dad[timer+1] ){
        ret = min( ret, (per!=1) + func(timer+1,1,momshare,st) );
    }

    return ret;
}


int main(){

    freopen("B-large.in","r",stdin);
    freopen("outB.out","w",stdout);

    int kase;
    scanf("%d",&kase);

    for (int kk=1;kase--;++kk) {

        int n,m;
        scanf("%d %d",&n,&m);

        CLR(mom);
        CLR(dad);

        int a,b;
        while (n--) {
            scanf("%d %d",&a,&b);
            while ( a<b ){
                mom[a] = true;
                a++;
            }
        }
        while (m--) {
            scanf("%d %d",&a,&b);
            while ( a<b ){
                dad[a] = true;
                a++;
            }
        }
        mom[24*60] = mom[0];
        dad[24*60] = dad[0];

        NEG(dp);

        int ans = min( func(0,0,0,0) , func(0,1,0,1) );
        printf("Case #%d: %d\n",kk,ans);

    }


    return 0;
}
