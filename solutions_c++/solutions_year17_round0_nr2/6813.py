#include <stdio.h>
#include <iostream>
#include <vector>
#include <string.H>
#include <algorithm>
using namespace std;
int ans[100];
void flip(char *a){
    if(*a == '+')
        *a = '-';
    else if(*a == '-')
        *a = '+';
    //printf("%c",*a);
    return;
}
int tc;
char s[10000];
int k;
int main(){
    FILE *in = fopen("B-large.in.txt","r");
    FILE *out = fopen("output.txt","w");
    fscanf(in,"%d",&tc);
    for(int o = 1; o <= tc; o++){
        fscanf(in,"%s",s);
        bool nine=false;
        for(int i = 0;s[i];i++){
            ans[i] = s[i]-'0';
            if(nine){
                ans[i] = 9;
                continue;
            }
            if(i>0){
                if(ans[i]<ans[i-1]){
                    do{
                        ans[i-1]--;
                        i--;
                    }while(i>0 && ans[i] < ans[i-1]);
                    nine=true;
                }
            }//else ans[i] = s[i]-'0';

            /*for(int i=0;i<strlen(s);i++)
                printf("%d",ans[i]);
            printf("\n");*/
        }
        fprintf(out,"Case #%d: ",o);
        bool start = false;
        for(int i=0;i<strlen(s);i++){
            if(ans[i] != 0)
                start = true;
            if(start)
                fprintf(out,"%d",ans[i]);
        }
        fprintf(out,"\n");
    }
    return 0;
}
/*
3
---+-++- 3
+++++ 4
-+-+- 4
*/
