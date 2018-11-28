#include <bits/stdc++.h>
#define N 99
using namespace std;

char a[N],b[N];

int findIndex(int i){
    char x=a[i];
    for(;i>=0;i--){
        if(a[i]!=x) break;
    }
    return i+1;
}

void solve(int tc){
    printf("Case #%d: ",tc);
    memset(a,0,sizeof a);
    memset(b,0,sizeof b);
    scanf("%s",a); int n=strlen(a);
    for(int i=0;i<n;i++){
        if(i+1<n && a[i]>a[i+1]){
            int j=findIndex(i);
            b[j]=a[i]-1;
            for(++j;j<n;j++) b[j]='9';
            break;
        }
        else b[i]=a[i];
    }
    if(b[0]=='0') printf("%s\n",b+1);
    else printf("%s\n",b);
}

int main()
{
    freopen("B-large.in","r",stdin); freopen("out.txt","w",stdout);
    int T; scanf("%d",&T);
    for(int tc=1;tc<=T;tc++){
        solve(tc);
    }
    return 0;
}
