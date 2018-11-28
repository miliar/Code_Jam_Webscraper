#include <bits/stdc++.h>
#define pb push_back
#define f first
#define s second
#define ll long long
#define pii pair<int,int>
#define pll pair<ll,ll>
#define pdd pair<double,double>
using namespace std;
int n, m;
char a[50][50];
void _main()
{
    cin >> n >> m;
    for(int i = 0; i < n; i++)
    for(int j = 0; j < m; j++)cin >> a[i][j];
    int idx = 0, col = 0;
    for(int i = 0; i < n; i++)
    {
        for(int j = 0; j < m; j++)if(a[i][j] != '?')
        {
            idx = i;
            break;
        }
    }
    for(int j = 0; j < m; j++)if(a[idx][j] != '?')
    {
        col = j;
        break;
    }
    //cur row
    char c = a[idx][col];
    for(int j = col-1; j >= 0; j--)if(a[idx][j] == '?')a[idx][j] = c;
    for(int j = col+1; j < m; j++)
    {
        if(a[idx][j] == '?')a[idx][j] = c;
        else c = a[idx][j];
    }
    //up
    for(int i = idx-1; i >= 0; i--)
    {
        col = -1;
        for(int j = 0; j < m; j++)if(a[i][j] != '?')
        {
            col = j;
            break;
        }
        if(col != -1)
        {
            c = a[i][col];
            for(int j = col-1; j >= 0; j--)if(a[i][j] == '?')a[i][j] = c;
            for(int j = col+1; j < m; j++)
            {
                if(a[i][j] == '?')a[i][j] = c;
                else c = a[i][j];
            }
        }
        else
        {
            for(int j = 0; j < m; j++)a[i][j] = a[i+1][j];
        }
    }
    //down
    for(int i = idx+1; i < n; i++)
    {
        col = -1;
        for(int j = 0; j < m; j++)if(a[i][j] != '?')
        {
            col = j;
            break;
        }
        if(col != -1)
        {
            c = a[i][col];
            for(int j = col-1; j >= 0; j--)if(a[i][j] == '?')a[i][j] = c;
            for(int j = col+1; j < m; j++)
            {
                if(a[i][j] == '?')a[i][j] = c;
                else c = a[i][j];
            }
        }
        else
        {
            for(int j = 0; j < m; j++)a[i][j] = a[i-1][j];
        }
    }
}
int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int tt; cin >> tt;
    for(int i = 1; i <= tt; i++)
    {
        _main();
        cout << "Case #" << i << ": \n";
        for(int j = 0; j < n; j++)
        {
            for(int k = 0; k < m; k++)cout << a[j][k];
            cout << "\n";
        }
    }
    return 0;
}
