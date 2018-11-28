#include <iostream>
#include <stdio.h>
#include <string.h>
using namespace std;
char cad[25];
int num[25];
int main()
{

    int t,l;
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    scanf("%d",&t);
    for (int _case=1; _case<=t; _case++){
        scanf("%s",cad);
        num[0]=0;
        l=strlen(cad);
        for (int i=0; i<l; i++){
            num[i+1]=cad[i]-'0';
        }
        for (int i=1; i<l; i++){
            if (num[i]>num[i+1]){
                int j=i;
                while (j>0 && num[j]==num[j-1])j--;
                num[j]=num[j]-1;
                for (int k=j+1; k<=l; k++)num[k]=9;
                break;
            }
        }
        int i=1;
        while (num[i]==0)i++;
        printf("Case #%d: ",_case);
        for (int k=i; k<=l; k++){
            printf("%d",num[k]);
        }
        printf("\n");
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
