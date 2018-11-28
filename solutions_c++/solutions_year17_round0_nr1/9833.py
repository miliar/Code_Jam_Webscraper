#include <cstdio>
#include <cstring>

using namespace std;

int main()
{
    int T;

    scanf("%d",&T);

    for(int p=1; p<=T; p++) {
        char str[1001];
        int k,len,ans=0;
        bool IMPOSSIBLE=false;

        scanf("%s %d",str,&k);
        len=strlen(str);

        //printf("%s %d\n",str,k);
        for(int i=0; i<len-k+1; i++) {
            if(str[i] == '-') {
                for(int j=i; j<i+k; j++) {
                    str[j]=(str[j] == '+') ? ('-'):('+');
                }
                ans++;
            }
        }

        for(int i=0; i<len; i++)
            if(str[i]=='-') IMPOSSIBLE=true;
        printf("Case #%d: ",p);
        if(!IMPOSSIBLE) printf("%d\n",ans);
        else printf("IMPOSSIBLE\n");

    }
    return 0;
}
