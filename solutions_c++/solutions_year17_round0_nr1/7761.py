#include<bits/stdc++.h>
using namespace std;
int a[1005];
int main(){
    freopen("A-large.in", "r", stdin);
    freopen("output2.txt", "w", stdout);
    int tst,c=1;
    scanf("%d",&tst);
    string s;
    while(tst--){
        cin>>s;
        int i,j,l,f,k,ans=0;
        scanf("%d",&k);
        l=s.length();
        printf("Case #%d: ",c);
        c++;
        for(i=0;i<l;i++)
            if(s[i]=='-')
            a[i]=0;
            else
            a[i]=1;
        for(i=0;i<=l-k;i++){
            if(a[i]==0){
                ans++;
                j=i;
                for(f=1;f<=k;f++,j++){
                    a[j]=!a[j];
                }
            }
        }
        f=1;
        for(;i<l;i++){
            if(a[i]==0){
                f=0;break;
            }
        }
        if(f==0){
            printf("IMPOSSIBLE\n");
        }
        else{
            printf("%d\n",ans);
        }
    }
    return 0;
}
