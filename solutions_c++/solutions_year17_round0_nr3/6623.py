#include <iostream>
#include <algorithm>
#include <set>
#include <vector>
#include <future>
#include <functional>
#include <string>
#include <limits>
#include <climits>
#include <map>
#include <list>
#include <numeric>
#include <cstdio>
#include <cstring>

using namespace std;

struct TestCase
{
    int n, k;
    vector<bool> rooms;

	void input()
    {
        cin >> n >> k;
    }
    void enter(int &bestMinLR, int &bestMaxLR)
    {
        bestMinLR = numeric_limits<int>::min();
        bestMaxLR = numeric_limits<int>::min();
        int bestI;

        for (int i = 1; i <= n; i++)
        {
            if (rooms[i])
            {
                continue;
            }
            int l = 0;
            for (int t = i - 1; !rooms[t]; l++, t--);
            int r = 0;
            for (int t = i + 1; !rooms[t]; r++, t++);

            int minLR = min(l, r);
            int maxLR = max(l, r);
            if (bestMinLR < minLR || (bestMinLR == minLR && bestMaxLR < maxLR))
            {
                bestMinLR = minLR;
                bestMaxLR = maxLR;
                bestI = i;
            }
        }
        rooms[bestI] = true;
    }
    
    int minLR, maxLR;

	void process()
    {
        rooms = vector<bool>(n + 2);
        rooms.front() = rooms.back() = true;
        for (int i = 0; i < k; i++)
        {
            enter(minLR, maxLR);
        }
    }
	void output()
    {
        cout << maxLR << " " << minLR;
    }
};

int main()
{
	int t;
	cin >> t;

	vector<TestCase> tc(t);
	vector<future<void>> f;
	for (int i = 0; i < t; i++) tc[i].input();
	for (int i = 0; i < t; i++)
		f.push_back(async(launch::async,
			[&](int p){ tc[p].process(); }, i));
	for (int i = 0; i < t; i++) f[i].wait();
	for (int i = 0; i < t; i++)
	{
		cout << "Case #" << i + 1 << ": ";
		tc[i].output();
		cout << endl;
	}
	return 0;
}
