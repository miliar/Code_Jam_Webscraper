#include<bits/stdc++.h>
using namespace std;

typedef long long ll;

int main(){
int t,i;
scanf("%d",&t);
for(i=1;i<=t;i++){
    char nu[22];
    int j,x;
    scanf("%s",nu);
    int n=strlen(nu);
    for(j=1;j<n;j++){
        if(nu[j-1]>nu[j])
            break;
    }
    printf("Case #%d: ",i);
    if(j==n){
        printf("%s\n",nu);
    }
    else{
        if(nu[j-1]=='1'){

            for(x=0;x<n-1;x++)
                printf("9");
           printf("\n");
        }
        else{
             x=j-1;
             while(x>0 && nu[x-1]==nu[x]){
                x--;
             }
             j=x;
             x++;
            while(x!=n)
            {
                nu[x++]='9';
            }
            nu[j]--;
            for(j=0;j<n;j++)
                printf("%c",nu[j]);
            printf("\n");
        }
    }
}


return 0;
}
