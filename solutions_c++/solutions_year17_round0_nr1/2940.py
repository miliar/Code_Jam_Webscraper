#include <cstdio>
#include <cstdlib>
#include <string>
#include <algorithm>
#include <map>
#include <set>
#include <vector>
#include <queue>
#include <iostream>

using namespace std;

int testCount;

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);	
	cin >> testCount;
	for (int testNumber = 1; testNumber <= testCount; testNumber++)
	{
		int ans = 0;
		int k;
		queue<int> q;
		string s;
		cin >> s >> k;
		bool flip = false;
		for(int i = 0; i < s.size(); i++)
		{
			if (q.size() > 0 && (i - q.front()>= k))
			{
				q.pop();
				flip = !flip;
			}
			if ((s[i] == '+' && flip)
				|| (s[i] == '-' && !flip))
			{
				if ((s.size() - i) >= k)
				{
					q.push(i);
					flip = !flip;
					ans++;
				}
				else
				{
					ans = -1;
					break;
				}
			}
		}
		if (ans != -1)
			printf("Case #%d: %d\n", testNumber, ans);
		else
			printf("Case #%d: IMPOSSIBLE\n", testNumber);
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}
