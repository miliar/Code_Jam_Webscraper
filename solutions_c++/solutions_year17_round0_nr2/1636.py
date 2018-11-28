#include<cstdio>
#include<iostream>
#include<algorithm>
#include<cstring>
#include<cmath>
#include<vector>
#include<queue>
#include<map>
#include<set>
#include<stack>
#include<cstdlib>
#include<string>
#include<bitset>
#include<iomanip>
#include<deque>
#include<utility>
#include<functional>
#include<sstream>
#define INF 1000000000
#define fi first
#define se second
#define N 100005
#define P 1000000007
#define debug(x) cerr<<#x<<"="<<x<<endl
#define MP(x,y) make_pair(x,y)
using namespace std;
typedef long long LL;
typedef pair<int,int> pii;
int main()
{
    int T;
    int test = 0;
    freopen("Blarge.in","r",stdin);
    freopen("Blarge.out","w",stdout);
    cin>>T;
    while(T--)
    {
        test ++;
        int flag=1;
        printf("Case #%d: ",test);
        string x,y;
        cin>>x;
        y = x;
        while(flag)
        {
            flag = 0;
            for(int i = 0;i < (int)x.size()-1;i++)
                if(y[i]>y[i+1])
                {
                    flag = 1;
                    y[i]--;
                    for(int j=i+1;j<x.size();j++)
                        y[j]='9';
                    for(int j = i;j>=0;j--)
                        if(y[j]=='0'-1)
                            y[j-1]--,y[j]='9';
                    //cout<<y<<endl;
                    break;
                }
        }
        if(y[0]=='0')
            cout<<y.substr(1,y.size()-1)<<endl;
        else cout<<y<<endl;
    }
    return 0;

}
// davidlee1999WTK 2017/
// ios::sync_with_stdio(false);
//#pragma comment(linker, "/STACK:102400000,102400000") compiler c++,not g++
/*

*/
