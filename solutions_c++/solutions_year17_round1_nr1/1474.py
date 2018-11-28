#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <unordered_map>
#include <unordered_set>
#include <queue>
#include <stack>
#include <string>
#include <string.h>
#include <math.h>

using namespace std;

// typedefs
typedef long long ll;
typedef unsigned long long ull;
typedef pair <int,int> pii;

// constants
const double PI = 2.0*acos(0.0);
const double EPS = 1e-9;  // too small/big?????

// magic
int N,M;
char cake[50][50];
char ans[50][50];

int solve()
{
    for(int i=0;i<N;i++) for(int j=0;j<M;j++)
        ans[i][j] = cake[i][j];
    for(int i=0;i<N;i++)
    {
        for(int j=0;j<M;j++)
        {
            if(cake[i][j] != '?')
            {
                for(int k=i-1;k>=0;k--)
                {
                    if(ans[k][j]=='?')
                        ans[k][j] = cake[i][j];
                    else
                        break;
                }
                for(int k=i+1;k<N;k++)
                {
                    if(ans[k][j]=='?')
                        ans[k][j] = cake[i][j];
                    else
                        break;
                }
            }
        }
    }
    for(int j=0;j<M;j++)
    {
        if(ans[0][j]!='?')
            continue;
        int col;
        if(!j)
        {
            for(col=j+1;col<M;col++)
            {
                if(ans[0][col]!='?')
                    break;
            }
            if(col == M)
                cerr<<"FOOK!"<<endl;
        }
        else
            col = j-1;
        for(int i=0;i<N;i++)
            ans[i][j] = ans[i][col];
    }
    for(int i=0;i<N;i++)
        cout<<ans[i]<<"\n";
    return 0;
}

int main()
{
    int T;
    cin>>T;
    for(int tc=1; tc<=T; tc++)
    {
        cerr << "Running test #" << tc << "..." << endl;
        cin>>N>>M;
        for(int i=0;i<N;i++)
        {
            cin>>cake[i];
            for(int j=0;j<M;j++)
                ans[i][j]='?';
            ans[i][M] = 0;
        }

        printf("Case #%d:\n", tc);
        solve();
    }
    return 0;
}