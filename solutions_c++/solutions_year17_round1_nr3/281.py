#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<int,int> ii;

#define X first
#define Y second


const int alp=26;
const int N=60;
const int inf=600;

int hd,ad,hk,ak,buf,debuf;


void prepare(){
    cin>>hd>>ad>>hk>>ak>>buf>>debuf;
}
int stimulate(int deuse,int bufuse){
    int chd=hd,cad=ad,chk=hk,cak=ak;
    int turn=0;
    while (turn<=inf){
        turn++;
        if (deuse){
            if (cak-debuf<chd){
                deuse--;
                cak=max(0,cak-debuf);
            }else chd=hd;
        }else if (bufuse){
            if (cak<chd) {
                bufuse--;
                cad+=buf;
            }else chd=hd;
        }else {
            chk-=cad;
            if (chk>0&&chd<=cak) chk+=cad,chd=hd;
        }
        if (chk<=0) return turn;
        chd-=cak;
        if (chd<=0) return inf;
    }
    return turn;
}
void solve(){
    int ans=inf;
    for(int deuse=0;deuse<=100;deuse++){
        if (deuse&&debuf==0) break;
        for(int bufuse=0;bufuse<=100;bufuse++) {
            if (bufuse&&buf==0) break;
//            cout<<deuse<<" "<<bufuse<<" "<<ans<<'\n';
            ans=min(ans,stimulate(deuse,bufuse));
        }
    }
    if (ans<inf) cout<<ans<<'\n';
    else cout<<"IMPOSSIBLE\n";
}
int main(){
    freopen("input.in","r",stdin);
    freopen("output.out","w",stdout);
    int test;
    cin>>test;
    for(int te=1;te<=test;te++){
        prepare();
        cout<<"Case #"<<te<<": ";
        solve();
    }
}
