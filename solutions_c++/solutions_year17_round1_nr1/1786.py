#include <cstdio>
#include <iostream>
#include <vector>
#include <string>
#include <queue>
#include <cmath>
#include <climits>
#include <algorithm>
#include <cstring>

using namespace std;

int t;
int n, m;
bool check[25][25];

int main(void)
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large-output.txt", "w", stdout);
    cin >> t;
    for(int z=1;z<=t;z++)
    {
        string str[25];
        cin >> n >> m;
        for(int i=0;i<n;i++)
        {
            cin >> str[i];
        }

        for(int i=0;i<n;i++)
        {
            for(int j=0;j<m;j++)
            {
                if(str[i][j] != '?')
                {
                    int p = j+1;
                    while(p < m && str[i][p] == '?')
                    {
                        str[i][p] = str[i][j];
                        p++;
                    }
                    p = j-1;
                    while(p>=0 && str[i][p] == '?')
                    {
                        str[i][p] = str[i][j];
                        p--;
                    }
                }
            }
        }

        for(int i=0;i<n;i++)
        {
            for(int j=0;j<m;j++)
            {
                if(str[i][j] != '?')
                {
                    int p = i+1;
                    while(p < n && str[p][j] == '?')
                    {
                        str[p][j] = str[i][j];
                        p++;
                    }
                    p = i-1;
                    while(p >= 0 && str[p][j] == '?')
                    {
                        str[p][j] = str[i][j];
                        p--;
                    }
                }
            }
        }

        printf("Case #%d:\n", z);
        for(int i=0;i<n;i++)
        {
            cout << str[i] <<'\n';
        }

    }

}
