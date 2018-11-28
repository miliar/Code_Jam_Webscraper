
#define PROBLEM_NAME "B"
#define PROBLEM_SMALL_INPUT "-small-attempt1"
#define PROBLEM_LARGE_INPUT "-large"

#include <vector>
#include <list>
#include <algorithm>

using namespace std;

struct XX
{
	char type;
	int count;

	XX(char ch, int i) : type(ch), count(i) {}
};

string* pp;

bool comp(const XX& l, const XX& r)
{
	if (l.count == r.count)
	{
		int ll = pp->rfind(l.type);
		int rr = pp->rfind(r.type);
		if (ll == string::npos && rr == string::npos)
			return false;
		if (ll == string::npos)
			return false;
		if (rr == string::npos)
			return true;
		if (l.type == (*pp)[0] && r.type != (*pp)[0])
			return true;
		if (l.type != (*pp)[0] && r.type == (*pp)[0])
			return false;
		return ll > rr;
	}
	else
	{
		return l.count > r.count;
	}
}

int main(int argc, char* argv[])
{
//	set_fio(PROBLEM_NAME ".txt");
//	set_fio(PROBLEM_NAME ".txt", PROBLEM_NAME ".out.txt");
//	set_fio(PROBLEM_NAME PROBLEM_SMALL_INPUT ".in");
	set_fio(PROBLEM_NAME PROBLEM_SMALL_INPUT ".in", PROBLEM_NAME PROBLEM_SMALL_INPUT ".out.txt");
//	set_fio(PROBLEM_NAME PROBLEM_LARGE_INPUT ".in");
//	set_fio(PROBLEM_NAME PROBLEM_LARGE_INPUT ".in", PROBLEM_NAME PROBLEM_LARGE_INPUT ".out.txt");

	int T;
	fin >> T;
	for (int cases=1; cases<=T; ++cases)
	{
		int N, R, O, Y, G, B, V;
		fin >> N >> R >> O >> Y >> G >> B >> V;
		int total = R + O + Y + G + B + V;

		// small set : O = G = V = 0. only consider R, Y, B
		if (R > total/2 || Y > total/2 || B > total/2)
		{
			fout << "Case #" << cases << ": IMPOSSIBLE" << endl;
			continue;
		}

		vector<XX> x;
		x.push_back(XX('R', R));
		x.push_back(XX('Y', Y));
		x.push_back(XX('B', B));

		string s;
		s.resize(N);
		pp = &s;
		for (int i=0; i<N; ++i)
		{
			if (!x.empty())
			{
				stable_sort(x.begin(), x.end(), comp);
				int index = 0;
				if (i > 0)
				{
					if (x[0].type == s[i-1])
						index = 1;
				}

				XX xx = x[index];
				x.erase(x.begin() + index);

				s[i] = xx.type;
				xx.count--;
				if (xx.count > 0)
				{
					//x.insert(x.begin(), xx);
					x.push_back(xx);
				}
			}
			else
			{
				s.resize(i);
			}
		}

		fout << "Case #" << cases << ": " << s << endl;

		for (int i=1; i<s.size(); ++i)
		{
			if (s[i] == s[i-1])
			{
				fout << "-------- (" << s.size() << ") conflict at " << i << endl;
				break;
			}
		}

		if (s[0] == s[s.size()-1])
		{
			fout << "-------- (" << s.size() << ") head and tail are same" << endl;
		}
	}

	return 0;
}
