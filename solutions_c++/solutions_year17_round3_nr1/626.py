#include <iostream>
#include <algorithm>
#include <cstdio>
#include <string>
#include <vector>
#include <queue>
#include <cstring>
#include <iomanip>
#define INT long long int
#define oo 987654321
#define PI 3.1415926535

using namespace std;
INT dt[1010][1010], n, k;
struct CAKE{ INT h, r; } s[1010];
bool cmp(CAKE x, CAKE y)
{
    if( x.r == y.r ) return x.h > y.h;
    return x.r < y.r;
}

INT dp(INT x, INT y)
{
    if( y == k ) return s[x-1].r * s[x-1].r;
    if( x == n ) return 0;
    if( ~dt[x][y] ) return dt[x][y];
    INT &ret = dt[x][y];
    return ret = max(dp(x+1, y), dp(x+1, y+1)+2*s[x].r*s[x].h);
}

void solve(int no)
{
    memset(dt, -1, sizeof(dt));
    cin>>n>>k;
    for(int i = 0 ; i < n ; i++ ) cin>>s[i].r>>s[i].h;
    sort(s, s+n, cmp);
    cout<<"Case #"<<no<<": "<<setprecision(20)<<PI*dp(0, 0)<<endl;
    return;
}

int main()
{
    freopen("C:\\Users\\JKJeong\\Downloads\\in.txt", "r", stdin);
    freopen("C:\\Users\\JKJeong\\Downloads\\out.txt", "w", stdout);
    ios::sync_with_stdio(false);
    int t;
    cin>>t;
    for(int i = 1 ; i <= t ; i++ ) solve(i);
    return 0;
}

