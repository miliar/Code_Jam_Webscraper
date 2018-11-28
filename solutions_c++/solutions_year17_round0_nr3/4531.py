#include <bits/stdc++.h>

#define pb push_back
#define mp make_pair
#define mt make_tuple
#define ll long long
#define pii pair<int,int>
#define tii tuple <int,int,int>
#define N 100005
#define mod 2000003
#define X first
#define Y second
#define eps 0.0000000001
#define all(x) x.begin(),x.end()
#define tot(x) x+1,x+n+1
using namespace std;
char s[25];

int T,t,n,k,m,dist,l,r;
int main() {
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    scanf("%d",&T);

    for(int t=1; t<=T; t++) {
        scanf("%d%d",&n,&k);
        printf("Case #%d: ",t);
       priority_queue<tii>q;
        q.push(mt(n,1,n));
    k--;
        while(k) {
            tie(dist,l,r)=q.top();
            q.pop();
            m=(l+r)/2;
            q.push(mt(m-l,l,m-1));
            q.push(mt(r-m,m+1,r));
            k--;
        }

        tie(dist,l,r)=q.top();
        printf("%d %d\n",dist/2,(dist-1)/2);
    }

    return 0;
}
