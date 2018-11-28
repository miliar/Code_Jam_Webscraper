
#define PROBLEM_NAME "C"
#define PROBLEM_SMALL_INPUT "-small-1-attempt0"
#define PROBLEM_MID_INPUT "-small-2-attempt1"
#define PROBLEM_LARGE_INPUT "-large"

#include <algorithm>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <string>

using namespace std;

struct stall_info
{
	int leftmost_occupied_stall,
		rightmost_occupied_stall;
};

bool operator<(const stall_info& l, const stall_info& r)
{
	int dl = l.rightmost_occupied_stall - l.leftmost_occupied_stall;
	int dr = r.rightmost_occupied_stall - r.leftmost_occupied_stall;

	if (dl > dr)
		return true; // bigger one should be at the front
	else if (dl < dr)
		return false;

	return (l.leftmost_occupied_stall < r.leftmost_occupied_stall &&
		l.rightmost_occupied_stall < r.rightmost_occupied_stall);


	//return (dl > dr ||
	//	(dl == dr && l.rightmost_occupied_stall < r.leftmost_occupied_stall));
	//	(l.rightmost_occupied_stall < r.leftmost_occupied_stall));

//	return (
//		l.leftmost_occupied_stall < r.leftmost_occupied_stall &&
//		l.rightmost_occupied_stall < r.rightmost_occupied_stall);
}

void dump(set<stall_info>& s, int N, set<int>& occupied)
{
	return;
	string str(N+2, '.');
	str[0] = '|';
	str[N+1] = '|';

	for (set<int>::iterator it = occupied.begin(); it != occupied.end(); ++it)
	{
		str[*it] = 'O';
	}

	//for (set<stall_info>::iterator it = s.begin(); it != s.end(); ++it)
	//{
	//	stall_info i = *it;
	//	str[i.leftmost_occupied_stall] = 'O';
	//	str[i.rightmost_occupied_stall] = 'O';
	//}
	cerr << str << endl;
}


struct Greater
{
	bool operator()(int l, int r) { return l > r; }
};


typedef map<int, int, Greater> mymap;
mymap S;

inline void add_i(int i, int count = 1)
{
	mymap::iterator it = S.find(i);
	if (it != S.end())
		(*it).second+=count;
	else
		S[i] = count;
}

int main(int argc, char* argv[])
{
//	set_fio(PROBLEM_NAME ".txt");
//	set_fio(PROBLEM_NAME PROBLEM_SMALL_INPUT ".in");
//	set_fio(PROBLEM_NAME PROBLEM_SMALL_INPUT ".in", PROBLEM_NAME PROBLEM_SMALL_INPUT ".out.txt");
//	set_fio(PROBLEM_NAME PROBLEM_MID_INPUT ".in");
	set_fio(PROBLEM_NAME PROBLEM_MID_INPUT ".in", PROBLEM_NAME PROBLEM_MID_INPUT ".out.txt");
//	set_fio(PROBLEM_NAME PROBLEM_LARGE_INPUT ".in");
//	set_fio(PROBLEM_NAME PROBLEM_LARGE_INPUT ".in", PROBLEM_NAME PROBLEM_LARGE_INPUT ".out.txt");

	int T;
	fin >> T;
	for (int cases=1; cases<=T; ++cases)
	{
		int N, K;
		fin >> N >> K;

		S.clear();
		S[N] = 1;

		int last_insert = 0;
		for (int i=1; i<=K; ++i)
		{
			mymap::iterator it = S.begin();
			last_insert = (*it).first;
			int v = last_insert;
			if ((*it).second == 1)
				S.erase(it);
			else
				(*it).second--;

			if (v == 1)
			{
			}
			else if (v == 2)
			{
				add_i(1);
			}
			else
			{
				if (v&1)
				{
					int vv = v>>1;
					add_i(vv, 2);
				}
				else
				{
					int vv = v>>1;
					add_i(vv-1);
					add_i(vv);
				}
			}
		}

		fout << "Case #" << cases << ": ";
		int vv = last_insert>>1;
		if (last_insert == 1)
		{
			fout << "0 0" << endl;
		}
		else if (last_insert == 2)
		{
			fout << "1 0" << endl;
		}
		else if (last_insert&1)
		{
			fout << vv << " " << vv << endl;
		}
		else
		{
			fout << vv << " " << vv-1 << endl;
		}
	}

	return 0;
}

int main1(int argc, char* argv[])
{
//	set_fio(PROBLEM_NAME ".txt");
//	set_fio(PROBLEM_NAME PROBLEM_SMALL_INPUT ".in");
//	set_fio(PROBLEM_NAME PROBLEM_SMALL_INPUT ".in", PROBLEM_NAME PROBLEM_SMALL_INPUT ".out.txt");
	set_fio(PROBLEM_NAME PROBLEM_MID_INPUT ".in");
//	set_fio(PROBLEM_NAME PROBLEM_MID_INPUT ".in", PROBLEM_NAME PROBLEM_MID_INPUT ".out.txt");
//	set_fio(PROBLEM_NAME PROBLEM_LARGE_INPUT ".in");
//	set_fio(PROBLEM_NAME PROBLEM_LARGE_INPUT ".in", PROBLEM_NAME PROBLEM_LARGE_INPUT ".out.txt");

	int T;
	fin >> T;
	for (int cases=1; cases<=T; ++cases)
	{
		int N, K;
		fin >> N >> K;

		multiset<int, Greater> s;
		s.insert(N);

		int last_insert = 0;
		for (int i=1; i<=K; ++i)
		{
			int v = *s.begin();
			last_insert = v;
			s.erase(s.begin());
			if (v == 1)
			{
			}
			else if (v == 2)
			{
				s.insert(1);
			}
			else
			{
				if (v&1)
				{
					int vv = v>>1;
					s.insert(vv);
					s.insert(vv);
				}
				else
				{
					int vv = v>>1;
					s.insert(vv-1);
					s.insert(vv);
				}
			}
		}

		fout << "Case #" << cases << ": ";
		int vv = last_insert>>1;
		if (last_insert == 1)
		{
			fout << "0 0" << endl;
		}
		else if (last_insert == 2)
		{
			fout << "1 0" << endl;
		}
		else if (last_insert&1)
		{
			fout << vv << " " << vv << endl;
		}
		else
		{
			fout << vv << " " << vv-1 << endl;
		}
	}

	return 0;
}


int main0(int argc, char* argv[])
{
//	set_fio(PROBLEM_NAME ".txt");
//	set_fio(PROBLEM_NAME PROBLEM_SMALL_INPUT ".in");
//	set_fio(PROBLEM_NAME PROBLEM_SMALL_INPUT ".in", PROBLEM_NAME PROBLEM_SMALL_INPUT ".out.txt");
	set_fio(PROBLEM_NAME PROBLEM_MID_INPUT ".in");
//	set_fio(PROBLEM_NAME PROBLEM_MID_INPUT ".in", PROBLEM_NAME PROBLEM_MID_INPUT ".out.txt");
//	set_fio(PROBLEM_NAME PROBLEM_LARGE_INPUT ".in");
//	set_fio(PROBLEM_NAME PROBLEM_LARGE_INPUT ".in", PROBLEM_NAME PROBLEM_LARGE_INPUT ".out.txt");

	int T;
	fin >> T;
	for (int cases=1; cases<=T; ++cases)
	{
		int N, K;
		fin >> N >> K;

		set<stall_info> s;
		stall_info init;
		init.leftmost_occupied_stall = 0;
		init.rightmost_occupied_stall = N+1;
		s.insert(init);

		set<int> occupied;
		occupied.insert(0);
		occupied.insert(N+1);

//		cerr << "init" << endl;
		dump(s, N, occupied);

		int leftmost_occupied_at_last_insert = 0,
			rightmost_occupied_at_last_insert = N+1,
			index_occupied_at_last_insert = 0;
		for (int i=1; i<=K; ++i)
		{
			stall_info v = *s.begin();
			int idx = (v.leftmost_occupied_stall + v.rightmost_occupied_stall)/2;
			stall_info v1, v2;
			v1.leftmost_occupied_stall = v.leftmost_occupied_stall;
			v1.rightmost_occupied_stall = idx;
			v2.leftmost_occupied_stall = idx;
			v2.rightmost_occupied_stall = v.rightmost_occupied_stall;

			leftmost_occupied_at_last_insert = v.leftmost_occupied_stall;
			rightmost_occupied_at_last_insert = v.rightmost_occupied_stall;
			index_occupied_at_last_insert = idx;

			int size1 = s.size();
			s.erase(s.begin());
			occupied.insert(idx);
			int size_incr = 0;
			if (v1.rightmost_occupied_stall > v1.leftmost_occupied_stall + 1)
			{
				s.insert(v1);
				size_incr++;
			}
			if (v2.rightmost_occupied_stall > v2.leftmost_occupied_stall + 1)
			{
				s.insert(v2);
				size_incr++;
			}

			int size2 = s.size();

			if (size2 != size1 - 1 + size_incr)
				cerr << "ERROR size mismatch. before " << size1 << ", after " << size2 << endl;

//			cerr << "step : " << i << endl;
			dump(s, N, occupied);
		}

		int left_empty = index_occupied_at_last_insert - leftmost_occupied_at_last_insert - 1;
		int right_empty = rightmost_occupied_at_last_insert - index_occupied_at_last_insert - 1;

		fout << "Case #" << cases << ": ";
		if (left_empty >= right_empty)
			fout << left_empty << " " << right_empty << endl;
		else
			fout << right_empty << " " << left_empty << endl;
	}

	return 0;
}
