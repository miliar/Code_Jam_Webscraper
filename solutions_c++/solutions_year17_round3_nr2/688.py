#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <iostream>

#define MAXN 205
using namespace std;

struct Node
{
    int s, t;
    bool isC;

    bool operator<(const Node& rhs)const{
        return s<rhs.s;
    }
};

Node a[MAXN];
int ac, aj;
int timeCJ[MAXN];
int timeC[MAXN];
int timeJ[MAXN];

void solve()
{
    scanf("%d%d", &ac, &aj);

    int tC=0;
    for(int i=0;i<ac;i++){
        scanf("%d%d", &a[i].s, &a[i].t);
        a[i].isC=true;
        tC+=a[i].t-a[i].s;
    }

    int tJ=0;
    for(int i=ac;i<ac+aj;i++){
        scanf("%d%d", &a[i].s, &a[i].t);
        a[i].isC=false;
        tJ+=a[i].t-a[i].s;
    }

    sort(a, a+ac+aj);
    int nCJ=0, nC=0, nJ=0;
    for(int i=1;i<ac+aj;i++){
        if(a[i-1].isC&&a[i].isC){
            timeC[nC++]=a[i].s-a[i-1].t;
        }
        else if(!a[i-1].isC&&!a[i].isC){
            timeJ[nJ++]=a[i].s-a[i-1].t;
        }
        else{
            timeCJ[nCJ++]=a[i].s-a[i-1].t;
        }
    }
    if(a[ac+aj-1].isC&&a[0].isC){
        timeC[nC++]=a[0].s-a[ac+aj-1].t+1440;
    }
    else if(!a[ac+aj-1].isC&&!a[0].isC){
        timeJ[nJ++]=a[0].s-a[ac+aj-1].t+1440;
    }
    else{
        timeCJ[nCJ++]=a[0].s-a[ac+aj-1].t+1440;
    }

    int sumC=0, sumJ=0;
    for(int i=0;i<nC;i++) sumC+=timeC[i];
    for(int i=0;i<nJ;i++) sumJ+=timeJ[i];
    for(int i=0;i<nCJ;i++){
        sumC+=timeCJ[i];
        sumJ+=timeCJ[i];
    }

    if(sumC+tC>=720&&sumJ+tJ>=720){
        printf("%d\n", nCJ);
    }
    else if(sumC+tC<720){
        int temp=sumC+tC;
        sort(timeJ, timeJ+nJ);
        for(int i=nJ-1;i>=0&&temp<720;i--){
            temp+=timeJ[i];
            nCJ+=2;
        }
        printf("%d\n", nCJ);
    }
    else if(sumJ+tJ<720){
        int temp=sumJ+tJ;
        sort(timeC, timeC+nC);
        for(int i=nC-1;i>=0&&temp<720;i--){
            temp+=timeC[i];
            nCJ+=2;
        }
        printf("%d\n", nCJ);
    }
}

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int t;  cin >> t;
    for(int i=1;i<=t;i++){
        printf("Case #%d: ", i);
        solve();
    }
    return 0;
}
