#include<stdio.h>
#include<string.h>
int main(){
//   freopen("in.txt","r",stdin);
//   freopen("out.txt","w",stdout);
    int T;scanf("%d",&T);
    char s[20];
    for(int t=1;t<=T;t++){
        scanf("%s",s);
        int n=strlen(s);
        printf("Case #%d: ",t);
        if(n==1) printf("%s\n",s);
        else {
            int l=n,k=n;
            for(int i=0;i<n;i++){
                int j=i;
                while(s[j]==s[i]&&j<n) j++;
                if(j<n&&s[i]>s[j]) {l=i,k=j-1;break;}
                i=j-1;
            }
            if(l!=0)
            for(int i=0;i<n;i++){
                if(i<l) printf("%c",s[i]);
                else if(i>=l&&i<=k) printf("%c",s[i]-1);
                else printf("9");
            }
            else{
                if(s[0]!='1') printf("%c",s[0]-1);
                for(int i=0;i<n-1;i++) printf("9");
            }
            printf("\n");
        }
    }
    return 0;
}
