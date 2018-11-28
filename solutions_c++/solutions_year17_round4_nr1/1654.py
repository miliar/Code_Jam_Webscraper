#include <cstdio>
#include <cstring>
#include <algorithm>
#include <iostream>
#include <cstdlib>
#include <cmath>
#include <queue>
#include <vector>
#include <map>
#define pb push_back
#define mp make_pair
#define eps 1e-9
#define zero(x) (fabs(x)<eps)
#define pi acos(-1.0)
#define ff1 first
#define ff2 second
#define ms(x,y) memset(x,y,sizeof(x))
using namespace std;
#define fr(i,x,y) for(int i=x;i<=y;i++)
typedef long long ll;
typedef pair <int, int> PII;
template<typename X> inline bool minimize(X&p,X q){if(p<=q)return 0;p=q;return 1;}
template<typename X> inline bool maximize(X&p,X q){if(p>=q)return 0;p=q;return 1;}
const ll inf=1000000000000;
struct node{
    int x,y;
    bool operator<(const node&oth )const{
        return x<oth.x;
    }
};

char s[1005];
int nn[5];
int dp3[102][102][102][3],dp2[102][102][3];
int n,p;
int a[105];
void doit(){
    scanf("%d%d",&n,&p);
    ms(nn,0);
    int sum=0;
    fr(i,1,n){
        scanf("%d",&a[i]);
        a[i]%=p;
        nn[a[i]]++;
        sum+=a[i];
    }
    sum%=p;
    if (p==2) {
        ms(dp2, 222);
        dp2[0][0][0] = 0;
        fr(i, 0, nn[0])fr(j, 0, nn[1])fr(z, 0, 1)if (dp2[i][j][z] >= 0) {
                        if (z == 0)maximize(dp2[i + 1][j][0], dp2[i][j][z] + 1);
                        if (z == 0)maximize(dp2[i][j + 1][1], dp2[i][j][z] + 1);
                        if (z == 1)maximize(dp2[i + 1][j][1], dp2[i][j][z]);
                        if (z == 1)maximize(dp2[i][j + 1][0], dp2[i][j][z]);
                    }
        printf("%d\n",dp2[nn[0]][nn[1]][sum]);
        return;
    }
    if (p==3) {
        ms(dp3, 222);
        //printf("%d %d %d\n",nn[0],nn[1],nn[2]);
        dp3[0][0][0][0] = 0;
        fr(i, 0, nn[0])fr(j, 0, nn[1])fr(k, 0, nn[2])fr(z, 0, 2)if (dp3[i][j][k][z] >= 0) {

                            maximize(dp3[i+1][j][k][z], dp3[i][j][k][z]+(z==0));
                            maximize(dp3[i][j+1][k][(z+1)%3], dp3[i][j][k][z]+(z==0));
                            maximize(dp3[i][j][k+1][(z+2)%3], dp3[i][j][k][z]+(z==0));

                        }
        printf("%d\n",dp3[nn[0]][nn[1]][nn[2]][sum]);
        return;
    }

}


int main() {

    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0.out","w",stdout);
    int cas,i=0;
    scanf("%d",&cas);
    while (cas--)
    {
            printf("Case #%d: ",++i);
            doit();

    }


}

