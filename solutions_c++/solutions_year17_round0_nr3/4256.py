#include <iostream>
#include <stdio.h>
#include <cstring>
#include <queue>
#include <cmath>
#include <fstream>

using namespace std;
int t;
long long n,k,ansL,ansR;
priority_queue <pair<long long,pair<long long,long long> > > q;
ofstream answer;

void bathroom (long long w){
    for (long long i=0;i<w;i++){
        long long dis=q.top().first;
        long long a=q.top().second.first;
        long long b=q.top().second.second;
        //cout << dis << "  " << a << "  " << b << endl;
        q.pop();
        q.push({dis/2,{a,a+(dis/2)}});
        ansL=(dis/2)-1;
        q.push({b-(a+(dis/2)),{a+(dis/2),b}});
        ansR=b-(a+(dis/2))-1;
    }
}

int main()
{
    answer.open("answer.txt");
    scanf("%d",&t);
    for (int i=0;i<t;i++){
        while (!q.empty()) q.pop();
        ansL=0;ansR=0;
        scanf("%lld%lld",&n,&k);
        q.push({n+1,{0,n+1}});
        bathroom(k);
        answer<<"Case #"<<i+1<<": "<<max(ansL,ansR)<<" "<<min(ansL,ansR) << endl;
    }
    return 0;
}
