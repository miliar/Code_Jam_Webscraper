
#include <iostream>
#include <algorithm>
#include <vector>
#include <stack>
#include <queue>
#include <list>
#include <cstring>
#include <math.h>

using namespace std;

typedef long long int lli;
typedef unsigned long long int ulli;
typedef long double ld;

int main() {

    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int t;
    cin >> t;

    for(int k=1;k<=t;k++)
    {
        int r,c,cnt=0;
        char one;

        cin >> r >> c;

        char a[r+1][c+1];

        for(int i=1;i<=r;i++)
        {
            for(int j=1;j<=c;j++)
            {
                cin >> a[i][j];
                if(a[i][j]!='?')
                {
                    one = a[i][j];
                    cnt++;
                }
            }
        }

        if(cnt==1)
        {
            for(int i=1;i<=r;i++)
            {
                for(int j=1;j<=c;j++)
                {
                    a[i][j] = one;
                }
            }
        }
        else
        {

            for(int i=2;i<=r;i++)
            {
                for(int j=1;j<=c;j++)
                {
                    if(a[i-1][j]!='?' &&  a[i][j]=='?' )
                        a[i][j] = a[i-1][j];
                }
            }

            for(int i=r-1;i>=1;i--)
            {
                for(int j=1;j<=c;j++)
                {
                    if(a[i+1][j]!='?' &&  a[i][j]=='?' )
                        a[i][j] = a[i+1][j];
                }
            }

            for(int i=2;i<=c;i++)
            {
                for(int j=1;j<=r;j++)
                {
                    if(a[j][i-1]!='?'  && a[j][i]=='?')
                        a[j][i] = a[j][i-1];
                }
            }


            for(int i=c-1;i>=1;i--)
            {
                for(int j=1;j<=r;j++)
                {
                    if(a[j][i+1]!='?' && a[j][i]=='?')
                        a[j][i] = a[j][i+1];
                }
            }

        }

        cout << "Case #" << k << ": " << endl;
        for(int i=1;i<=r;i++)
        {
            for(int j=1;j<=c;j++)
            {
                cout << a[i][j];
            }
            cout << "\n";
        }




    }

    return 0;
}


