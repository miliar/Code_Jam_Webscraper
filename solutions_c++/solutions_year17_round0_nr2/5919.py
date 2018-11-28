#include <cstdio>
#include <algorithm>
#include <string>
#include <iostream>
#define INT long long
using namespace std;
void make(INT val, int v, int k, INT &ans, INT n)
{
    if( val > n ) return;
    if( k == 0 ) return;
    ans = max(ans, val);
    for(int i = v ; i < 10 ; i++ )
        make(val*10+i, i, k-1, ans, n);
}
void solve(int no)
{
    INT n, ans = 0;
    cin>>n;
    make(0, 1, 18, ans, n);
    cout<<"Case #"<<no<<": "<<ans<<endl;
    return;
}

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    cin>>t;
    for(int i = 1 ; i <= t ; i++ ) solve(i);
    return 0;
}
