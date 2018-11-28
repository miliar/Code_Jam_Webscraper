
#define PROBLEM_NAME "A"
#define PROBLEM_SMALL_INPUT "-small-attempt1"
#define PROBLEM_LARGE_INPUT "-large"

#include <list>
#include <set>

using namespace std;

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
		double D;
		int N;
		fin >> D >> N;
		vector<double> pos, speed;
		for (int i=0; i<N; ++i)
		{
			int K, S;
			fin >> K >> S;
			pos.push_back(K);
			speed.push_back(S);
		}
		vector<double> t(N);
		for (int i=N-1; i>=0; --i)
		{
			t[i] = (D-pos[i])/speed[i];
		}

		double m = *max_element(t.begin(), t.end());
		double x = D / m;

		char str[256];
		sprintf_s(str, "%.6f", x);
		//fout << "Case #" << cases << ": " << x << endl;
		fout << "Case #" << cases << ": " << str << endl;
	}

	return 0;
}
