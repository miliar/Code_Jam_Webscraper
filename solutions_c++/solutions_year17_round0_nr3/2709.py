#include <iostream>
#include<queue>
#include<stdio.h>
#include<map>
using namespace std;
priority_queue <pair<long long,long long> > pq;
pair<long long, long long> per;
map <pair<long long, long long>, long long> nr;

long long n, k, lg, t, jum, minim, maxim, rmax, rmin, frecv, sum;

pair<long long, long long> transformare(long long lg){
    jum=lg/2;
    if (lg&1)
        return make_pair(jum,jum);
    else
        return make_pair(jum-1,jum);
}

void adauga(pair<long long, long long> pereche, long long numar){
    if (nr.find(pereche)==nr.end()){
        pq.push(pereche);
        nr[pereche]=numar;
    }else{
        nr[pereche]+=numar;
    }
}

int main()
{
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    scanf("%d",&t);
    for (int ii=1;ii<=t;ii++){
        scanf("%lld %lld",&n,&k);
        nr.clear(); 
        while(pq.size())
            pq.pop();
        adauga(transformare(n),1);
        sum=0;
        while (sum<k){
            per=pq.top();   pq.pop();
            minim=per.first;
            maxim=per.second;
            frecv=nr[per];
            sum+=frecv;
            adauga(transformare(minim),frecv);
            adauga(transformare(maxim),frecv);
            rmax=maxim; rmin=minim;
        }
        printf("Case #%d: %lld %lld\n",ii,rmax,rmin);
    }
    return 0;
}


