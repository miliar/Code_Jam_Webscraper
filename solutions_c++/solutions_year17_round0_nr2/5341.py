#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
using namespace std;

void recur(){
    int check=0,Count=1,mask=1;
    char cur,p;
    scanf("%c",&cur);
    while(true){
        //char c;
        p=cur;
        scanf("%c",&cur);
        Count++;
        if(cur=='\n'){
            if(check==0)
                for(;mask<Count;mask++)
                    printf("%c",p);
            else
                printf("9");
            return;
        }
        else{
            if(check==1)
                printf("9");
            else if(cur<p){
                check=1;
                if(Count==2&&p=='1')
                    continue;
                else if(mask==1&&p=='1')
                    printf("");
                else
                    printf("%c",p-1);
                for(;mask<Count-1;mask++)
                    printf("9");
            }
            else if(cur==p){
                continue;
            }
            else{
                for(;mask<Count;mask++)
                    printf("%c",p);
            }
        }
    }
}
int main() {
    int n;
    scanf("%d\n",&n);
    for(int i=1;i<=n;i++){
        printf("Case #%d: ",i);
        //cout<<"Case #"<<i<<": ";
        recur();
        printf("\n");
    //string num ("1");
    }
    return 0;
}
