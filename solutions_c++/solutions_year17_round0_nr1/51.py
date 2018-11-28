#include<cstdio>
#include<algorithm>
using namespace std;
char p[1010];
int K, n;
int main(){
    freopen("/Users/joseunghyeon/Downloads/A-large (1).in","r",stdin);
    freopen("/Users/joseunghyeon/Desktop/code2/output.txt","w",stdout);
    int TC, TT, i, j;
    scanf("%d",&TC);
    for(TT=1;TT<=TC;TT++){
        printf("Case #%d: ",TT);
        scanf("%s",p);
        scanf("%d",&K);
        for(i=0;p[i];i++);
        n = i;
        int c = 0;
        for(i=0;i<=n-K;i++){
            if(p[i]=='-'){
                c++;
                for(j=i;j<i+K;j++){
                    p[j]='+'-p[j]+'-';
                }
            }
        }
        for(i=0;i<n;i++)if(p[i]=='-')break;
        if(i==n)printf("%d\n",c);
        else printf("IMPOSSIBLE\n");
    }
}
