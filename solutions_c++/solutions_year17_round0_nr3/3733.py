#include<iostream>
#include<algorithm>
#include<cctype>
#include<cstdio>
#include<cstring>
#include<string>
#include<map>
#include<vector>
#include<set>
#include<cmath>
#include<queue>
#include<ctime>
#define pii pair<int,int>
#define xx first
#define yy second
#define mp make_pair
typedef long long ll;
using namespace std;
const int N = 1000000;

ll num[N+5];
priority_queue< ll > q;

int main()
{
    int i, j, T, cas = 1;
    ll n, k;
    freopen("C-small-2-attempt0.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    scanf("%d", &T);
    while( T -- ){
        scanf("%lld%lld", &n, &k);
        while( !q.empty() ) q.pop();
        memset( num, 0, sizeof(num) );
        q.push(n);
        ll a1 = -1, a2 = -1;
        while( !q.empty() ){
            ll v = q.top();
            q.pop();
            -- v;
            if( v/2 > N ) q.push(v/2);
            else num[v/2] ++;
            if( v-v/2 > N ) q.push(v-v/2);
            else num[v-v/2] ++;
            k --;
            if( k == 0 ){
                a1 = max( v/2, v-v/2 );
                a2 = min( v/2, v-v/2 );
                break;
            }
        }
        printf("Case #%d: ", cas++);
        if( a1 != -1 ){
            printf("%lld %lld\n", a1, a2);
            continue;
        }
        for( i = N; i >= 1; i -- ){
            if( !num[i] ) continue;
            if( num[i] >= k ){
                a1 = (i-1)/2;
                a2 = (i-1)-(i-1)/2;
                swap( a1, a2 );
                break;
            }
            else{
                num[ (i-1)/2 ] += num[i];
                num[ i-1 - (i-1)/2 ] += num[i];
                k -= num[i];
            }
        }
        printf("%lld %lld\n", a1, a2);
    }
}
