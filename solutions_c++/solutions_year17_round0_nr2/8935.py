#include <stdio.h>
#include <vector>
#include <algorithm>
using namespace std;

void my(long long int N)
{
    if ( N == 0) return;
    int a[50];
    int n=0;
    long long int NN = N;
    long long int ans = 0;
    while (NN > 0)
    {
        a[n++] = NN%10;
        NN = NN/10;
    }

    int prev = -1;
    int i;

    for (i=n-1;i>=0;i--)
    {
        if ( a[i] < prev ) break;
        prev = a[i];
    }
    if ( i < 0 ) { printf("%lld",N);return;}
    
    long long int next = 0;
    for (int j=n-1;j>i;j--) next = 10*next + a[j];
    my(next-1);
    for (int j=i;j>=0;j--) printf("9"); return;

}

void solve()
{
    long long  int N;
    scanf("%lld",&N);
    my(N);
    printf("\n");
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
