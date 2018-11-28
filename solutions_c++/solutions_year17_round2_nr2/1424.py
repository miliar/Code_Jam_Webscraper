#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
#include <queue>

using namespace std;

int main(int argc, char** argv)
{
	string inFile(argv[1]);
	string outFile(inFile + ".out");
	ifstream in(inFile);
	ofstream out(outFile);

	int ts; in >> ts;
	for (int t = 1; t <= ts; ++t)
	{
		int n; in >> n;
		int r, o, y, g, b, v; in >> r >> o >> y >> g >> b >> v;
		int m = 3;
		priority_queue<pair<int, char> > queue;
		queue.push({r, 'R'});
		queue.push({y, 'Y'});
		queue.push({b, 'B'});
		string res;
		for (int i = 0; i < n; i++)
		{
			pair<int, char> cur = queue.top();
			queue.pop();
			if (!res.empty() && i > 0 && res[i - 1] == cur.second && !queue.empty())
			{
				pair<int, char> cur2 = queue.top();
				queue.pop();
				queue.push(cur);
				cur = cur2;
			}
			if (cur.first > 0)
			{
				res.push_back(cur.second);
				cur.first--;
			}
			queue.push(cur);
		}
		if (res[0] == res[n - 1] && n > 2) swap(res[n - 1], res[n - 2]);
		bool ok = res.size() == n && res[0] != res[n - 1];
		for (int i = 1; ok && i < n; i++) ok &= res[i] != res[i - 1];
		if (!ok) res = "IMPOSSIBLE";
		out << "Case #" << t << ": " << res << endl;
	}
	return 0;
}
