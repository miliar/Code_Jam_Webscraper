#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <cstring>
#include <string>
#include <queue>
#include <set>
#include <map>
#include <bitset>
#include <cmath>
#include <stack>
#include <ctime>
#include <unordered_map>
#include <unordered_set>
#include <list>
#include <cassert>
using namespace std;

const int maxn=1e5+10;
const long long inf = 1000000000000000000LL;
int t;

int main(){
    freopen("input.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cin>>t;
    for(int ii=0;ii<t;ii++){
            int r, c;
        cin>>r>>c;
        char a[30][30];
        for(int j = 0; j<r; j++)
            for(int k = 0; k<c; k++)
                cin>>a[j][k];
        for(int j = 0; j<r; j++)
        {
            for(int k = 0; k<c; k++)
            {
                if(a[j][k]!='?')
                {
                    for(int p = k + 1; p<c; p++)
                        if(a[j][p] == '?')
                            a[j][p] = a[j][k];
                        else
                            break;
                    for(int p = k - 1; p>=0; p--)
                        if(a[j][p] == '?')
                            a[j][p] = a[j][k];
                        else
                            break;
                }
            }
        }
        for(int j = 0; j<(r - 1); j++)
        {
            for(int k = 0; k<c; k++)
                if(a[j][k] != '?' && a[j + 1][k] == '?')
                    a[j + 1][k] = a[j][k];
        }
        for(int j = r - 1; j>0; j--)
        {
            for(int k = 0; k<c; k++)
                if(a[j][k] != '?' && a[j - 1][k] == '?')
                    a[j - 1][k] = a[j][k];
        }
        cout<<"Case #"<<ii + 1<<":"<<endl;
        for(int j = 0; j<r; j++)
        {
            for(int k = 0; k<c; k++)
                cout<<a[j][k];
            cout<<endl;
        }
    }

    return 0;
}