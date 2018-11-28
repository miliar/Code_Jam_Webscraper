#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

ll N,K;
ll pow2[205];
stack <bool> trav_order;

void initialize(){
    pow2[0] = 1;
    for (int i=1;i<=100;i++)
        pow2[i] = pow2[i-1] * 2;
}

int findLvl(ll idx){
    int lvl=0;
    for (ll i=1;i<=idx;i*=2)
        lvl++;
    return lvl-1;
}

void testFindLvl(){
    printf ("TestFindLvl : ");
    while (1){
            ll k;
        scanf ("%lld",&k);
        if (k==-1) break;
        printf ("-> %d\n",findLvl(k));
    }
}

void backTree(ll lvl,ll idx){
    if (idx==1){
        return;
    }
    ll modres = idx%pow2[lvl-1];
    ll par = pow2[lvl-1] + modres;//LVL HEAD + SHIFT + HALF SHIFT
    bool branch = (idx - pow2[lvl]) >= pow2[lvl-1];
    trav_order.push(branch);
    //printf ("node : %lld | par : %lld | Branch : %d\n",idx,par,branch);
    backTree(lvl-1,par);
}
/*
void trav(int lvl, ll idx, ll R,ll L){
    if (lvl == K){

        return ;
    }
    ll newIdx,newR,newL;
    return;
    trav(lvl+1,newIdx,newR,newL);
}
*/

//void trav(ll L,ll R){//trav(1,N)
//    ll range=R-L+1,mid=(L+R)/2,rangeL,rangeR;
//    rangeL = mid - L;
//    rangeR = R - mid;
//    while (!trav_order.empty()){
//        bool walk = trav_order.top();
//        range = R-L+1;
//
//        trav_order.pop();
//
//        ll newL,newR,newCur,newRange;
//        if (walk){
//            newR = R;
//            newL = mid+1;
//        }else{
//            newR = mid-1;
//            newL = L;
//        }
//        mid = (L+R)/2;
//        rangeL = mid - L;
//        rangeR = R - mid;
//        printf ("-> %d %lld %lld %lld\n",walk,mid,L,R);
//        L = newL;
//        R = newR;
//    }
//
//    printf ("%lld %lld\n",rangeR,rangeL);
//
//}

void trav(ll range){
    ll newRangeL,newRangeR,R,L;
    while (!trav_order.empty()){
        bool walk = trav_order.top();
        ll newRange;
        trav_order.pop();
        if (range%2){
            newRangeL = newRangeR = range/2;
        }else{
            newRangeR = range/2;
            newRangeL = range/2-1;
        }
        if (walk){
            newRange = newRangeL;
        }else{
            newRange = newRangeR;
        }
        //printf ("-> %d\n",walk);
        range = newRange;
        //printf ("-> %lld %lld %lld\n",range,newRangeL,newRangeR);
    }

    R = range/2;
    L = range/2 - ((range%2)==0);
   //L = max(L,0ll);
    printf ("%lld %lld\n",R,L);
}

void solve(){
    initialize();
    //testFindLvl();
    scanf ("%lld %lld",&N,&K);
    //trav(0,K,N/2,N/2 - (N%2==0));
    backTree(findLvl(K), K);
    //trav(1,N);
    trav(N);
}

int main(){
    freopen ("C-large.in","r",stdin);
    freopen ("sabu-large.sol","w",stdout);
    int TC;

    scanf ("%d",&TC);
    for (int tc=1;tc<=TC;tc++){
        printf ("Case #%d: ",tc);
        solve();
    }

return 0;
}
