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

#define maxn 1010
//#define INF 100000000
//#define maxm 1000000
//#define MM 1000000007

//const long double pi = 3.141592653589793238462643383279502884197169399375105820974944592307816406286;

typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<double> VD;
typedef long long LL;
typedef pair<int,int> PII;

struct node
{
	int l,r,c;
}a[maxn];

bool cmp(const node &x, const node &y)
{
	return x.l < y.l;
}

bool myfunction (int i, int j) { return (i > j); }

int d1[maxn], d2[maxn];

int solve(int t, int* d, int dn)
{
	int i;
	for (i = 0; t > 0; t -= d[++i]);
	return i;
}

int main()
{
	//srand((int)time(NULL));
	
	freopen("B-small-attempt0.in","r",stdin);
	freopen("output.txt","w",stdout);
	//ios_base::sync_with_stdio(false);
	
	int T;
	scanf("%d",&T);
	FOR(tt,1,T)
	{
		printf("Case #%d: ",tt);
		int n1, n2;
		cin >> n1 >> n2;
		int t1 = 0, t2 = 0;
		FOR(i,1,n1)
		{
			cin >> a[i].l >> a[i].r;
			a[i].c = 1;
			t1 += a[i].r - a[i].l;
		}
		FOR(i,n1+1,n1+n2)
		{
			cin >> a[i].l >> a[i].r;
			a[i].c = 2;
			t2 += a[i].r - a[i].l;
		}
		sort(a + 1, a + n1 + n2 + 1, cmp);
		a[n1+n2+1] = a[1];
		a[n1+n2+1].l += 1440;
		a[n1+n2+1].r += 1440;
		int m1 = n1, m2 = n2;
		int dn1 = 0, dn2 = 0;
		FOR(i,1,n1+n2)
			if (a[i].c == a[i+1].c)
			{
				if (a[i].c == 1)
				{
					d1[++dn1] = a[i+1].l - a[i].r;
					t1 += a[i+1].l - a[i].r;
					m1--;
				}
				else
				{
					d2[++dn2] = a[i+1].l - a[i].r;
					t2 += a[i+1].l - a[i].r;
					m2--;
				}
			}
		//cout << "m1=" << m1 << " m2=" << m2 << endl;
		if (t1 <= 720 && t2 <= 720)
		{
			cout << m1 * 2 << endl;
			continue;
		}
		sort(d1 + 1, d1 + dn1 + 1, myfunction);
		sort(d2 + 1, d2 + dn2 + 1, myfunction);
		if (t1 <= 720)
			cout << (m1 + solve(720 - t1, d2, dn2)) * 2 << endl;
		else
			cout << (m1 + solve(720 - t2, d1, dn1)) * 2 << endl;
	}
	
	//fclose(stdin);
	//fclose(stdout);
	return 0;
}
