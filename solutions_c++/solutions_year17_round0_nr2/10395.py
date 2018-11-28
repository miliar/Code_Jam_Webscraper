#include <iostream>
#include <stdio.h>
#include <fstream>
using namespace std;
int n,i,flag,j;
int check(int n){
    int r,rc;
    flag=0;
    while(n){
        rc=n%10;
        n=n/10;
        r=n%10;
        if(rc>=r)
            continue;
        else{
            flag=1;
            break;
        }
    }
    if(flag==0)
        return 1;
    else return 0;
}
int main(void)
{
    int t;
    FILE *f=fopen("A-smalloutput.txt","w");
    scanf("%d",&t);
    for(i=1;i<=t;i++){
        scanf("%d",&n);
        for(j=n;j>0;j--){
            if(check(j)==1){
                fprintf(f,"Case #%d: %d\n",i,j);
                break;
            }
            else continue;
        }
    }
    return 0;
}
