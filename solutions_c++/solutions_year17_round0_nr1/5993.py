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



int main()
{
	//freopen("A-small-attempt0.in","r",stdin);freopen("A-small-attempt0.out","w",stdout);
	//freopen("2017A.in", "r", stdin); freopen("2017A.out", "w", stdout);
	freopen("A-large.in","r",stdin);freopen("A-large.out","w",stdout);
	//freopen("C-large-practice.in", "r", stdin); freopen("C-large-practice.out", "w", stdout);
	int testcase;


	scanf("%d", &testcase);
	for (int case_id = 1; case_id <= testcase; case_id++)
	{
		ll ans = 0;
		printf("Case #%d: ", case_id);
		string s;
		int k;
		bool ok = true;
		cin>>s;
		cin >> k;
		for (int i = 0; i < s.length(); i++)
		{
			if (i <= s.length() - k)
			{
				if (s[i] == '-')
				{
					ans++;
					for (int j = 0; j < k; j++){
						if (s[i + j] == '-')
							s[i + j] = '+';
						else
							s[i + j] = '-';
					}
				}
			}
			else
			{
				if (s[i] == '-')
				{
					ok = false;
					break;
				}
			}
		}
		if (ok)
			cout << ans;
		else
			cout << "IMPOSSIBLE";
		printf("\n");
	}
	return 0;
}