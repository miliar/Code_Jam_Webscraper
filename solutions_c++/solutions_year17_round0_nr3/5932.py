#include<fstream>
#include <string>
#include <vector>
#include <queue>
using namespace std;

struct Space
{
	long long pos, dist;
	Space(long long position, long long distance) : pos(position), dist(distance) {}
};

class Comp
{
public:
	bool operator() (const Space& a, const Space& b)
	{
		if (a.dist != b.dist)
			return a.dist < b.dist;
		return a.pos > b.pos;
	}
};

int main()
{
	ifstream fin("in.txt");
	ofstream fout("out.txt");
	int T;
	fin >> T;
	for (int t = 0; t < T; t++)
	{
		long long n, p;
		fin >> n >> p;
		long long min, max;
		priority_queue<Space, vector<Space>, Comp> qu;
		qu.push(Space(0, n));
		while (p--)
		{
			Space s = qu.top();
			qu.pop();
			s.dist--;
			Space left(s.pos, s.dist / 2);
			Space right(s.pos + 1 + left.dist, s.dist - left.dist);
			if (left.dist > 0)
				qu.push(left);
			if (right.dist > 0)
				qu.push(right);

			min = left.dist;
			max = right.dist;
		}

		fout << "Case #" << t + 1 << ": " << max << " " << min << endl;
	}
}