#include<cstdio>
#include<iostream>
#include<algorithm>
using namespace std;
int T,n,r,o,y,g,b,v,R[1001];
pair<int,int> a[3];
int main() {
    //freopen("B-small-attempt1.in", "r", stdin);
    //freopen("output_B_2.out", "w", stdout);
    scanf("%d",&T);
    for(int t=1;t<=T;t++) {
        scanf("%d%d%d%d%d%d%d",&n,&r,&o,&y,&g,&b,&v);
        printf("Case #%d: ", t);
        a[0] = {r, 1};
        a[1] = {y, 2};
        a[2] = {b, 3};
        sort(a,a+3);
        if(a[2].first > n/2 && n > 1) puts("IMPOSSIBLE");
        else {
            int i,j;
            for(i=0;i<n;i++) R[i]=0;
            for(i=0,j=0;j<a[2].first;i+=2,j++) R[i%n] = a[2].second;
            for(--i,j=0;j<a[1].first;i+=2,j++) {
                if(R[i%n]) i++;
                R[i%n] = a[1].second;
            }
            for(i=0;i<n;i++) if(!R[i]) R[i] = a[0].second;
            for(i=0;i<n;i++) {
                if(R[i] == 1) putchar('R');
                else if(R[i] == 2) putchar('Y');
                else putchar('B');
            }
            puts("");
        }
    }
    return 0;
}
