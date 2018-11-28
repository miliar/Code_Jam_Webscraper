#include <iostream>
#include <vector>
#include <queue>
#include <map>
#include <string>
#include <stack>

using namespace std;

int main(void){
    int T;
    char dump;
    FILE *fin=fopen("/Users/enyaning/Downloads/B-small-attempt0.in.txt","r");
//    FILE *fin=stdin;
    fscanf(fin,"%d",&T);
    fscanf(fin,"%c",&dump);
    for(int I=1;I<=T;I++){
        char S[20]={0};
        fscanf(fin,"%s",S);
//        getchar();
        int n=(int)strlen(S);
        
        int i;
        for(i=1;i<n;i++){
            if(S[i-1]>S[i]){
                break;
            }
        }
        if(i!=n){
            for(i--;i>=0;i--){
                if(i==0 || S[i-1]<S[i]) break;
            }
            S[i++]-=1;
            for(;i<n;i++){
                S[i]='9';
            }
            if(S[0]=='0'){
                printf("Case #%d: %s\n",I,S+1);
            }else{
                printf("Case #%d: %s\n",I,S);
            }
        }else{
            //already tidy
            printf("Case #%d: %s\n",I,S);
        }
    }
}

/*

3
---+-++- 3
+++++ 4
-+-+- 4
 
*/
