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
int n, m, t, r[10], dt[101][101][101][101];

int dp(int k, int w, int x, int y, int z, int v)
{
    if( w > r[0] or x > r[1] or y > r[2] or z > r[3] ) return -oo;
    if( k == n ) return 0;
    if( ~dt[w][x][y][z] ) return dt[w][x][y][z];
    int &ret = dt[w][x][y][z] = 0;
    for(int i = 0 ; i < m ; i++ )
    {
        switch(i){
            case 0: ret=max(ret, dp(k+1, w+1, x, y, z, v) + (v?0:1) ); break;
            case 1: ret=max(ret, dp(k+1, w, x+1, y, z, (v+1)%m) + (v?0:1) ); break;
            case 2: ret=max(ret, dp(k+1, w, x, y+1, z, (v+2)%m) + (v?0:1) ); break;
            case 3: ret=max(ret, dp(k+1, w, x, y, z+1, (v+3)%m) + (v?0:1) ); break;
        }
    }
    return ret;
}

void solve(int no)
{
    memset(dt, -1, sizeof(dt));
    memset(r, 0, sizeof(r));
    cin>>n>>m;
    for(int i = 0 ; i < n ; i++ ) cin>>t, r[t%m]++;
    cout<<"Case #"<<no<<": "<<dp(0,0,0,0,0,0)<<endl;
    return;
}

int main()
{
    freopen("C:\\Users\\Jeong Family\\Downloads\\in.txt", "r", stdin);
    freopen("C:\\Users\\Jeong Family\\Downloads\\out.txt", "w", stdout);
    ios::sync_with_stdio(false);
    int t;
    cin>>t;
    for(int i = 1 ; i <= t ; i++ ) solve(i);
    return 0;
}

