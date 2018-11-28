#include <bits/stdc++.h>
#define ll long long
using namespace std;
ll getMinServe(ll num,ll need) { // bsearch
    ll ans = ceil(double(num)/1.1/need);
    // try lower
    while(10*num <= 9*(ans-1)*need) {
        ans--;
    }
    return ans;
}
ll getMaxServe(ll num,ll need) { // bsearch
    ll ans = floor(double(num)/0.9/need);
    // try higher
    while(10*num >= 11*(ans+1)*need) {
        ans++;
    }
    return ans;
}
bool check(ll have,ll need,ll serve) {
    return true;
    if(round(serve*need*0.9) <= have && have <= round(serve*need*1.1)) return true;
    return false;
}
void solve() {
    int n,p;
    scanf("%d %d",&n,&p);
    ll ing[1010];
    for(int i = 0;i < n;i++) {
        scanf("%d",&ing[i]);
    }
    int arr[n][p];
    priority_queue<ll,vector<ll>,greater<ll> > pq[n];
    for(int i = 0;i < n;i++) {
        for(int j = 0;j < p;j++) {
            int x;
            scanf("%d",&x);
            if(getMinServe(x,ing[i]) > getMaxServe(x,ing[i])) continue; // bad package
            pq[i].push(x);
        }
    }
    int ans = 0;
    while(!pq[0].empty()) {
        // check if other match this serving
        //printf("Trying first %d\n",pq[0].top());
        for(ll serve = getMinServe(pq[0].top(),ing[0]);serve <= getMaxServe(pq[0].top(),ing[0]);serve++) {
            //printf("Trying serve %d\n",serve);
            bool boom = false;
            for(int i = 1;i < n;i++) {
                while(true) {
                    if(pq[i].empty()) {
                        boom = true;
                        break;
                    }
                    else if(getMaxServe(pq[i].top(),ing[i]) < serve) { // not good
                        pq[i].pop();
                        continue;
                    }
                    else if(getMinServe(pq[i].top(),ing[i]) > serve) {
                        boom = true;
                        break;
                    }
                    //printf("Good ing %d with %d (%d-%d)\n",i,pq[i].top(),getMinServe(pq[i].top(),ing[i]),getMaxServe(pq[i].top(),ing[i]));
                    break; // good
                }
                if(boom) break;
            }
            if(!boom) {
                //printf("Served %lld : %lld ",serve,pq[0].top());
                if(!check(pq[0].top(),ing[0],serve)) {
                    printf("BOOM");
                    exit(0);
                }
                //printf("Passed !!\n");
                // all good
                ans++;
                for(int i = 1;i < n;i++) {
                    //printf("%lld ",pq[i].top());
                    if(!check(pq[i].top(),ing[i],serve)) {
                        printf("BOOM");
                        exit(0);
                    }
                    pq[i].pop();
                }
                //printf("\n");
                break;
            }
        }
        pq[0].pop();
    }
    printf("%d\n",ans);
}
int main() {
    int t;
    scanf("%d",&t);
    for(int i = 0;i < t;i++) {
        printf("Case #%d: ",i+1);
        solve();
    }
}
