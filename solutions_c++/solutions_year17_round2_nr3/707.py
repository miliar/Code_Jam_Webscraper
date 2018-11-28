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
    int n, q;

    vector<long long> hdist;
    vector<long long> hspeed;
    vector<pair<int, int>> queries;
    vector<vector<long long>> adjm;

	void input()
    {
        cin >> n >> q;
        for (int i = 0; i < n; i++)
        {
            long long a, b;
            cin >> a >> b;
            hdist.push_back(a);
            hspeed.push_back(b);
        }
        adjm.resize(n, vector<long long>(n));
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n; j++)
            {
                cin >> adjm[i][j];
            }
        }
        for (int i = 0; i < q; i++)
        {
            int a, b;
            cin >> a >> b;
            queries.push_back({a, b});
        }
    }
    vector<double> answers;
    void solve(int begin, int end)
    {
        begin--;
        end--;

        vector<bool> went(n, false);
        vector<double> best(n, numeric_limits<double>::max());
        set<pair<double, int>> s;
        s.insert({0, begin});
        best[begin] = 0;

        while (s.size())
        {
            double dist = s.begin()->first;
            int current = s.begin()->second;
            s.erase(s.begin());
            if (went[current])
            {
                continue;
            }
            went[current] = true;
            for (int next = 0; next < n; next++)
            {
                if (went[next])
                {
                    continue;
                }
                if (adjm[current][next] == -1)
                {
                    continue;
                }
                if (adjm[current][next] > hdist[current])
                {
                    continue;
                }
                auto cost = dist + (double)adjm[current][next] / (double)hspeed[current];
                if (best[next] > cost)
                {
                    s.erase({best[next], next});
                    best[next] = cost;
                    s.insert({best[next], next});
                }
            }
        }
        answers.push_back(best[end]);
    }
    void process()
    {
        for (int k = 0; k < n; k++)
        {
            for (int i = 0; i < n; i++)
            {
                for (int j = 0; j < n; j++)
                {
                    if (adjm[i][k] == -1 || adjm[k][j] == -1)
                    {
                        continue;
                    }
                    auto next = adjm[i][k] + adjm[k][j];
                    if (adjm[i][j] == -1 || adjm[i][j] > next)
                    {
                        adjm[i][j] = next;
                    }
                }
            }
        }
        for (int i = 0; i < q; i++)
        {
            solve(queries[i].first, queries[i].second);
        }
    }
	void output()
    {
        for (auto a : answers)
        {
            printf("%.9lf ", a);
        }
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
