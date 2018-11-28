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
int num[20];
int ans[20];
int main()
{
    int k, i, j, T, cas = 1;
    ll n;
    freopen("B-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    scanf("%d", &T);
    while( T -- ){
        printf("Case #%d: ", cas++);
        scanf("%lld", &n);
        int cnt = 0;
        while( n ){
            num[cnt++] = n%10;
            n /= 10;
        }
        memset( ans, 0, sizeof(ans) );
        for( i = cnt-1; i >= 0; i -- ){
            if( i == 0 ) ans[i] = num[i];
            else{
                if( num[i] < num[i-1] ) ans[i] = num[i];
                else if( num[i] == num[i-1] ){
                    for( j = i-1; j >= 0; j -- ){
                        if( num[j] != num[i] ) break;
                    }
                    if( j < 0 || num[j] > num[i] ){
                        ans[i] = num[i];
                    }
                    else{
                        ans[i] = num[i]-1;
                        for( j = i-1; j >= 0; j -- ){
                            ans[j] = 9;
                        }
                        break;
                    }
                }
                else{
                    ans[i] = num[i]-1;
                    for( j = i-1; j >= 0; j -- ){
                        ans[j] = 9;
                    }
                    break;
                }
            }
        }
        for( i = 19; i >= 0; i -- ){
            if( ans[i] != 0 ) break;
        }
        for( ; i >= 0; i -- ) printf("%d", ans[i]);
        puts("");
    }
}
