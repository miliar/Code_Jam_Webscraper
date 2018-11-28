#include <cstdio>
#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
#include <queue>
#include <set>
#include <map>
#include <stack>
using namespace std;

#define For(i,n) for(int i=0; i<(n); i++)
#define mp(a,b) make_pair((a),(b))
typedef long long ll;
typedef pair<int,int> pii;

void solve(int p1) {
    printf("Case #%d: ",p1);
    int n,p;
    scanf("%d %d",&n,&p);
    vector<int> P; P.resize(p,0);
    For(i,n) {
        int x;
        scanf("%d",&x);
        P[x%p]++;
    }
    int res=0;
    res+=P[0]; P[0]=0;
    if(p==2) {
        res+=(P[1]+1)/2;
    }
    else if(p==3) {
        int x=min(P[1],P[2]);
        res+=x;
        P[1]-=x; P[2]-=x;
        if(P[1]!=0) {
            res+=(P[1]+2)/3;
        }
        else if(P[2]!=0) {
            res+=(P[2]+2)/3;
        }
    }
    else {
        res+=P[2]/2; P[2]%=2;
        int x=min(P[1],P[3]);
        res+=x;
        P[1]-=x; P[3]-=x;
        if(P[1]!=0) {
            if(P[2]!=0 && P[1]>=2) {
                res++;
                P[1]-=2;
            }
            res+=(P[1]+3)/4;
        }
        else if(P[3]!=0) {
            if(P[2]!=0 && P[3]>=2) {
                res++;
                P[3]-=2;
            }
            res+=(P[3]+3)/4;
        }
        else {
            if(P[2]!=0) res++;
        }
    }
    printf("%d\n",res);
}

int main() {
    int t1;
    scanf("%d",&t1);
    For(i,t1) solve(i+1);
}
