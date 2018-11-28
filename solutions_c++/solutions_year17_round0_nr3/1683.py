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
    freopen("Clarge.in","r",stdin);
    freopen("Clarge.out","w",stdout);
    cin>>T;
    while(T--)
    {
        test ++;
        printf("Case #%d: ",test);
        LL pw=1,k,n,x,y;
        cin>>n>>k;
        while(pw < k)
        {
            k-=pw;
            n-=pw;
            pw *=2;
        }
        x = n/pw;
        if(k<= n%pw)
            x++;
        cout << x/2 <<' ' <<(x-1)/2<<endl;
    }
    return 0;
}
// davidlee1999WTK 2017/
// ios::sync_with_stdio(false);
//#pragma comment(linker, "/STACK:102400000,102400000") compiler c++,not g++
/*

*/
