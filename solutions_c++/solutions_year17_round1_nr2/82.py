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
    vector<int> A; A.resize(n);
    For(i,n) scanf("%d",&A[i]);
    vector<vector<pii> > B;
    B.resize(n);
    For(i,n) {
        For(j,p) {
            int x;
            scanf("%d",&x);
            int l=(10*x+10)/11,h=(10*x)/9;
            int lo=(l+A[i]-1)/A[i],hi=h/A[i];
            if(lo > hi) continue;
            B[i].push_back(mp(lo,hi));
        }
        sort(B[i].begin(),B[i].end());
    }
    int res=0;
    vector<int> P; P.resize(n,0);
    For(i,B[0].size()) {
        bool t=true;
        for(int j=1; j<n; j++) {
            while(P[j]!=B[j].size() && B[j][P[j]].second < B[0][i].first) P[j]++;
            if(P[j]==B[j].size() || B[j][P[j]].first > B[0][i].second) t=false;
        }
        if(t) {
            res++;
            For(j,n) P[j]++;
        }
    }
    printf("%d\n",res);
}

int main() {
    int t1;
    scanf("%d",&t1);
    For(i,t1) solve(i+1);
}
