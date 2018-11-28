#include<stdio.h>
#include<algorithm>
using namespace std;

int n,m,T;
int a1[111],a2[111];
int b1[111],b2[111];

int main() {
   freopen("B-small-attempt0 (3).in","r",stdin);
    freopen("B-small-out.txt","w",stdout);

    int i,j,k;
    int p,q,r;
    int t,tt,ttt;
    int ans;

scanf("%d",&T);
for(int ii=0;ii<T;ii++) {
    scanf("%d %d",&n,&m);
    for(i=0;i<n;i++) {
        scanf("%d %d",&a1[i],&a2[i]);
    }
    for(i=0;i<m;i++) {
        scanf("%d %d",&b1[i],&b2[i]);
    }

    if(n == 0 && m == 1) {
        if(b1[0] < 720 && 720 < b2[0]) ans = 2;
        else ans = 2;
    } else if(n == 0 && m == 2) {
        if(b1[0] > b1[1]) {
            swap(b1[0],b1[1]);
            swap(b2[0],b2[1]);
        }

        if(b2[1] <= 720) ans = 2;
        else if(720 <= b1[0]) ans = 2;
        else if(b2[1] - b1[0] <= 720) ans = 2;
        else if(b2[0] + (1440 - b1[1]) <= 720) ans = 2;
        else if(b2[0] + (b2[1] - b1[1]) <= 720) ans = 4;
        else if((b2[0] - b1[0]) + (1440 - b1[1]) <= 720) ans = 4;
        else ans = 4;
    } else if(n == 1 && m == 0) {
        if(a1[0] < 720 && 720 < a2[0]) ans = 2;
        else ans = 2;
    } else if(n == 1 && m == 1) {
        if(a1[0] > b1[0]) {
            swap(a1[0],b1[0]);
            swap(a2[0],b2[0]);
        }
        if(a2[0] <= 720 && 720 <= b1[0]) ans = 2;
        else ans = 2;
    } else if(n == 2 && m == 0) {
        if(a1[0] > a1[1]) {
            swap(a1[0],a1[1]);
            swap(a2[0],a2[1]);
        }

        if(a2[1] <= 720) ans = 2;
        else if(720 <= a1[0]) ans = 2;
        else if(a2[1] - a1[0] <= 720) ans = 2;
        else if(a2[0] + (1440 - a1[1]) <= 720) ans = 2;
        else if(a2[0] + (a2[1] - a1[1]) <= 720) ans = 4;
        else if((a2[0] - a1[0]) + (1440 - a1[1]) <= 720) ans = 4;
        else ans = 4;
    }

    printf("Case #%d: %d\n",ii+1,ans);
}


    return 0;
}

