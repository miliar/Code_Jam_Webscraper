#include<cstdio>
#include<algorithm>
#include<cstring>
using namespace std;

char inp[1005];
int ans;
int k;

int main()
{
    freopen( "A-large.in" , "r" , stdin );
    freopen( "opt.out" , "w" , stdout );
    int allt,nowt = 0;
    scanf("%d",&allt);
    while(++nowt <= allt){
        ans = 0;
        scanf("%s%d",inp,&k);
        int len = strlen(inp);
        bool fin = false;
        printf("Case #%d: ",nowt);
        for(int i=0;i<len;++i){
            if( inp[i] == '-' ){
                ans++;
                if(i > len-k){
                    printf("IMPOSSIBLE\n");
                    fin = true;
                    break;
                }
                for(int j=i+1;j<i+k;++j){
                    if(inp[j] == '-')
                        inp[j] = '+';
                    else
                        inp[j] = '-';
                }


            }
        }
        if(fin)
            continue;
        printf("%d\n",ans);
    }
    return 0;
}
