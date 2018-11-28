
#define PROBLEM_NAME "B"
#define PROBLEM_SMALL_INPUT "-small-attempt0"
#define PROBLEM_LARGE_INPUT "-large"

#include <set>
#include <vector>

using namespace std;


bool is_tidy(const string& s)
{
	for (int i=s.size()-1; i>=1; --i)
	{
		if (s[i-1] > s[i])
			return false;
	}
	return true;
}

bool decr_last_to_9(string& s, int index_last)
{
	if (s[index_last] == '9')
		return true;

	int index = index_last - 1;
	while (true)
	{
		if (index < 0)
			return false;
		if (s[index] == '0')
			index--;
		else
		{
			s[index] -= 1;
			for (int i=index+1; i<=index_last; ++i)
				s[i] = '9';
			return true;
		}
	}
	return false;
}

string remove_heading_0(const string& s)
{
	int i=0;
	for (;i<s.size(); ++i)
	{
		if (s[i] != '0')
			break;
	}
	string s2 = s.substr(i);
	return s2;
}

int main(int argc, char* argv[])
{
//	set_fio(PROBLEM_NAME ".txt");
//	set_fio(PROBLEM_NAME PROBLEM_SMALL_INPUT ".in");
//	set_fio(PROBLEM_NAME PROBLEM_SMALL_INPUT ".in", PROBLEM_NAME PROBLEM_SMALL_INPUT ".out.txt");
//	set_fio(PROBLEM_NAME PROBLEM_LARGE_INPUT ".in");
	set_fio(PROBLEM_NAME PROBLEM_LARGE_INPUT ".in", PROBLEM_NAME PROBLEM_LARGE_INPUT ".out.txt");

	int T;
	fin >> T;
	for (int cases=1; cases<=T; ++cases)
	{
		string s;
		fin >> s;
		string orig = s;

		int index = s.size() - 1;
		while (index >= 0 && !is_tidy(s))
		{
			bool reduce = decr_last_to_9(s, index);
			index--;
		}


		string s2 = remove_heading_0(s);

		//fout << "Case #" << cases << ": " << orig << " => " << s << " :" << is_tidy(s) << endl;
		fout << "Case #" << cases << ": " << s2 << endl;
	}

	return 0;
}
