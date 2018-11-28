#include <iostream>
#include <cstdio>
#include <algorithm>
#include <string.h>

using namespace std;
char num[25];

int main()
{
    int t;
    FILE*f1=fopen("B-large.in","r");
    FILE*f2=fopen("B-large.out","w");
    fscanf(f1,"%d",&t);
    for(int tt=1;tt<=t;tt++){
        fscanf(f1,"%s",num);
        int len=strlen(num);
        while(1){
            bool flag=true;
            for(int i=1;i<len;i++){
                if(num[i-1]>num[i]){
                    flag=false;
                    num[i-1]--;
                    for(int j=i;j<len;j++)
                        num[j]='9';
                    break;
                }
            }
            if(flag)
                break;
        }
        fprintf(f2,"Case #%d: ",tt);
        int idx=0;
        for(;idx<len;idx++){
            if(num[idx]!='0')
                break;
        }
        fprintf(f2,"%s\n",num+idx);
    }
    fclose(f1);
    fclose(f2);
    return 0;
}
