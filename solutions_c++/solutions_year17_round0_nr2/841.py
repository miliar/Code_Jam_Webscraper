#include <stdio.h>

int T, Digit[30], Top;
long long N;

int main(void) {

    int i, j, k;

    freopen("B-large.in","r",stdin);
    freopen("output.txt","w",stdout);

    scanf("%d",&T);
    for(i=1 ; i<=T ; i++) {
        scanf("%lld",&N);
        Top=0;
        Digit[0]=10;
        while(N) {
            Digit[++Top]=N%10;
            N/=10;
        }
        Digit[Top+1]=0;
        for(j=Top ; j>=1 ; j--)
            if(Digit[j-1]<Digit[j])
                break;
        for(k=j-1 ; k>=1 ; k--)
            Digit[k]=9;
        Digit[j]--;
        while(Digit[j+1]>Digit[j]) {
            Digit[j+1]--;
            Digit[j]=9;
            j++;
        }
        if(!Digit[Top])
            Top--;
        printf("Case #%d: ",i);
        for(j=Top ; j>=1 ; j--)
            printf("%d",Digit[j]);
        printf("\n");
    }

    return 0;
}
