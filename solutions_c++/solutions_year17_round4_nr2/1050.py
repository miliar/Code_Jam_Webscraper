#include<stdio.h>
#include<cstring>
#include<algorithm>
#include<cstdlib>
#include<cmath>
#include<vector>

using namespace std;

typedef long long int lli;
typedef vector<int> vi;
typedef pair<int, int> ii;
typedef vector<ii> vii;

int c1[1010];
int c2[1010];
int tc1;
int tc2;


int main(void){
    freopen("B-small-attempt1.in", "r", stdin);
    freopen("B-small-attempt1.out", "w", stdout);
    int t;
    scanf("%d",&t);
    for(int u=1;u<=t;++u){
        int n, c, m;
        scanf("%d %d %d",&n,&c,&m);
        tc1 = 0;
        tc2 = 0;
        int tic1[1010];
        int tic2[1010];
        fill(tic1,tic1+1010,0);
        fill(tic2,tic2+1010,0);
        for(int i=0;i<m;++i){
            int p, b;
            scanf("%d %d",&p,&b);
            if(b==1){
                tic1[p]++;
                tc1++;
            }else{
                tic2[p]++;
                tc2++;
            }
        }
        int maxx = max(tc1,tc2);
        int total = maxx;
        int ups = 0;
        for(int i=n;i>0;i--){
            if(tic1[i]+tic2[i]>maxx){
                if(i==1){
                    total+=(tic1[i]+tic2[i]-maxx);
                }else{
                    ups+=(tic1[i]+tic2[i]-maxx);
                }
            }
        }
        printf("Case #%d: %d %d\n",u,total,ups);
    }
    return 0;
}

