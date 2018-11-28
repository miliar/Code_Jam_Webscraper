#include <stdio.h>
#include <vector>
#include <algorithm>
using namespace std;

void solve()
{
    int a[2000];
    char c;
    int n=0;
    int K;
    while ( (c=getchar()) != ' ') 
        if ( c == '+' ) a[n++] = 1; 
        else a[n++] = 0;
    scanf("%d\n",&K);

    int ans =0;
    for (int i=0;i<n;i++)
        if ( !a[i] )
        {
            ans++;
            if ( i+K-1 >= n ) { printf("IMPOSSIBLE\n"); return ;}
            for (int j=i;j<=i+K-1;j++) a[j] = 1-a[j];
        }
        
    printf("%d\n",ans);

}


int main()
{
    int T;
    scanf("%d\n",&T);
    for (int t=1;t<=T;t++)
    {
        printf("Case #%d: ",t);
        solve();
    }
    return 0;
}
