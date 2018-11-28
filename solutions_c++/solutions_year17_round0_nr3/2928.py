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
    ll n,k;
    scanf(" %lld %lld",&n,&k);
    map<ll,ll> M;
    M[n]=1;
    while(1) {
        map<ll,ll>::iterator it=M.end();
        it--;
        ll vel=it->first,pocet=it->second;
        M.erase(it);
        ll maxi=vel/2,mini=(vel-1)/2;
        if(pocet>=k) {
            printf("%lld %lld\n",maxi,mini);
            return;
        }
        k-=pocet;
        if(M.find(maxi)==M.end()) M[maxi]=0;
        if(M.find(mini)==M.end()) M[mini]=0;
        M[maxi]+=pocet;
        M[mini]+=pocet;
    }
}

int main() {
    int t;
    scanf("%d ",&t);
    For(i,t) solve(i+1);
}
