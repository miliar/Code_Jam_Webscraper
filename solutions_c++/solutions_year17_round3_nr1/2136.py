#include<bits/stdc++.h>
#define pb push_back
#define mpp make_pair
#define PI acos(-1)
/*************NOTES*********************\

***************************************/
using namespace std;
typedef long long ll;
typedef unsigned long long ull;
typedef pair < int , int > pii;
const ll inf = 1e9;
const ll mod = 1e9 + 7;
const double eps = 1e-8;
const ll MAX = 1e7 + 20;

template< class T > T gcd(T a, T b) { return (b != 0 ? gcd<T>(b, a%b) : a); }
template< class T > T lcm(T a, T b) { return (a / gcd<T>(a, b) * b); }

/*----------------------Graph Moves----------------*/
//const int fx[]={+1,-1,+0,+0};
//const int fy[]={+0,+0,+1,-1};
//const int fx[]={+0,+0,+1,-1,-1,+1,-1,+1};   // Kings Move
//const int fy[]={-1,+1,+0,+0,+1,+1,-1,-1};  // Kings Move
//const int fx[]={-2, -2, -1, -1,  1,  1,  2,  2};  // Knights Move
//const int fy[]={-1,  1, -2,  2, -2,  2, -1,  1}; // Knights Move
/*------------------------------------------------*/

inline const int EQ( double tmp ){ if( fabs( tmp ) < eps ) return 0; return tmp > eps ? 1 : -1;}
ll  BM(ll  B,ll  P,ll  M){ ll  R=1; while(P>0)  { if(P&1){ R=(R*B)%M;}P/=2;B=(B*B)%M;}return (ll )R;}
ll  MI(ll  x, ll m ){ return BM(x,m-2,m); }

struct node{
    double x, y, up, side ;
}arr[1005];
int n , k;
bool cmp( node a, node b ){
    if( a.x == b.x ) return a.y > b.y;
    return a.x > b.x;
}
double dp[1005][1005];
bool vis[1005][1005];
double hope( int pos, int taken, int last ){
    if( taken == k ){
        return arr[last].up;
    }
    if( pos == n ){
        if( taken == 0 ) return 0;
        return -inf;
    }

    //if( vis[pos][taken] )return dp[pos][taken];
    vis[pos][taken] = true;

    double ck1 = 0.0, ck2 = 0.0;
    dp[pos][taken] = 0;
    if( last != -1 ){
        if( taken == k - 1 ){
            ck1 = fabs(arr[last].up - arr[pos].up )  + arr[pos].side + arr[pos].up ;
        }
        else ck1 = fabs(arr[last].up - arr[pos].up )  + arr[pos].side + hope( pos + 1 , taken + 1, pos );
        ck2 = hope( pos + 1, taken , last );
    }else if( last == -1 ){
        if( taken == k - 1 ){
            ck1 = arr[pos].side + arr[pos].up ;
        }
        else ck1 = arr[pos].side + hope( pos + 1, taken + 1 , pos );
        ck2 = hope( pos + 1 , taken , -1 );
    }
    return dp[pos][taken] =  max( ck1, ck2 );
}

int main ( ){
     #ifdef swapnil
    freopen("in.txt","r",stdin );
    freopen("out.txt","w",stdout );
    #endif // swapnil

    int t;
    cin >> t;
    for( int ks = 1; ks <= t; ks++ ){
        cin >> n >> k;
        for( int i = 0; i < n; i++ ){
            double x, y;
            cin >> x >> y;
            arr[i].x = x; arr[i].y = y;
            arr[i].up = PI * x * x ;
            arr[i].side = 2 * PI * x * y;
        }
        sort( arr, arr + n, cmp );
//        for( int i = 0; i < n; i++ ){
//            cout << arr[i].x << " " << arr[i].y << "\n";
//        }

        memset( vis, false, sizeof( vis ) );
        memset( dp, 0 , sizeof( dp ) );
        double ans = hope( 0, 0, -1 );
        printf("Case #%d: %.9f\n", ks, ans );
        //cerr << "Case " << ks << ": solved\n";
    }




    return 0;
}

