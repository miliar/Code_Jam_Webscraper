#include <stdio.h>
#include <iostream>
#include <vector>
#include <string.H>
#include <algorithm>
using namespace std;
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
    FILE *in = fopen("A-large.in.txt","r");
    FILE *out = fopen("output.out","w");
    fscanf(in,"%d",&tc);
    bool imp = false;
    for(int o = 1; o <= tc; o++){
        cout << o << endl;
        imp = false;
        int count = 0;
        fscanf(in,"%s",s);
        fscanf(in,"%d",&k);

        for(int i=0;s[i];i++){
            if(s[i] == '-'){
                if(i+k > strlen(s)) {
                    imp = true;
                }else{
                    count++;
                for(int j=i;j<i+k;j++)
                    flip(&s[j]);
                }
            }
        }
        if(!imp)
            fprintf(out,"Case #%d: %d\n",o,count);
        else fprintf(out,"Case #%d: IMPOSSIBLE\n",o);
    }
    return 0;
}
/*
3
---+-++- 3
+++++ 4
-+-+- 4
*/
