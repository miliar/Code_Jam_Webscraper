#include<stdio.h>
#include<string.h>
int T;
char c[100];
int a[100];
int n;
int main() {
    freopen("B-large.in","r",stdin);
    freopen("B-large-out.txt","w",stdout);
    int i,j,k;
    int p,q,r;

scanf("%d",&T);
for(int ii=0;ii<T;ii++) {
    scanf("%s",c);
    printf("Case #%d: ",ii+1);
    n = strlen(c);
    for(i=0;i<n;i++)a[i] = c[i] - '0';

    while(1) {
        r = -1;
        for(i=0;i<n-1;i++) {
            if(a[i] > a[i+1]) {
                r = i;
                break;
            }
        }
        if(r == -1) break;
        a[r] --;
        for(i = r+1; i < n; i++) {
            a[i] = 9;
        }
    }
    if(a[0] != 0) printf("%d",a[0]);
    for(i=1;i<n;i++)printf("%d",a[i]);
    printf("\n");

}



    return 0;
}
