#include <bits/stdc++.h>

using namespace std;

int main(){
    freopen("hi.txt","r",stdin);
    freopen("hi2.txt","w",stdout);
    int tc;
    scanf("%d",&tc);
    char str[110];
    char ans[110];
    for(int t=1;t<=tc;t++){
        scanf("%s",str);
        int n=strlen(str);
        int dec=-1;
        for(int i=0;i<n-1;i++){
            if(str[i]>str[i+1]){
                dec=i;
                break;
            }
        }
        if(dec==-1){
            printf("Case #%d: %s\n",t,str);
            continue;
        }
        int pos=dec;
        for(int i=dec;i>=0;i--){
            if(str[i]!=str[dec])break;
            pos=i;
        }
        for(int i=0;i<pos;i++){
            ans[i]=str[i];
        }
        ans[pos]=str[pos]-1;
        for(int i=pos+1;i<n;i++){
            ans[i]='9';
        }
        printf("Case #%d: ",t);
        bool leading=true;
        for(int i=0;i<n;i++){
            if(ans[i]=='0' && leading){
                continue;
            }
            leading=false;
            printf("%c",ans[i]);
        }
        printf("\n");
    }
    return 0;
}
