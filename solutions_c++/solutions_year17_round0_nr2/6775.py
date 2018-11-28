#include<bits/stdc++.h>

using namespace std;



bool isTidy(char * a){

    long long int i,l;
    l = strlen(a);
    for(i=0;i<l-1;i++){
        if(a[i+1]<a[i])
            return false;
    }
    return true;

}

int main(){

    long long int t,n,i,j,a,b,l,k;
    char curWord[25],other[25],pura[50];

    scanf("%lld",&t);
    for(i=1;i<=t;i++){
        getchar();
        scanf("%s",pura);
        l = strlen(pura);

        while( !isTidy(pura) ){
            for(j=0;j<l-1;j++){
                if(pura[j]>pura[j+1]){
                    a = j;
                    break;
                }
            }
            pura[a]--;
            for(k = a+1;k<l;k++)
                pura[k] = '9';

        }

        printf("Case #%d: ",i);
        if(pura[0]>'0')
            printf("%c",pura[0]);
        for(k=1;k<l;k++){
            printf("%c",pura[k]);
        }
        printf("\n");
    }


    return 0;
}
