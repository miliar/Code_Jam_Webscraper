#include <iostream>
#include <vector>
#include <queue>
#include <map>
#include <string>
#include <stack>

using namespace std;

int main(void){
    int T;
    scanf("%d",&T);
    for(int I=1;I<=T;I++){
        char S[1000]={0};
        scanf("%s",S);
        int K;
        scanf("%d", &K);
        int n=(int)strlen(S);
        
        char flip[1000]={0};
        int current=0;
        int res=0;
        
        for(int i=0;i<=n-K;i++){
            int x;
            if(S[i]=='-') x=1;
            else x=0;
            
            if(i>=K) current-=flip[i-K];
            x=(x+current)%2;
            
            if(x==1){
                flip[i]=1;
                res+=1;
            }else{
                flip[i]=0;
            }
            current+=flip[i];
        }
        
//        for(int i=0;i<n;i++) printf("%d ", flip[i]); printf("\n");
//        printf("current %d\n", current);
        
        for(int i=n-K+1;i<n;i++){
            int x;
            if(S[i]=='-') x=1;
            else x=0;
            
            if(i>=K) current-=flip[i-K];
            x=(x+current)%2;
            
            if(x==1) res=-1;
        }
        
        printf("Case #%d: ",I);
        if(res==-1){
            printf("IMPOSSIBLE\n");
        }else{
            printf("%d\n",res);
        }
    }
}

/*

3
---+-++- 3
+++++ 4
-+-+- 4
 
*/
