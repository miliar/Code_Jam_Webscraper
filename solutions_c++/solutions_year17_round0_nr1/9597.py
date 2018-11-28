#include<bits/stdc++.h>
using namespace std;
int main()
{
    //freopen("a.txt","r",stdin);
    //freopen("b.txt","w",stdout);
    int t,tc=0;
    scanf("%d",&t);
    while(t--){
        int k,counter=0,flag=0;
        char s[1010];
        scanf("%s",&s);
        scanf("%d",&k);
        for(int i=0;i<strlen(s);i++){
            if(s[i]=='-'){
                for(int j=i;j<i+k && i+k<=strlen(s);j++){
                    if(s[j]=='-'){
                        s[j]='+';
                    }
                    else{
                        s[j]='-';
                    }
                }
                counter++;
            }
        }
       for(int i=0;i<strlen(s);i++){
            if(s[i]=='-'){
                flag=1;
            }
       }
       if(flag==1){
            printf("Case #%d: IMPOSSIBLE\n",++tc);
       }
       else{
            printf("Case #%d: %d\n",++tc,counter);
       }
    }
    //freopen("a.txt","w",stdout);
}
