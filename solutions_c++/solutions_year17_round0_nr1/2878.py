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
    vector<int> A;
    int n=0;
    while(1) {
        char c;
        scanf("%c",&c);
        if(c!='+' && c!='-') break;
        n++;
        if(c=='+') A.push_back(1);
        else A.push_back(0);
    }
    int k;
    scanf("%d ",&k);
    int res=0;
    For(i,n-k+1) {
        if(A[i]==1) continue;
        For(j,k) A[i+j]=(A[i+j]+1)%2;
        res++;
        }
    bool t=true;
    For(i,n) if(A[i]==0) t=false;
    printf("Case #%d: ",p1);
    if(t) printf("%d\n",res);
    else printf("IMPOSSIBLE\n");
}

int main() {
    int t;
    scanf("%d ",&t);
    For(i,t) solve(i+1);
}
