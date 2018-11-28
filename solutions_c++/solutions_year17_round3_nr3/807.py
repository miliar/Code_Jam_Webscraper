#include <stdio.h>
#include "stdlib.h"
#include "set"
#include "vector"

using namespace std;

int main() {
    freopen("C-small-1-attempt0.in.txt", "r", stdin);
    freopen("C-small-1-attempt0.out.txt", "w", stdout);
    
    long t;
    scanf("%ld",&t);
    for (long tt=1;tt<=t;tt++){
        long n,k,u;
        double uu,tmp;
        multiset<long> a;
        a.clear();
        scanf("%ld%ld",&n,&k);
        scanf("%lf",&uu);
        u=uu*10000+0.5;
        for (int i=0;i<n;i++){
            scanf("%lf",&tmp);
            long ttmp=tmp*10000+0.5;
            a.insert(ttmp);
        }
        for (long i=0;i<u;i++){
            long tmp=*a.begin();
            a.erase(a.begin());
            a.insert(tmp+1);
        }
        double ans=1.0;
        for (auto i=a.begin();i!=a.end();i++){
            ans*=(double(*i)/10000.0);
        }
        printf("Case #%ld: %lf\n",tt,ans);
    }
    return 0;
}
