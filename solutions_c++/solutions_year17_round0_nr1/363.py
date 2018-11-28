#include <bits/stdc++.h>
#include <unordered_map>

using namespace std;

int main(){
    freopen("hi.txt","r",stdin);
    freopen("hi2.txt","w",stdout);
    int tc;
    scanf("%d",&tc);
    char str[1010];
    for(int t=1;t<=tc;t++){
        scanf("%s",str);
        int k;
        scanf("%d",&k);
        int len=strlen(str);
        int ans=0;
        bool can=true;
        for(int i=0;i<len;i++){
            if(str[i]=='-'){
                if(i+k-1>=len){
                    can=false;
                    break;
                }
                for(int j=0;j<k;j++){
                    if(str[i+j]=='-'){
                        str[i+j]='+';
                    }
                    else{
                        str[i+j]='-';
                    }
                }
                ans++;
            }
        }
        printf("Case #%d: ",t);
        if(can){
            printf("%d\n",ans);
        }
        else{
            printf("IMPOSSIBLE\n");
        }
    }
    return 0;
}
