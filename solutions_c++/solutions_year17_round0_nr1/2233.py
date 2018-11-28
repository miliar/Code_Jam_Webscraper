#include <bits/stdc++.h>
using namespace std;
int main()
{
    string s;
    bitset<1001> B;
    int t,k,l,j,n,m,a;
    scanf("%d",&t);
    for(int i=1; i<=t; ++i)
    {
        printf("Case #%d: ",i);
        cin>>s>>k;
        l=s.size();
        for(j=0; j<l; ++j)
        {
            if(s[j]=='-')
            {
                B.set(j);
            }
        }
        a=0;
        l-=k;
        for(j=0; j<=l; ++j)
        {
            if(B.test(j))
            {
                ++a;
                n=j+k;
                for(m=j; m<n; ++m)
                {
                    B.flip(m);
                }
            }
        }
        while(--k)
        {
            if(B.test(j))
            {
                B.set(1000);
                break;
            }
            ++j;
        }
        if(B.test(1000))
        {
            printf("IMPOSSIBLE\n");
        }
        else
        {
            printf("%d\n",a);
        }
        B.reset();
    }
    return 0;
}
