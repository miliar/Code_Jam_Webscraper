#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>
using namespace std;

#define PB push_back
#define MP make_pair

#define REP(i,n) for(int i=0;i<(n);++i)
#define FOR(i,l,h) for(int i=(l);i<=(h);++i)
#define FORD(i,h,l) for(int i=(h);i>=(l);--i)

#define coutpoint9 setiosflags(ios::fixed)<<setprecision(9)

#define maxn 60
//#define INF 100000000
//#define maxm 1000000
//#define MM 1000000007

//const long double pi = 3.141592653589793238462643383279502884197169399375105820974944592307816406286;

typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<double> VD;
typedef long long LL;
typedef pair<int,int> PII;

double a[maxn];

int main()
{
	//srand((int)time(NULL));
	
	freopen("C-small-1-attempt1.in","r",stdin);
	freopen("output.txt","w",stdout);
	//ios_base::sync_with_stdio(false);
	
	int T;
	scanf("%d",&T);
	FOR(tt,1,T)
	{
		printf("Case #%d: ",tt);
		int n, k;
		cin >> n >> k;
		double U;
		cin >> U;
		FOR(i,1,n)
			cin >> a[i];
		sort(a + 1, a + n + 1);
		a[n+1] = 1.0;
		double h = 0;
		int p = 0;
		FOR(i,1,n)
			if (i < n && (a[i+1] - a[i]) * i <= U)
				U -= (a[i+1] - a[i]) * i;
			else
			{
				h = U / i + a[i];
				p = i;
				break;
			}
		double ans = 1.0;
		FOR(i,1,p)
			ans *= h;
		FOR(i,p+1,n)
			ans *= a[i];
		cout << coutpoint9 << ans << endl;
	}
	
	//fclose(stdin);
	//fclose(stdout);
	return 0;
}
