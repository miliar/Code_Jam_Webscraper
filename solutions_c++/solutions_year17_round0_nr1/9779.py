#include <bits/stdc++.h>
#define mem(a,b) memset(a,b,sizeof(a))
using namespace std;
int _I(){int x; scanf("%d",&x); return x;}
void solve()
{
    int t = _I(),_case = 1;
    while( t-- ){
        char s[1001];
        int k;
        scanf("%s",s);
        scanf("%d",&k);
        int sz = strlen(s);
        int l = 0,ans=0;
        for( int i = 0; i < sz; i++){
            if(s[i]=='-'){
                ans++;
                l = i;
                for(int j = i; j < (i+k); j++){
                    if(s[j]=='-') s[j] = '+';
                    else s[j]= '-';
                }
            }
        }
        //int c =0;
        //for( int i = 0; i < sz; i++) if( s[ i ] == '+' ) c++;
        if(l+k > sz) printf("Case #%d: IMPOSSIBLE\n",_case++);
        else printf("Case #%d: %d\n",_case++,ans);
    }
}
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    //while(1)
    //bitseive();
    solve();
    return 0;
}
