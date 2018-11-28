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
    string cakes;
    int k;
    string answer = "0";

	void input()
    {
        cin >> cakes >> k;
    }
    void flip(int i)
    {
        for (int j = 0; j < k; j++)
        {
            cakes[i + j] = cakes[i + j] == '-' ? '+' : '-';
        }
        answer = to_string(stoi(answer) + 1);
    }
	void process()
    {
        for (int i = 0; i < cakes.length(); i++)
        {
            if (i + k > cakes.length())
            {
                break;
            }
            if (cakes[i] == '-')
            {
                flip(i);
            }
        }
        for (int i = 0; i < cakes.length(); i++)
        {
            if (cakes[i] == '-')
            {
                answer = "IMPOSSIBLE";
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
