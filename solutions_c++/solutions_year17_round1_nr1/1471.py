#include<bits/stdc++.h>
using namespace std;

int n , m;
char Array[30][30];

void solve( int i , int j , char val)
{
    if( i < 0 || j < 0 || i >= n ||j >= m )
        return;

    if( Array[i][j] != '?' )
        return;

    Array[i][j] = val;

    solve( i + 1 , j , val);
    solve( i - 1 , j , val);
    //column
}

void solve2( int i , int j , char val)
{

    if( i < 0 || j < 0 || i >= n ||j >= m )
        return;

    if( Array[i][j] != '?' )
        return;

    Array[i][j] = val;

    solve2( i  , j + 1 , val);
    solve2( i , j - 1 , val);
    //row
}

int main()
{
    freopen("input.txt" , "r" , stdin);
    freopen("output.txt" , "w" , stdout);

    int t;
    cin>>t;

    for(int tt = 1; tt <= t; tt++)
    {
        cin>>n>>m;

        for(int i = 0 ; i < n ; i++)
        {
            for(int j = 0 ; j < m ; j++)
                cin>>Array[i][j];
        }

        for(int i = 0 ; i < n ; i++)
        {
            for(int j = 0 ; j < m ; j++)
            {
                if(Array[i][j] != '?')
                {
                    char val = Array[i][j];
                    Array[i][j] = '?';
                    solve(i , j , val);
                }
            }
        }

        for(int i = 0 ; i < n ; i++)
        {
            for(int j = 0 ; j < m ; j++)
            {
                if(Array[i][j] != '?')
                {
                    char val = Array[i][j];
                    Array[i][j] = '?';
                    solve2(i , j , val);
                }
            }
        }

        cout<<"Case #"<<tt<<":"<<endl;

        for(int i = 0 ; i < n ; i++)
        {
            for(int j = 0 ; j < m ; j++)
                cout<<Array[i][j];
            cout<<endl;
        }
    }
    return 0;
}
