#include <cstdio>
#include <algorithm>
#include <cstring>
using namespace std;

int main(){
    int tcn;
    scanf("%d",&tcn);
    for(int tc=1;tc<=tcn;tc++){
        printf("Case #%d: ",tc);
        char pan[1010];
        int k;
        int n;
        scanf("%s%d",pan,&k);
        n = strlen(pan);
        int ans = 0;
        for(int i=0;i<n-k+1;i++){
            if(pan[i]=='-'){
                for(int j=0;j<k;j++){
                    pan[j+i] = pan[j+i] == '-'?'+':'-';
                }
                ans++;
            }
        }
        int flag = 0;
        for(int i=0;i<n;i++){
            if(pan[i] == '-')flag = 1;
        }
        if(flag){
            printf("IMPOSSIBLE\n");
        }
        else{
            printf("%d\n",ans);
        }

    }
}
