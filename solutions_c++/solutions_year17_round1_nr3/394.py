#include <iostream>
#include <string.h>
#include <stdio.h>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
using namespace std;
#define maxn 100010
#define inf 2100000000
int hd,ad,hk,ak,b,d;
int debuff(int left,int hel,int atk) {
    if(left == 0){
        return 0;
    }
    int natk = max(atk-d,0);
    if(hel<=natk) {
        return -1;
    }
    int tmp = debuff(left-1,hel - natk, natk);
    if(tmp==-1){
        tmp = debuff(left,hd - atk,atk);
        if(tmp==-1)
        return -1;
        return tmp+1;
    }
    return tmp + 1;
}

int buff(int left,int hel){
    if(left == 0){
        return 0;
    }
    if(hel<=ak) {
        return -1;
    }
    int tmp = buff(left-1,hel - ak);
    if(tmp==-1){
        tmp = buff(left,hd - ak);
        if(tmp==-1)
        return -1;
        return tmp+1;
    }
    return tmp + 1;
}

int attack(int hel1,int atk1,int hel2,int atk2){
    if(hel2<=atk1)
        return 1;
    if(hel1<=atk2)
        return -1;
    int tmp = attack(hel1 - atk2,atk1,hel2-atk1,atk2);
    if(tmp<0){
        tmp  = attack(hd - atk2,atk1,hel2,atk2);
        if(tmp<0)
            return -1;
        return tmp+1;
    }
    return tmp+1;
}

int solve(int db,int bu){ //
    int ret = 0;
    int hel = hd,atk = ak;
    if(hd<=ak){
        return -1;
    }
    int tmp = debuff(db,hel,atk);
    if(tmp < 0)
        return -1;
    ret += tmp;
    tmp = buff(bu,hd);
    if(tmp < 0)
        return -1;
    ret += tmp;
    tmp = attack(hd,ad+bu*b,hk,max(0,ak-d*db));
    if(tmp<0)
        return -1;
    ret +=tmp;
    return ret;
}
int main()
{
    freopen("dd.txt","r",stdin);
    //freopen("out.txt","w+",stdout);
    int ncase,T=0;
    cin>>ncase;
    while(ncase--){
        printf("Case #%d:\n",++T);
        scanf("%d%d%d%d%d%d",&hd,&ad,&hk,&ak,&b,&d);
        int deb = 0,buf = 100;
        if(d!=0){
            deb = (ak+d-1)/d;
        }
        int ans = inf;
        if(b==0)
            buf = 0;
        for(int i=0;i<=buf;i++){
            for(int j=0;j<deb;j++){
                int tmp = solve(j,i);
                if(tmp>=0){
                    ans = min(ans,tmp);
                }
            }
        }
        if(ans==inf){
            printf("IMPOSSIBLE\n");
            continue;
        }
        printf("%d\n",ans);
    }
    return 0;
}
