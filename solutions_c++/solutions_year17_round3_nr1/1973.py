#include <bits/stdc++.h>
#include <math.h>

using namespace std;

int r[1005],h[1005];
double s[1005];
//double dp[1005];
int rk[1005];
int id[1005];
const double PI = 2*acos(0.0);
double ans,kep;

multiset<double>::iterator it;

bool cmp(int x,int y)
{
    return r[x] > r[y];
}

int main()
{
    freopen("Al.out","w",stdout);
    int T,N,K,t,x;
    int i,j,k;

    scanf("%d",&T);
    for(t=1;t<=T;++t)
    {
        multiset<double> Set;
        scanf("%d %d",&N,&K);
        --K;
        for(i=0;i<N;++i)
        {
            id[i] = i;
            scanf("%d %d",&r[i],&h[i]);
            s[i] = 2.0*r[i]*h[i]*PI;
            Set.insert(s[i]);
//            printf(">>> %f\n",s[i]);
        }
        sort(id,id+N,cmp);
        ans = 0;
        for(k=0;k<N;++k)
        {
            i = id[k];
            kep = PI*r[i]*(r[i]+2*h[i]);
//            printf("> %d %d\n",i,Set.size());
            Set.erase(Set.lower_bound(s[i]));
            j=0;
            for(it=Set.end();it!=Set.begin()&&j<K;++j)
            {

                --it;
                kep += *it;
//                cout << kep << '\n';
            }
            if(j==K)
                ans = max(ans,kep);
        }
        printf("Case #%d: ",t);
        printf("%f\n",ans);
//        cout << ans << '\n';
    }
    return 0;
}
