#include <cstdio>
#include <cstring>
#define FILEIOS freopen("input.txt","r",stdin);freopen("output.txt","w",stdout);
using namespace std;
char A[1004];
int main()
{
    FILEIOS
    int tc,cas=1,k;
    scanf("%d",&tc);
    while(tc--){
        scanf("%s %d",A,&k);
        //printf("%s\n",A);
        int p=0,m=0,ans=0;
        int l=strlen(A);
        for(int i=0;i<l;i++){
            if(A[i]=='+')   p++;
            else    m++;
        }
        for(int i=0;i<l;i++){
            if(A[i]=='+') continue;
            else{
                    if(i+k <= l){
                        ans++;
                        for(int j=i;j<i+k;j++){
                            if(A[j]=='+'){  A[j]='-';p--;m++;}
                            else{
                                    A[j]='+';p++;m--;
                            }
                        }
                    }
                    else    break;
            }
        }
        if(p == l)
            printf("Case #%d: %d\n",cas++,ans);
        else
            printf("Case #%d: IMPOSSIBLE\n",cas++);
    }
    return 0;
}
