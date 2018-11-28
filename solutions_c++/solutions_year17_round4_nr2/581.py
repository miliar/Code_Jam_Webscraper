#include <bits/stdc++.h>

using namespace std;

int N, C, M;
int A[1001];
int B[1001];

void _main(int TEST)
{
    scanf("%d%d%d", &N, &C, &M);
    for(int i=1; i<=N; i++)
        B[i]=0;
    for(int i=1; i<=C; i++)
        A[i]=0;
    int lo=1;
    for(int i=0; i<M; i++)
    {
        int p, b;
        scanf("%d%d", &p, &b);
        lo=max(lo, ++A[b]);
        B[p]++;
    }
    int hi=M, mid;
    while(lo<hi)
    {
        mid=(lo+hi)/2;
        int avail=0;
        bool ok=true;
        for(int i=1; i<=N; i++)
        {
            avail+=mid;
            if(avail<B[i])
            {
                ok=false;
                break;
            }
        }
        if(ok)
            hi=mid;
        else
            lo=mid+1;
    }
    int ans=0;
    for(int i=1; i<=N; i++) if(B[i]>lo)
        ans+=B[i]-lo;
    printf("%d %d\n", lo, ans);
}

int main()
{
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("B-small-attempt0.out", "w", stdout);
    int TEST;
    scanf("%d", &TEST);
    for(int i=1; i<=TEST; i++)
    {
        //cerr << i << endl;
        printf("Case #%d: ", i);
        _main(i);
    }
    return 0;
}
