#include<bits/stdc++.h>
using namespace std;
main(){
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small.out","w",stdout);
    int T,cs;
    scanf("%d",&T);
    for(cs=1;cs<=T;cs++){
        int hd,hk,ad,ak,b,d,Min=600;
        scanf("%d %d %d %d %d %d",&hd,&ad,&hk,&ak,&b,&d);
        for(int cb=0;cb<=100;cb++){
            for(int cd=0;cd<=100;cd++){
                int turn=0,nb=0,nd=0,nhd=hd,nhk=hk,nad=ad,nak=ak;
                while(1){
                    turn++;
                    if(turn>=Min){
                        break;
                    }
                    if(nd<cd){
                        if(nhd<=nak-d){
                            nhd=hd;
                            nhd-=nak;
                            if(nhd<=nak){
                                turn=600;
                                break;
                            }
                            continue;
                        }
                        nak-=d;
                        nhd-=nak;
                        nd++;
                        continue;
                    }
                    if(nb<cb){
                        if(nhd<=nak){
                            nhd=hd;
                            nhd-=nak;
                            if(nhd<=nak){
                                turn=600;
                                break;
                            }
                            continue;
                        }
                        nad+=b;
                        nhd-=nak;
                        nb++;
                        continue;
                    }
                    if(nhk<=nad)break;
                    if(nhd<=nak){
                        nhd=hd;
                        nhd-=nak;
                        if(nhd<=nak){
                            turn=600;
                            break;
                        }
                        continue;
                    }
                    nhk-=nad;
                    nhd-=nak;
                }
                Min=min(Min,turn);
            }
        }
        if(Min==600)printf("Case #%d: IMPOSSIBLE\n",cs);
        else printf("Case #%d: %d\n",cs,Min);
    }
}
