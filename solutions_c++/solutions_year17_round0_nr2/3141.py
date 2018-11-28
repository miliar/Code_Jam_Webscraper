#include <bits/stdc++.h>

#define st first
#define nd second
using namespace std;

typedef long long LL;

int a[10000];
int n;
char st[100];


void solve(int cs){
    scanf("%s",st);
    int l=strlen(st);
    for (int i=0;i<l;++i) a[i]=st[i]-48;
    for (int i=l-1;i>0;--i){
        if (a[i]<a[i-1]) {
            a[i-1]--;
            for (int j=i;j<l;++j) a[j]=9; 
        }
    }
    printf("Case #%d: ",cs);
    int i=0;
    while (a[i]==0) ++i;
    for (;i<l;++i) printf("%d",a[i]);
    printf("\n");
}
 
int main(){
    int tot;
    scanf("%d",&tot);
    for (int i=1;i<=tot;++i) solve(i);
}
