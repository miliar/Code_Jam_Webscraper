#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <iostream>

#define MAXN 1005
using namespace std;

char a[MAXN];
int k;

void solve()
{
    scanf("%s", a);
    scanf("%d", &k);
    int len=strlen(a);
    int cnt=0;
    for(int i=0;i<len;i++){
        if(a[i]=='-'){
            if(i>len-k){
                printf("IMPOSSIBLE\n");
                return;
            }
            else{
                cnt++;
                for(int j=i;j<i+k;j++){
                    a[j]=((a[j]=='-')?'+':'-');
                }
            }
        }
    }
    printf("%d\n", cnt);
}

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int t;  cin >> t;
    for(int i=1;i<=t;i++){
        printf("Case #%d: ", i);
        solve();
    }
    return 0;
}
