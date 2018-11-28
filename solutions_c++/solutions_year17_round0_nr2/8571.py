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
    int n;
    int answer;
	void input()
    {
        cin >> n;
    }
    bool check(int n)
    {
        string s = to_string(n);
        if (s.length() == 1)
        {
            return true;
        }
        for (int i = 1; i < s.length(); i++)
        {
            if (s[i - 1] > s[i])
            {
                return false;
            }
        }
        return true;
    }
    void process()
    {
        for (int i = n; 1 <= i; i--)
        {
            if (check(i))
            {
                answer = i;
                return;
            }
        }
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
