#include<bits/stdc++.h>
using namespace std;

int n,pp;
int G[123];

void work(int ca) {
    scanf("%d%d",&n,&pp);
    for(int i = 0;i < n;i++) {
        scanf("%d",&G[i]);
        G[i] %= pp;
    }
    sort(G,G + n);
    int* p = upper_bound(G,G + n,0);
    int ans = p - G;
    int idx = ans;
    if(pp == 2){
        ans += (G + n - p) / 2;
        if((G + n - p) % 2 == 0)
            ans--;
    }else if(pp == 3){
        int n1 = upper_bound(p,G + n,1) - p;
        int n2 = n - ans - n1;
        if(n1 >= n2){
            ans += n2 + (n1 - n2) / 3;
            n1 -= n2;
            if(n1 % 3 == 0)
                ans--;
        } else{
            ans += n1 + (n2 - n1) / 3;
            n2 -= n1;
            if(n2 % 3 == 0)
                ans--;
        }
    }
    printf("Case #%d: %d\n",ca,ans + 1);
}

int main(){
    int t;
    scanf("%d",&t);
    for(int _ = 1;_ <= t;_++)
        work(_);
    return 0;
}
