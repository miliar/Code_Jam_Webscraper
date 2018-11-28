#include <cstdio>
#include <algorithm>
#include <cstring> 
using namespace std;
char s[20];
int T,ans[20];
int main(){
	//freopen("B-large.in","r",stdin);
	//freopen("B-large.out","w",stdout);
    scanf("%d",&T);
    for(int cas=1;cas<=T;cas++){
        printf("Case #%d: ",cas);
        scanf("%s",s);
        int len=strlen(s);
        int i;
        for(int i=0;i<len;i++)ans[i]=9;
        int flag=0;
        for(i=0;i<len;i++){
        	if(i==len-1)break;
            if(s[i+1]<s[i]){
            	flag=1;
                break;
            }ans[i]=s[i]-'0';
        }if(flag){
            while(i>0&&s[i]==s[i-1])ans[i]=9,i--;
            ans[i]=s[i]-'0'-1;
		}if(!flag)ans[len-1]=s[len-1]-'0';
		for(i=0;i<len;i++)if(ans[i])break;
		for(;i<len;i++)printf("%d",ans[i]);
        puts("");
    }return 0;
}
