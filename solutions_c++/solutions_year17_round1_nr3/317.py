#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <string.h>
#include <set>
using namespace std;

typedef long long ll;
typedef pair<int,int> pii;

int main(){
    int tcn;
    scanf("%d",&tcn);
    for(int tc=1;tc<=tcn;tc++){
        printf("Case #%d: ",tc);
        int h1, a1, h2, a2;
        int b,d;
        scanf("%d%d%d%d%d%d",&h1,&a1,&h2,&a2,&b,&d);
        int amin = 2000000001;
        int ans = 2000000001;
        for(int i=0;i<=100;i++){
            if(i&&b==0)continue;
            int na1 = a1 + b*i;
            int count = h2/na1 + (h2%na1 ? 1 : 0);
            amin = min(amin, count + i);
        }
        for(int i=0;i<=100;i++){
            if(i && d==0)continue;
            int flag = 0;
            int na2 = a2 - d*i;
            int count = amin + i;
            int remaind = i;
            int h = h1;
            int ak = a2;
            int remaina = amin;
            while(remaina){
                if(remaina == 1)break;
                if((!remaind && remaina > 2 && h1 <= 2*ak )){
                    flag = 1;
                    break;
                }
                if(h != h1 && h != h1 - ak && ((!remaind && h <= ak) || (remaind && h <= ak-d))){
                    count++;
                    //printf("%d %d %d\n", h1, ak, h);
                    h = h1;
                }
                else if(remaind){
                    remaind--;
                    ak -= d;
                }
                else remaina--;
                h -= ak;
                if(h <= 0){
                    flag = 1;
                    break;
                }
            }
            if(!flag)ans = min(ans, count);
        }
        if(ans == 2000000001){
            printf("IMPOSSIBLE\n");
        }
        else{
            printf("%d\n",ans);
        }
    }
}
