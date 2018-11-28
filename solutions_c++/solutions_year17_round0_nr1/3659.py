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
const int N = 100005;

char s[10005];
bool v[10005];

int main()
{
    int n, k, i, j, T, cas = 1;
    freopen("A-large (1).in", "r", stdin);
    freopen("out.txt", "w", stdout);
    scanf("%d", &T);
    while( T -- ){
        printf("Case #%d: ", cas++);
        scanf("%s%d", s, &k);
        n = strlen(s);
        memset( v, 0, sizeof(v) );
        for( i = 0; i < n; i ++ ){
            if( s[i] == '+' ) v[i] = 1;
        }
        int cnt = 0;
        for( i = 0; i <= n-k; i ++ ){
            if( !v[i] ){
                for( j = i; j < i+k; j ++ ) v[j] ^= 1;
                cnt ++;
            }
        }
        int fl = 0;
        for( ; i < n; i ++ ){
            if( !v[i] ){
                fl = 1;
                break;
            }
        }
        if( fl ) puts("IMPOSSIBLE");
        else printf("%d\n", cnt);
    }
}
