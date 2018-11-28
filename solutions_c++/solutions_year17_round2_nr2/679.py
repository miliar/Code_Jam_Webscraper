#include <iostream>
#include <algorithm>
#include <set>
#include <vector>
#include <future>
#include <functional>
#include <string>
#include <map>
#include <list>
#include <numeric>
#include <cstdio>
#include <cstring>

using namespace std;

struct TestCase
{
    int n, r, o, y, g, b, v;
	void input()
    {
        cin >> n >> r >> o >> y >> g >> b >> v;
    }
    string answer = "IMPOSSIBLE";
    char Lookup[3];
    void process()
    {
        vector<pair<int, int>> d = {{r, 0}, {b, 1}, {y, 2}};
        for (int i = 0; i < 3; i++)
        {
            int first = d[i].first;
            int second = 0;
            for (int j = 0; j < 3; j++)
            {
                if (i == j) continue;
                second += d[j].first;
            }
            if (first > second)
            {
                return;
            }
        }

        answer = "";
        vector<int> list;

        sort(d.begin(), d.end(), greater<pair<int, int>>());
        Lookup[0] = 0;
        Lookup[1] = 1;
        Lookup[2] = 2;
        for (int i = 0; i < 3; i++)
        {
            Lookup[i] = (Lookup[i] == 0) ? ('R') : (Lookup[i] == 1 ? 'B' : 'Y');
        }

        auto most = max_element(d.begin(), d.end());
        
        auto debug = [&](){};
/*        for (auto k : d) cout << k.first << " " << k.second << " ";
        cout << endl;};*/

        debug();

        int m0 = most->first;
        while (most->first--)
        {
            list.push_back(most->second);
        }
        d.erase(most);

        debug();

        most = max_element(d.begin(), d.end());
        int m1 = most->first;
        auto it = list.begin();
        while (most->first--)
        {
            it++;
            it = list.insert(it, most->second);
            it++;
        }
        d.erase(most);

        debug();

        auto finalize = [&]()
        {
            for (auto i : list)
            {
                answer += Lookup[i];
            }
        };

        if (m0 + m1 == n)
        {
            finalize();
            return;
        }

        most = max_element(d.begin(), d.end());
        int m2 = most->first;
        while (list.size() < m0 + m0 && most->first--)
        {
            it++;
            it = list.insert(it, most->second);
            it++;
        }
        while (most->first--)
        {
            for (int i = 0; i < list.size(); i++)
            {
                int p = i - 1;
                int q = i;
                
                while (p < 0) p += list.size();
                while (q >= list.size()) q -= list.size();

                if (list[p] != most->second && list[q] != most->second)
                {
                    list.insert(list.begin() + q, most->second);
                    break;
                }
            }
        }

        finalize();
    }
	void output()
    {
        cout << answer;
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
