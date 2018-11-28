#include <bits/stdc++.h>
using namespace std;
#define mem(a,b) memset(a,b,sizeof(a))
#define PI acos(-1.0)
#define mod 100000007
bool check(int n,int p){return (bool)n&(1<<p);}
int Set(int n,int p){return n|(1<<p);}
int _I(){int x; scanf("%d",&x); return x;}
bool f(int n)
{
    char ch[10];
    sprintf(ch,"%d",n);
    int l = strlen(ch);
    //printf("%s\n",ch);
    for( int j = 1 ; j < l; j++ ){
        if((ch[ j ]-'0') < (ch[ j-1 ]-'0')) return false;
    }
    return true;
}
int ans[ 10001 ];
void precal()
{
    int a;
    for( int i = 1; i <= 1110; i++){
        if(f(i)) a = i;
        //printf("%d\n",a);
        ans[ i ] = a;
    }
}
void solve()
{
    int t = _I(),_case = 1;
    while( t-- ){
        int n = _I();
        printf("Case #%d: %d\n",_case++,ans[ n ]);
    }
}
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.out","w",stdout);
    //while(1)
    precal();
    solve();
    return 0;
}
