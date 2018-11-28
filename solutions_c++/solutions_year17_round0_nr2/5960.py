#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;
typedef long long ll;

bool OK(ll i)
{
	int m = i % 10;
	i = i / 10;
	while (i > 0)
	{
		int t = i % 10;
		if (t > m) return false;
		m = t;
		i = i / 10;
	}
	return true;
}

ll nnext(ll i,int j)
{
	ll t = i;
	int k = j;
	while (k-- > 0) t = t / 10;
	t = t - 1;
	k = j;
	while (k-- > 0) t = t * 10 + 9;
	return t;
}

int main()
{
	//freopen("B-small-attempt0.in","r",stdin);freopen("B-small-attempt0.out","w",stdout);
	freopen("B-large.in","r",stdin);freopen("B-large.out","w",stdout);
	//freopen("A.in", "r", stdin); freopen("A.out", "w", stdout);
	int testcase;




	scanf("%d", &testcase);
	for (int case_id = 1; case_id <= testcase; case_id++)
	{
		ll ans = 0;
		ll n;
		printf("Case #%d: ", case_id);
		cin >> n;
		int i = 1;
		while (1)
		{
			if (OK(n))
			{
				cout << n;
				printf("\n");
				break;
			}
			n = nnext(n,i);
			i++;
		}
	}
	return 0;
}