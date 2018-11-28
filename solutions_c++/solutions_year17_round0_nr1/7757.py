#include <iostream>
#include <string>
#include <queue>
#include <vector>
using namespace std;


int to[2][2] = {{0, -1}, {-1, 0}};
int dp[16][16];
int result, n, r, c;
string a;
int b;

void check()
{
    int count = 0;
    for(int i = 0; i < r; i++)
    {
        for(int j = 0; j < c; j++)
        {
            if(dp[i][j])
            {
                for(int k = 0; k < 2; k++)
                {
                    int ii = i + to[k][0];
                    int jj = j + to[k][1];
                    if(ii >= 0 && ii < r && jj >= 0 && jj < c && dp[ii][jj])
                        count++;
                }
            }
        }
    }
    result = min(result, count);
}
void DFS(int i, int count)
{
    if(count == n)
    {
        check();
    }
    else
    {
        for(int j = i; j < r*c; j++)
        {
            dp[j/c][j%c] = 1;
            DFS(j+1, count+1);
            dp[j/c][j%c] = 0;
        }
    }
}
int main() {
    int T;
    cin>>T;
    int case_number = 1;
    while(T--)
    {
        cin>>a>>b;
        result = 0;
        for (int i = 0; i <= a.length()-b; i++) {
            if (a[i] == '-') {
                result++;
                for (int j = i; j < i+b; j++) {
                    if (a[j] == '-') {
                        a[j] = '+';
                    } else {
                        a[j] = '-';
                    }
                }
            }
        }
        int i;
        for (i = a.length()-b+1; i < a.length(); i++) {
            if (a[i] == '-') {
                cout<<"Case #"<<case_number++<<": "<<"IMPOSSIBLE"<<endl;
                break;
            }
        }
        if (i == a.length()) {
            cout<<"Case #"<<case_number++<<": "<<result<<endl;
        }
    }
}
