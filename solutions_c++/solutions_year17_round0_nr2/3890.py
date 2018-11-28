#include<cstdio>
#include<cstring>
using namespace std;
const int N=20;
char s[20];
int main()
{
    freopen("in.in","r",stdin);
    freopen("out.out","w",stdout);
    int T,kase=0;
    scanf("%d",&T);
    while(T--){
        printf("Case #%d: ",++kase);
        scanf("%s",s);
        int n=strlen(s);
        if(n==1){
            puts(s);
            continue;
        }
        for(int i=0;i<n-1;i++){
            if(s[i]>s[i+1]){
                s[i]=s[i]-1;
                for(int j=i+1;j<n;j++)
                    s[j]='9';
                int j=i;
                while(j&&s[j]<s[j-1]){
                    s[j-1]=s[j-1]-1;
                    s[j]='9';
                    j--;
                }
            }
        }
        if(s[0]=='0')puts(s+1);
        else puts(s);
    }
    return 0;
}
