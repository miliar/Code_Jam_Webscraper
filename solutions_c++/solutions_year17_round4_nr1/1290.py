#include <bits/stdc++.h>
using namespace std;
#define REP(i,n) for(int i=0;i<int(n);++i)
int main(){
    int T;
    scanf("%d",&T);
    REP(cs,T){
        int N, P, ans;
        int c[4] = {0, 0, 0, 0};
        scanf("%d%d",&N,&P);
        REP(i,N){
            int x;
            scanf("%d",&x);
            c[x%P]++;
        }
        if (P==2) {
            ans=c[0]+(c[1]+1)/2;
        } else if (P==3) {
            int a=min(c[1],c[2]), b=max(c[1],c[2]);
            ans=c[0]+a+(b-a+2)/3;
        } else {
            ans=c[0];
            int c13 = min(c[1],c[3]);
            ans+=c13;
            c[1]-=c13;
            c[3]-=c13;
            ans+=c[2]/2;
            c[2]%=2;
            int cc=max(c[1],c[3]), c2=c[2];
            if(c2==1 && cc>=2){
                ans+=1;
                c2--;
                cc-=2;
            }
            if(c2==1){
                ans++;
            } else {
                ans+=(cc+3)/4;
            }
        }
        printf("Case #%d: %d\n", cs+1, ans);
    }
}
