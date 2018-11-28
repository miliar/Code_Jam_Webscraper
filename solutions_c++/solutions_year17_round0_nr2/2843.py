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
    ll n;
    scanf("%lld",&n);
    vector<int> A;
    ll a=n;
    while(a>0) {
        A.push_back(a%10);
        a/=10;
    }
    reverse(A.begin(),A.end());
    int p=0;
    while(p!=A.size() && (p==0 || A[p]>=A[p-1])) p++;
    if(p==A.size()) {
        printf("%lld\n",n);
        return;
    }
    p--;
    while(p!=0 && A[p]==A[p-1]) p--;
    A[p]--;
    for(int i=p+1; i<A.size(); i++) A[i]=9;
    ll res=0;
    For(i,A.size()) {
        res*=10ll;
        res+=A[i];
    }
    printf("%lld\n",res);
}

int main() {
    int t;
    scanf("%d ",&t);
    For(i,t) solve(i+1);
}
