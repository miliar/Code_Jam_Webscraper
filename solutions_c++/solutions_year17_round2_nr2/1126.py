#include<stdio.h>
#include<algorithm>
using namespace std;
int T,n;
char a[10111];
int A;
int main() {
    freopen("B-small-attempt1 (1).in","r",stdin);
    freopen("B-small-attempt1 (1)-out.txt","w",stdout);
    int i,j,k;
    int p,q,r;
    double t,tt,ttt;
    int a1,a2,a3,a4,a5,a6;
    char c1,c3,c5;
    c1 = 'R';
    c3 = 'Y';
    c5 = 'B';

scanf("%d",&T);
for(int ii=0;ii<T;ii++) {
    c1 = 'R';
    c3 = 'Y';
    c5 = 'B';
    scanf("%d",&n);
    scanf("%d %d %d %d %d %d",&a1,&a2,&a3,&a4,&a5,&a6);
    // 1 3 5
    for(i=0;i<10;i++){
        if(a1 < a3) {
            swap(a1,a3);
            swap(c1,c3);
        }
        if(a1 < a5) {
            swap(a1,a5);
            swap(c1,c5);
        }
        if(a3 < a5) {
            swap(a3,a5);
            swap(c3,c5);
        }
    }
    //printf(">%d %c\n",a1,c1);
   // printf(">%d %c\n",a3,c3);
   // printf(">%d %c\n",a5,c5);
    printf("Case #%d: ",ii+1);
    if(a1 > a3 + a5) {
        printf("IMPOSSIBLE\n");
    } else {
        A = 0;
        for(i=0;i<a1;i++) {
            a[A] = c1;
            A++;
        }
        a[A] = c3;
        A++;

     //   for(i=0;i<A;i++)printf("%c ",a[i]);printf("\n\n\n");
        for(i=1;i<a3;i++) {
            t = 0;
            for(j=0;j<A-1;j++) {
                if(a[j] == a[j+1]) {
                    t++;
                    for(k=A;k>j;k--) {
                        a[k] = a[k-1];
                    }
                    a[j+1] = c3;
                    A++;
                    break;
                }
            }
            if(t == 0) {
                for(j=0;j<A-1;j++) {
                    if(a[j] != c3 && c3 != a[j+1]) {
                        for(k=A;k>j;k--) {
                            a[k] = a[k-1];
                        }
                        a[j+1] = c3;
                        A++;
                        break;
                    }
                }
            }
        }
      //  for(i=0;i<A;i++)printf("%c ",a[i]);printf("\n\n");

        for(i=0;i<a5;i++) {
            t = 0;
            for(j=0;j<A-1;j++) {
                if(a[j] == a[j+1]) {
                    t++;
                    for(k=A;k>j;k--) {
                        a[k] = a[k-1];
                    }
                    a[j+1] = c5;
                    A++;
                    break;
                }
            }
            if(t == 0) {
                for(j=0;j<A-1;j++) {
                    if(a[j] != c5 && c5 != a[j+1]) {
                        for(k=A;k>j;k--) {
                            a[k] = a[k-1];
                        }
                        a[j+1] = c5;
                        A++;
                        break;
                    }
                }
            }
        }
        for(i=0;i<A;i++)printf("%c",a[i]);
        printf("\n");
    }
}


    return 0;
}
