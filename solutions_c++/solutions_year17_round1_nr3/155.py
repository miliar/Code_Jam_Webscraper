#include<stdio.h>
#include<math.h>
#include<vector>
#include<algorithm>
#include<map>
#include<unordered_map>
#include<string>
#include<queue>
#define ll long long
#define fi first
#define se second
using namespace std;
int main(void){
    //freopen("test.txt", "r", stdin);
    freopen("C-small-attempt1.in", "r", stdin);
    //freopen("C-large.in","r", stdin);
    //freopen("C.out", "w",stdout);
    int T;
    scanf("%i", &T);
    for(int l=0;l<T;l++){
        int Hd; int Ad; int Hk; int Ak; int B; int D;
        scanf("%i %i %i %i %i %i\n", &Hd, &Ad, &Hk, &Ak, &B, &D);
        if(Ad>=Hk) {printf("Case #%i: 1\n", l+1); continue;}
        if(Hd<=Ak-D) {printf("Case #%i: IMPOSSIBLE\n", l+1); continue;}
        //if(2*Ad>=Hk||Ad+B>=Hk) {printf("Case #%i: 2\n", l+1); continue;}
        //if(2*Ak-3*D>=Hd) {printf("Case #%i: IMPOSSIBLE\n",l+1); continue;}
        int i;
        int j;
        int minires=1000000000;
        int stav=1;
        for(i=0;i<=100;i++){
            for(j=0;j<=100;j++){
                int res=0;
                stav=1;
                int Hdz=Hd; int Adz=Ad; int Hkz=Hk; int Akz=Ak;
                int k;
                for(k=0;k<i;k++){
                    if(Akz-D>=Hdz) {res++; Hdz=Hd-Akz;}
                    if(Akz-D>=Hdz) {stav=0; break;}
                    res++;
                    Akz-=D;
                    if(Akz<0) Akz=0;
                    Hdz-=Akz;
                }
                if(stav==0) continue;
                for(k=0;k<j;k++){
                    if(Akz>=Hdz) {res++; Hdz=Hd-Akz;}
                    if(Akz>=Hdz) {stav=0; break;}
                    res++;
                    Adz+=B; Hdz-=Akz;
                }
                //printf("%i %i   %i\n", i, j, res);
                if(stav==0) continue;
                for(k=0;;k++){
                    if(Adz>=Hkz) {res++; break;}
                    if(Akz>=Hdz) {res++; Hdz=Hd-Akz;}
                    if(Akz>=Hdz) {stav=0; break;}
                    res++;
                    Hkz-=Adz;
                    Hdz-=Akz;
                }
                if(stav==0) continue;
                if(res<minires) minires=res;
            }
        }
        if(minires==1000000000) {printf("Case #%i: IMPOSSIBLE\n", l+1); continue;}
        printf("Case #%i: %i\n", l+1, minires);
    }
    return 0;
}
