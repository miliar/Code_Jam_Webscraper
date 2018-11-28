#include<bits/stdc++.h>
#define ll long long int
#define vii vector<int>
#define vll vector<ll>
#define pb push_back
#define LIM 10000000
#define MOD 1000000007
#define MAX 10000000
#define pi acos(-1)
#define segVar int lft = node << 1 , rgt = (node << 1) + 1 , md = (st+ed) >> 1;
#define pii pair<int,int>
#define EPS 1e-9

using namespace std;

ll n, k;

int main() {
    freopen("C-small-2-attempt0.in","r",stdin);
    freopen("outcs.txt","w",stdout);

    int T;
    scanf("%d", &T);
    for(int t=1; t<=T; t++) {
        scanf("%lld %lld", &n,&k);

//        priority_queue<ll>pq;
        queue<ll>q1,q2;
        q2.push(n);

        ll mnn,mxx;
        for(int i=1; i<=k; i++) {
            ll nw;
//            cout << "FRONTS " << q1.front() << ' ' << q2.front() << endl;
            if(!q1.empty() && q1.front() >= q2.front()) {
                nw = q1.front();
                q1.pop();
                mxx = nw/2;
                mnn = (nw-1)/2;
                q1.push(mxx);
                q2.push(mnn);
            }
            else {
                nw = q2.front();
                q2.pop();
                mxx = nw/2;
                mnn = (nw-1)/2;
                q1.push(mxx);
                q2.push(mnn);
            }
        }
        printf("Case #%d: %lld %lld\n", t, mxx, mnn);
    }
    return 0;
}
