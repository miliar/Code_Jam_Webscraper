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
INT dt[1510][780][3][3], n, k, x, y, T[1500];

INT dp(INT x, INT y, INT z, INT zz)
{
    if( x == 1440 ) return y == 720 ? (z==zz?0:1): oo;
    if( ~dt[x][y][z][zz] ) return dt[x][y][z][zz];
    INT &ret = dt[x][y][z][zz];
    if( x == 0 )
    {
        if( !T[x] ) ret = min( dp(x+1, y+1, 1, 1), dp(x+1, y, 2, 2));
        else if( T[x] == 1 ) ret = dp(x+1, y+1, 1, 1);
        else if( T[x] == 2 ) ret = dp(x+1, y, 2, 2);
        return ret;
    }
    if( !T[x] ) ret = min( dp(x+1, y+1, 1,zz) + (z==2?1:0), dp(x+1, y, 2, zz) + (z==1?1:0) );
    else if( T[x] == 1 ) ret = dp(x+1, y+1, 1, zz) + (z==2?1:0);
    else if( T[x] == 2 ) ret = dp(x+1, y, 2, zz) + (z==1?1:0);
    return ret;
}

void solve(int no)
{
    memset(dt, -1, sizeof(dt));
    memset(T, 0, sizeof(T));
    cin>>x>>y;
    while( x-- )
    {
        INT a, b;
        cin>>a>>b;
        for(int i = a ; i < b ; i++ ) T[i] = 2;
    }
    while( y-- )
    {
        INT a, b;
        cin>>a>>b;
        for(int i = a ; i < b ; i++ ) T[i] = 1;
    }
    //for(int i = 0 ; i <= 1440 ; i++ ) if( T[i] ) cout<<i<<":"<<T[i]<<endl;
    cout<<"Case #"<<no<<": "<<dp(0, 0, 0, 0)<<endl;
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

