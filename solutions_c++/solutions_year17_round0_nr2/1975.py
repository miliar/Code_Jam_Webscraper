#pragma comment(linker, "/STACK:1024000000,1024000000")
#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <vector>
#include <set>
#include <map>
#include <string>
using namespace std;
#define LL long long
#define mp make_pair
#define fr first
#define sc second
#define pb push_back
#define lc (x<<1)
#define rc ((x<<1)|1)
const int N=105;
char s[N];
int a[N],b[N];
bool check(int n){
    for (int i=2;i<=n;i++) if (b[i]<b[i-1]) return 0;
    return 1; 
}
void PRT(int T,int n){
    int i=1;while (!b[i]) i++;
    cout<<"Case #"<<T<<": ";
    for (;i<=n;i++) printf("%d",b[i]);
    puts("");
}
int main(){
  //  freopen("in.txt","r",stdin);freopen("out.txt","w",stdout);
    int T,T0=0;cin>>T;
    while (T--){
        int i,j,n;
        scanf("%s",s+1);n=strlen(s+1);
        for (i=1;i<=n;i++) a[i]=b[i]=s[i]-'0';
        if (check(n)) {PRT(++T0,n);continue;}
        for (i=n-1;i>=1;i--){
            for (j=1;j<=n;j++) b[j]=a[j];
            if (!b[i]) continue;b[i]--;
            for (j=i+1;j<=n;j++) b[j]=9;
            if (check(n)) break;
        }
        PRT(++T0,n);
    }
  //  system("pause");
    return 0;
}
