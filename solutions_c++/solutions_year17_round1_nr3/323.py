#include <bits/stdc++.h>
#define ll long long
using namespace std;
ll simulate(ll health,ll hd,ll ad,ll hk,ll ak) {
    if(hd-2*ak <= 0 && hk-ad > 0) {
        return -1;
    }
    ll ans = 0;
    while(true) {
        //printf("%lld %lld\n",health,hk);
        ans++;
        if(hk-ad <= 0) {
            hk -= ad;
        }
        else if(health-ak <= 0) {
            health = hd;
        }
        else hk -= ad;

        if(hk > 0) health -= ak;
        else break;
    }
    //printf("Sim %lld %lld %lld %lld = %lld\n",hd,ad,hk,ak,ans);
    return ans;
}
void solve() {
    ll hd,ad,hk,ak,B,D;
    scanf("%lld %lld %lld %lld %lld %lld",&hd,&ad,&hk,&ak,&B,&D);
    // brute force D , B
    if(B == 0 && D == 0) {
        // simulate
        ll ans = simulate(hd,hd,ad,hk,ak);
        if(ans == -1) printf("IMPOSSIBLE\n");
        else printf("%lld\n",ans);
        return;
    }
    else {
        // brute force D B
        ll ans = simulate(hd,hd,ad,hk,ak);
        for(int d = 0;d <= (D==0?0:100);d++) {
            if(ak - D*(d-1) <= 0) break;
            for(int b = 0;b <= (B==0?0:100);b++) {
                if(ad + B*(b-1) >= hk) break;
                //printf("Trying %d %d\n",d,b);
                ll dd = d;
                ll bb = b;
                ll health = hd;
                ll turnUsedD = 0;
                ll newAk = ak;
                ll newAd = ad;
                while(dd > 0) {
                    turnUsedD++;
                    if(health-(newAk-D) <= 0) {
                        health = hd;
                        // if cure then hit then cure again then not working
                        if(health - newAk - (newAk-D) <= 0) {
                            break;
                        }
                    }
                    else { // debuff
                        newAk -= D;
                        dd--;
                    }
                    health -= newAk;
                }
                ll turnUsedB = 0;
                while(bb > 0) {
                    //printf("%lld\n%lld",turnUsedB,bb);
                    turnUsedB++;

                    if(health-newAk <= 0) {
                        health = hd;
                        if(health - 2*newAk <= 0) break;
                    }
                    else { // buff
                        newAd += B;
                        bb--;
                    }
                    health -= newAk;
                }
                ll tans = simulate(health,hd,newAd,hk,newAk);
                //printf("Trying %d %d = %lld\n",b,d,tans+turnUsedD,turnUsedB);
                if(tans != -1) ans = min(ans==-1?999999999:ans,tans+turnUsedD+turnUsedB);
            }
        }
        if(ans == -1) printf("IMPOSSIBLE\n");
        else printf("%lld\n",ans);
    }

}
int main() {
    int t;
    scanf("%d",&t);
    for(int i = 0;i < t;i++) {
        printf("Case #%d: ",i+1);
        solve();
    }
}
