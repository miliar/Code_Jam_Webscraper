#include <bits/stdc++.h>

#define pb push_back
#define mp make_pair
#define size(n) ( int( n.size() ) )
#define sqr(n) ( (n) * (n) )


using namespace std;

const int N = 1010;
int a[N];

int main(){
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t, k, i, n, j, cases;
    scanf("%d\n",&cases);
    for ( t = 1; t <= cases; t++ ){
        char ch;
        n = 0;
        while(1){
            ch = getchar();
            if ( ( ch != '+' ) && ( ch != '-' ) ){
                break;
            }
            a[++n] = 1;
            if ( ch == '-' ){
                a[n] = 0;
            }
        }
        scanf("%d\n",&k);
        int ans = 0;
        for ( i = 1; i <= n - k + 1; i++ ){
            if ( !a[i] ){
                ans++;
                for ( j = 1; j <= k; j++ ){
                    a[i+j-1] ^= 1;
                }
            }
        }
        int sum = 0;
        for ( i = 1; i <= n; i++ ){
            sum += a[i];
        }
        printf("Case #%d: ",t);
        if ( sum != n ){
            puts("IMPOSSIBLE");
        }
        else{
            printf("%d\n",ans);
        }
    }
    return 0;
}
