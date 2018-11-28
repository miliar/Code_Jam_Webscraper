#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <map>
#include <ctime>
#include <cmath>
#include <algorithm>
#include <set>
#include <utility>
#include <iomanip> 
#include <queue>

using namespace std;

#define pb push_back

#define N 1010

typedef long long ll;

int n, c, m, p[N], b[N];

int main() {

	//freopen("A-large.in.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	ios::sync_with_stdio(false);

	int t;
	cin >> t;
	int testcase = 0;
	while (t--)	{
		cin >> n >> c >> m;

		vector<int> cntp(n+1,0);
		vector<int> cntb(c+1,0);
		for (int i = 0; i < m; i++)
		{
			cin >> p[i] >> b[i];
			cntp[p[i]]++;
			cntb[b[i]]++;
		}
		
		int r = 0, cumsum = 0;
		for (int i = 1; i <= n; i++)
		{
			cumsum += cntp[i];
			r = max(r,(cumsum+i-1)/i);
		}
		
		for (int i = 1; i <= c; i++)
			r = max(r,cntb[i]);
			
		int pr = 0;
		for (int i = 1; i <= n; i++)
			if (cntp[i] > r)
				pr += cntp[i]-r;
			
		
		testcase++;
		cout << "Case #" << testcase << ": ";
		cout << r << ' ' << pr << endl;
	}

	return 0;
}