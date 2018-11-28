#include <cstdio>
#include <algorithm>


using namespace std;

int n,m,c;
int cntbuy[1010];
int cntpos[1010];
int p[1010];
int b[1010];
int now[1010];
int main (){
    int T;
    scanf("%d",&T);
    for(int I = 1 ; I <= T ; I ++){
        scanf("%d%d%d",&n,&c,&m);
        fill(p,p+1010,0);
        fill(b,b+1010,0);
        fill(cntbuy,cntbuy+1010,0);
        fill(cntpos,cntpos+1010,0);
        for(int i = 0 ; i < m ; i ++){
            int pos,buy;
            scanf("%d%d",&pos,&buy);
            pos--;
            buy--;
            cntbuy[buy]++;
            cntpos[pos]++;
        }
        int minr = 0;
        for(int i = 0 ; i < c ; i ++){
            minr=max(minr,cntbuy[i]);
        }
        int ans;
        for(int r = minr ; r < 1010 ; r ++){
            for(int i = 0 ; i < n ; i ++){
                now[i]=cntpos[i];
            }
            for(int i = n-1 ; i > 0 ; i --){
                if(now[i]>r){
                    now[i-1]+=now[i]-r;
                    now[i]=r;
                }
            }
            if(now[0]<=r){
                ans=r;
                break;
            }
        }
        int pro=0;
        for(int i = 0 ; i < n ; i ++){
            if(cntpos[i]>ans){
                pro+=cntpos[i]-ans;
            }
        }
        printf("Case #%d: %d %d\n",I,ans,pro);
    }
}
