#include <fstream>
#include <iostream>
#include <string>

using namespace std;

//#define SMALL_INPUT
#define LARGE_INPUT

#if defined(SMALL_INPUT)
std::ifstream fin("D:\\develop\\GCJ\\data\\small.in");
std::ofstream fout("D:\\develop\\GCJ\\data\\small.out");
#define gin fin
#define gout fout
#elif defined(LARGE_INPUT)
std::ifstream fin("D:\\develop\\GCJ\\data\\large.in");
std::ofstream fout("D:\\develop\\GCJ\\data\\large.out");
#define gin fin
#define gout fout
#else
#define gin cin
#define gout cout
#endif

class Solver
{
public:
	string Solve(string s, char cap = '0')
	{
		if (s.empty() || s[0] < cap) return "";

		string sub = s.substr(1, s.length() - 1);
		string sub_res = Solve(sub, s[0]);

		string s1 = s[0] + sub_res;
		int64_t i1 = atoll(s1.c_str());

		string s2 = s;
		s2[0] = s2[0] - 1;
		for (size_t i = 1; i < s2.length(); ++i)
			s2[i] = '9';

		int64_t i2 = atoll(s2.c_str());
		if (s2[0] < cap) i2 = -1;

		return i1 > i2 ? s1 : s2;
	}
};

int main()
{
	int t;
	gin >> t;

	for (int i = 1; i <= t; ++i)
	{
		string s;
		gin >> s;

		Solver sovler;
		string ret = sovler.Solve(s);
		if (ret[0] == '0') ret.erase(ret.begin());

		gout << "Case #" << i << ": ";
		gout << ret << "\n";
	}

	return 0;
}