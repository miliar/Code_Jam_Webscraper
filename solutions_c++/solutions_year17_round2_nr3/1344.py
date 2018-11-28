#include <bits/stdc++.h>
using namespace std;
double meh[150];
int horz[150][2];
int adl[150];
// total distance, speed
//destination city, dist
int main(){
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small-attempt0.txt","w",stdout);
    int teesee, n, q, temp, cur;
    double tmep;
    scanf("%d", &teesee);
    for(int asd=0; asd<teesee; asd++){
            memset(meh, 0, sizeof(meh));
        memset(horz, 0, sizeof(horz));
        memset(adl, 0, sizeof(adl));
        scanf("%d%d", &n, &q);
        for(int i=0; i<n; i++){
            scanf("%d%d", &horz[i][0], &horz[i][1]);
        }
        for(int i=0; i<n; i++){
            for(int k=0; k<n; k++){
                scanf("%d", &temp);
                if(temp!=-1){
                    adl[i] = temp;
                }
            }
        }
        for(int i=0; i<n-1; i++){
            cur = horz[i][0];
            tmep = 0;
            for(int k=i+1; k<n; k++){
                cur-=adl[k-1];
                if(cur<0){
                    break;
                }
                tmep += double(adl[k-1])/horz[i][1];
                if(meh[k]==0){
                    meh[k] = meh[i] + tmep;
                }else{
                meh[k] = min(meh[k], meh[i]+tmep);
            }
        }}
        scanf("%d%d", &temp, &q);
        printf("Case #%d: %.9f\n",asd+1 , meh[n-1]);
    }
}
