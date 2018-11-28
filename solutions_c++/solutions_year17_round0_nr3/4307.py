#include <fstream>
#include <algorithm>
#include <vector>
#include <set>
#include <string>
#include <queue>
#include <functional>

using namespace std;
using llong = long long;

struct segment
{
	llong start, end;

	segment(llong start, llong end) : start(start), end(end)
	{ }

	llong length() const { return end - start; }

	llong center() const { return start + length() / 2; }
	
	friend bool operator>(const segment& a, const segment& b)
	{
		return a.length() < b.length() || a.length() == b.length() && a.start > b.start;
	}
};

int main()
{
	ifstream in("input.txt");
	ofstream out("output.txt");

	int t;
	in >> t;

	for (auto tcase = 1; tcase <= t; tcase++)
	{
		llong n, k;
		in >> n >> k;

		priority_queue<segment, vector<segment>, greater<segment>> segments;
		segments.push(segment(0, n - 1));
		
		for (auto i = 0; i < k; i++)
		{
			auto seg = segments.top();
			segments.pop();

			auto center = seg.center();
			auto minDist = center - seg.start;
			auto maxDist = seg.end - center;

			if (minDist > 0)
				segments.push(segment(seg.start, center - 1));
			if (maxDist > 0)
				segments.push(segment(center + 1, seg.end));
			
			if (i == k - 1)
			{
				out << "Case #" << tcase << ": " << maxDist << " " << minDist << endl;
			}
		}
	}
}