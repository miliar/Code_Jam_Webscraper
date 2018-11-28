#include<iostream>
#include<cstdio>
#include<queue>
using namespace std;

char a[30][30];

int main()
{
    freopen("A-large.in.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++)
    {
        cout << "Case #" << t << ":" << endl;
        int n, m;
        cin >> n >> m;
        for (int i = 0; i < n; i++)
            for(int j = 0; j < m; j++)
                cin >> a[i][j];
        for (int i = 0; i < n; i++)
        {
            for (int j = 1; j < m; j++)
                if (a[i][j] == '?')
                    a[i][j] = a[i][j-1];
            for (int j = m-2; j >= 0; j--)
                if (a[i][j] == '?')
                    a[i][j] = a[i][j+1];
        }
        for (int j = 0; j < m; j++)
        {
            for (int i = 1; i < n; i++)
                if (a[i][j] == '?')
                    a[i][j] = a[i-1][j];
            for (int i = n-2; i >= 0; i--)
                if (a[i][j] == '?')
                    a[i][j] = a[i+1][j];
        }
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < m; j++)
                cout << a[i][j];
            cout << endl;
        }
    }
    return 0;
}
