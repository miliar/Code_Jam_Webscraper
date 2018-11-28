//In the name of God
//-----gmmj

#include <cstdio>
#include <iostream>
#include <cmath>
#include <cstring>
#include <cstdlib>
#include <vector>
#include <string>
#include <algorithm>
#include <queue>
#include <deque>
#include <set>
#include <stack>
#include <map>
#include <sstream>
#include <ctime>
#include<iomanip>
#include<ctime>

#define Time printf("\nTime : %.3lf s.\n", clock()*1.0/CLOCKS_PER_SEC);
#define For(J,R,K) for(int J=R;J<K;++J)
#define Rep(I,N) For(I,0,N)
#define MP make_pair
#define ALL(X) (X).begin(),(X).end()
#define SF scanf
#define PF printf
#define pii pair<long long,long long>
#define pdd pair<double , double>
#define Sort(v) sort(ALL(v))
#define Test freopen("a.in","r",stdin);
#define Testout freopen("a.out","w",stdout);
#define pb push_back
#define Set(a,n) memset(a,n,sizeof(a))
#define MAXN 1000+9
#define EPS 1e-15
#define inf 1ll<<62

typedef long long ll;

using namespace std;

ll n , d;



int main()
{
    //Test;
    //Testout;
    int tc;
    cin >> tc;
    For(cas , 1 , tc+1)
    {
        cin >> d >> n;
        double mn = -1;
        double x , v;
        Rep(i , n)
        {
            cin >> x >> v;
            mn = max(mn , (d - x)/v);
        }
        cout << "Case #" << cas << ": " ;
        cout << fixed << setprecision(6) << (d / mn) << endl;

    }
	return 0;
}

