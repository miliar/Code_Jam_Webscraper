
#define PROBLEM_NAME "A"
#define PROBLEM_SMALL_INPUT "-small-attempt1"
#define PROBLEM_LARGE_INPUT "-large"

#include <algorithm>
#include <set>
#include <vector>

using namespace std;


bool CountFlip(int& count, string s, int K)
{
	if (s.size() < K)
		return false;
	else if (s.size() == K)
	{
		int cnt = std::count(s.begin(), s.end(), '+');
		if (cnt == K)
		{
			count = 0;
			return true;
		}
		else if (cnt == 0)
		{
			count = 1;
			return true;
		}
		else
			return false;
	}

	bool front_possible, back_possible;
	int front_count = 0, back_count = 0;

	if (s[0] == '+')
	{
		front_possible = CountFlip(front_count, s.substr(1), K); // 1st char flipped. start from 2nd char.
	}
	else // if (s[0] == -)
	{
		string s2 = s;
		// flip first K cakes.
		for (size_t i=0; i<K; ++i)
		{
			if (s2[i] == '+') s2[i] = '-';
			else if (s2[i] == '-') s2[i] = '+';
		}
		front_possible = CountFlip(front_count, s2.substr(1), K); // 1st char flipped. start from 2nd char.
		front_count++; // my flip in this func
	}

	if (s[s.size()-1] == '+')
	{
		back_possible = CountFlip(back_count, s.substr(0, s.size()-1), K); // last char flipped. end just before last char.
	}
	else // if (s[s.size()-1] == -)
	{
		string s2 = s;
		for (size_t i=0; i<K; ++i)
		{
			if (s2[s2.size()-1-i] == '+') s2[s2.size()-1-i] = '-';
			else if (s2[s2.size()-1-i] == '-') s2[s2.size()-1-i] = '+';
		}
		back_possible = CountFlip(back_count, s2.substr(0, s2.size()-1), K);
		back_count++; // my flip in this func
	}

	if (front_possible && back_possible)
	{
		count = min(front_count, back_count);
		return true;
	}
	else if (front_possible)
	{
		count = front_count;
		return true;
	}
	else if (back_possible)
	{
		count = back_count;
		return true;
	}
	else
		return false;
}

int main(int argc, char* argv[])
{
//	set_fio(PROBLEM_NAME ".txt");
//	set_fio(PROBLEM_NAME PROBLEM_SMALL_INPUT ".in");
	set_fio(PROBLEM_NAME PROBLEM_SMALL_INPUT ".in", PROBLEM_NAME PROBLEM_SMALL_INPUT ".out.txt");
//	set_fio(PROBLEM_NAME PROBLEM_LARGE_INPUT ".in");
//	set_fio(PROBLEM_NAME PROBLEM_LARGE_INPUT ".in", PROBLEM_NAME PROBLEM_LARGE_INPUT ".out.txt");

	int T;
	fin >> T;
	for (int cases=1; cases<=T; ++cases)
	{
		string S;
		int K;
		fin >> S >> K;

		int count;
		bool possible = CountFlip(count, S, K);

		fout << "Case #" << cases << ": ";
		if (possible)
			fout << count << endl;
		else
			fout << "IMPOSSIBLE" << endl;
	}

	return 0;
}
