#include<bits/stdc++.h>

using namespace std;

int a[1005];
char s[1005];

int main(){
    freopen("A-large.in","r",stdin);
    freopen("A-small-attempt0.out","w",stdout);
    int T,T2;
    cin>>T;
    T2=T;
    while(T--){
        scanf("%s",s);
        int k,res=0;
        cin>>k;
        int n = strlen(s);
        int lc = 0 ;
        for(int i = 0; i<n ; i++)
            s[i] = (s[i]=='+')?0:1;
        for(int i = 0; i<n; i++){
            a[i] = s[i];
            if (i>0) 
                a[i] ^=s[i-1];
            if (i>=k)
                a[i]^=a[i-k];
            res+=a[i]; 
            if (i>n-k&&a[i]==1)
                lc = 1;
        }
        if (lc==0) 
            printf("Case #%d: %d\n", T2-T, res);
        else
            printf("Case #%d: IMPOSSIBLE\n",T2-T);
    }
}
