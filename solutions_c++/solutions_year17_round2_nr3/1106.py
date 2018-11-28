
#define PROBLEM_NAME "C"
#define PROBLEM_SMALL_INPUT "-small-attempt0"
#define PROBLEM_LARGE_INPUT "-large"

#include <set>
#include <vector>

using namespace std;

int N, Q;
vector<vector<int> > D;
vector<pair<int, int> > horses;

// from,to : 1-based
// "about to move from 'from' to 'to'.
double mintime(int from, int to, double horse_remain, double horse_speed)
{
	if (from == to)
		return 0;

	int next = from+1; // for small dataset only

	if (horse_remain < D[from-1][next-1])
		return -1;

	horse_remain -= D[from-1][next-1];
	double mytime = D[from-1][next-1] / horse_speed;

	double t1 = mintime(next, to, horse_remain, horse_speed);
	double t2 = mintime(next, to, horses[next-1].first, horses[next-1].second);

	if (t1 < 0 && t2 < 0)
		return -1;
	if (t1 < 0)
		return t2 + mytime;
	else if (t2 < 0)
		return t1 + mytime;
	else if (t1 < t2)
		return t1 + mytime;
	else
		return t2 + mytime;
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
		fin >> N >> Q;
		horses.clear();
		for (int i=0; i<N; ++i)
		{
			int E, S;
			fin >> E >> S;
			horses.push_back(make_pair(E, S));
		}

		D.resize(N);
		for (int i=0; i<N; ++i)
		{
			D[i].resize(N);
			for (int j=0; j<N; ++j)
			{
				int d;
				fin >> d;
				D[i][j] = d;
			}
		}

		//for (int i=0; i<Q; ++i)
		//{
			int U, K;
			fin >> U >> K;
		//}

		double t = mintime(U, K, horses[0].first, horses[0].second);
		char str[100];
		sprintf_s(str, "%.6f", t);
		//fout << "Case #" << cases << ": " << t << endl;
		fout << "Case #" << cases << ": " << str << endl;
	}

	return 0;
}
