#include <iostream>
#include <cstdio>

using namespace std;

int T;
long long N, K;
long long V, S;

int main()
{
    scanf("%d",&T);
    for (int Case=1; Case<=T; Case++)
    {
        scanf("\n%lld %lld",&N,&K);
        K--;
        V=N;
        S=K;
        while (S>0)
        {
            if (S%2==0)
            {
                S-=1;
                V-=1;
            }
            S/=2;
            V/=2;
        }
        printf("Case #%d: %lld %lld\n",Case,V/2,(V-1)/2);
    }

    return 0;
}
