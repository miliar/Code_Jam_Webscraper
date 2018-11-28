#include <bits/stdc++.h>
#define f first
#define s second

using namespace std;

long long sq[70];

int main()
{
    freopen("Cl.out","w",stdout);
    int T,t;
    long long N,K;
    scanf("%d",&T);
    long long x,ox=0;
    vector<pair<long long,int> > V;
    vector<pair<long long,int> >::iterator it;
    int i;
    long long BOUND = 1e+18;
    for(i=0,x=1LL;x <= BOUND;++i,x*=2)
    {
        V.push_back({x+ox,i});
        ox+=x;
        sq[i]=x;
//        printf("%lld\n",x+ox);
    }
    bool c;
    for(t=1;t<=T;++t)
    {
        scanf("%lld %lld",&N,&K);
        printf("Case #%d: ",t);

//        if(K==1)
//        {
//            printf("%lld %lld\n",N/2,(N-1)/2);
//            continue;
//        }

        it = lower_bound(V.begin(),V.end(),make_pair(K,0));
//        printf("%lld ",(N/sq[it->s]-1)/2);
        c = (N-sq[it->s]+1)%sq[it->s] >= K-sq[it->s]+1;
        printf("%lld ",((N-sq[it->s]+1)/sq[it->s]+c)/2);
        printf("%lld\n",((N-sq[it->s]+1)/sq[it->s]+c-1)/2);
//        if((N-sq[it->s]+1)%sq[it->s]==0 || (N-sq[it->s]+1)%sq[it->s] >= K-sq[it->s]+1)
//        {
//            printf("%lld\n",(N/sq[it->s]-1)/2);
//        }
//        else
//        {
//            printf("%lld\n",(N/sq[it->s])/2-1);
//        }


    }
    return 0;
}
