#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

using namespace std;

void file_inout(bool active){
    if(active){
        freopen("input","r",stdin);
        freopen("output","w",stdout);
    }
}

int main()
{
    file_inout(true);
    int cases = 0;
    int k = 0;
    scanf("%i",&cases);
    for(int index=0;index<cases;index++){
        char pancakes[1001];
        scanf("%s",pancakes);
        scanf("%i",&k);
        char prev = pancakes[0];
        int total = 0;
        int pancakes_length = strlen(pancakes);
        for(int i=0;i<=pancakes_length-k;i++){
            if(pancakes[i] == '-'){
                for(int j=i;j<i+k;j++){
                    pancakes[j] = (pancakes[j]=='+'?'-':'+');
                }
//                printf("T: %s\n",pancakes);
                total++;
            }
        }
        bool success = true;
        for(int i=pancakes_length-k;i<pancakes_length;i++){
            success =success && (pancakes[i]=='+');
        }
        char result[10];
        itoa(total,result,10);
        printf("Case #%i: %s\n",index+1,success?result:"IMPOSSIBLE");
    }
    return 0;
}
