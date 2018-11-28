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


#define SIZE 1010

typedef pair<double,double> pdd;

pdd cake[SIZE];


double dp[SIZE][SIZE];
bool vis[SIZE][SIZE];
int n;

const double inf = 1e30;
const double pi = acos(-1);


double func(int totake,int have) {
    if ( have == 0 )return 0;
    if (totake == n){
        return -inf;
    }

    double &ret = dp[totake][have];
    if ( vis[totake][have] )return ret;

    vis[totake][have] = true;
    ret = max( func(totake+1,have) , 2 * pi * cake[totake].X * cake[totake].Y +func(totake+1,have-1) );

    return ret;
}

int main(){

    freopen("A-large.in","r",stdin);
    freopen("outA.out","w",stdout);

    int kase;
    scanf("%d",&kase);

    for (int kk=1;kase--;++kk) {
        int k;
        scanf("%d %d",&n,&k);

        FO(i,0,n) {
            scanf("%lf %lf",&cake[i].X,&cake[i].Y);
        }

        sort(  cake,cake+n  );
        reverse(  cake,cake+n  );


        CLR(vis);

        double ans = -inf;
        for (int i=0;i<n;++i) {
            ans = max(ans , pi * cake[i].X * cake[i].X + 2 * pi * cake[i].X * cake[i].Y +func(i+1,k-1));
        }

        printf("Case #%d: %.8f\n",kk,ans);
    }

    return 0;
}
