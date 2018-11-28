#include <bits/stdc++.h>
using namespace std;

string M[30];
int r,c;

int main()
{
    ios_base::sync_with_stdio(false); cin.tie(0);
    int T,ntest=1;
    cin >> T;
    while(T--)
    {
        cin >> r >> c;
        for(int i = 0; i < r; i++)
            cin >> M[i];

        // Down
        for(int i = 0; i < r; i++)
            for(int j = 0; j < c; j++)
                if(M[i][j] != '?')
                {
                    for(int k = i + 1; k < r; k++)
                        if(M[k][j] == '?')
                            M[k][j] = M[i][j];
                        else
                            break;
                }

        // Up
        for(int i = 0; i < r; i++)
            for(int j = 0; j < c; j++)
                if(M[i][j] != '?')
                {
                    for(int k = i - 1; k < r; k--)
                        if(M[k][j] == '?')
                            M[k][j] = M[i][j];
                        else
                            break;
                }

        // Left to Right
        for(int i = 0; i < r; i++)
            for(int j = 1; j < c; j++)
                if(M[i][j] == '?')
                    M[i][j] = M[i][j-1];
        
        // Right to Left
        for(int i = 0; i < r; i++)
            for(int j = c - 2; j >= 0; j--)
                if(M[i][j] == '?')
                    M[i][j] = M[i][j+1];  

        cout << "Case #" << ntest++ << ":" << '\n';
        for(int i = 0; i < r; i++)
            cout << M[i] << '\n';    
    }
    return 0;
} 