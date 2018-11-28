#include <bits/stdc++.h>

using namespace std;

void solve() {
    int hd,ad,hk,ak,b,d; cin>>hd>>ad>>hk>>ak>>b>>d;
    int lastCure = 0;
    int tt = 0;
    int ohd = hd,oad = ad,ohk = hk,oak = ak;
    int k = (hk + ad - 1) / ad;
    for(int i = 1;i <= 1000;i++) {
        k = min(k,i +  (hk + ad  + b * i - 1) / (ad + b * i) );
    }
    int ans = 100000;
    for(int x = 0;x <= 1000;x++) {
        int kk = k;
        int xx = x;
        hd = ohd,ad = oad,hk = ohk,ak = oak;
        int flag = 0;
        int cc = 0;
        int changed = 0;
        int lastCure = -1;
        while((kk || xx)) {
            changed = 0;
            cc++;
            if(xx) {
                if(ak  - d <  hd) {
                    ak-=d;
                    xx--;
                }
                else {
                    if(lastCure == cc - 1) {
                        flag = 1;
                        break;
                    }
                    lastCure = cc;
                    hd = ohd;
                }
            }
            else if(kk) {
                if(kk == 1) {
                    kk--;
                    break;
                }
                if(ak >= hd) {
                    if(lastCure == cc - 1) {
                        flag = 1;
                        break;
                    }
                    lastCure = cc;
                    hd = ohd;
                }
                else {
                    kk--;
                }
            }
            hd -= ak;
            if(hd <= 0)  {
                flag = 1;
                break;
            }
        }
        if(flag) continue;
        ans = min(ans,cc);

    }
    if(ans == 100000) cout<<"IMPOSSIBLE"<<endl;
    else cout<<ans<<endl;
}

int main() {
    assert(freopen("input.txt","r",stdin));
    assert(freopen("output.txt","w",stdout));
    int t; cin>>t;
    for(int i = 1;i <= t;i++) {
        cerr<<"Executing Case #"<<i<<endl;
        cout<<"Case #"<<i<<": ";
        solve();
    }

}
