#include <iostream>
#include <cstdio>
#include <algorithm>
#include <string.h>

using namespace std;
char number[100];
int t;
int main()
{
    FILE*fin=fopen("B-large.in","r");
    FILE*fout=fopen("B-large.out","w");
    fscanf(fin,"%d",&t);
    for(int k=1;k<=t;k++){
        fscanf(fin,"%s",number);
        int len=strlen(number);
        while(1){
            int mark=1;
            for(int i=1;i<len;i++){
                if(number[i-1]>number[i]){
                    number[i-1]=number[i-1]-1;
                    for(int j=i;j<len;j++)
                        number[j]='9';
                    mark=0;
                    break;
                }
            }
            if(mark)
                break;
        }
        fprintf(fout,"Case #%d: ",k);
        int cnt;
        for(cnt=0;cnt<len;cnt++){
            if(number[cnt]!='0')
                break;
        }
        fprintf(fout,"%s\n",number+cnt);
    }
    fclose(fin);
    fclose(fout);
    return 0;
}
