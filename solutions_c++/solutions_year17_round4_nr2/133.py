#include<fstream>
#include<iostream>
#include<sstream>
#include<iomanip>
#include<string>
#include<vector>
#include<list>
#include<set>
#include<map>
#include<queue>
#include<algorithm>
#include<functional>
#include<numeric>
#include<bitset>
using namespace std;
typedef pair<int, int> pii;
typedef long long ll;
#define mp make_pair

//int main17R2_B()
int main()
{
	ifstream fin("B-large.in");
	ofstream fout("B-large.out");
	//ifstream fin("test.in");
	//ofstream fout("test.out");

	unsigned int numberOfCases;
	fin >> numberOfCases;

	for (unsigned int zz = 1; zz <= numberOfCases; ++zz)
	{
		int N, C, M;
		fin >> N >> C >> M;
		vector<vector<int> > vv(C);
		vector<int> cnt(N, 0);
		for (int i = 0; i < M; ++i)
		{
			int P, B;
			fin >> P >> B;
			vv[B-1].push_back(P-1);

			++cnt[P - 1];
		}

		int result(0);
		for (auto& v : vv)
		{
			result = max<int>(result, v.size());
		}

		int running(0);
		for (int i = 0; i < N; ++i)
		{
			running += cnt[i];
			int j = i + 1;
			int cur = (running + i) / j;
			result = max(result, cur);
		}

		int promos(0);
		for (int i = 0; i < N; ++i)
		{
			promos += max(0, cnt[i] - result);
		}

		fout << "Case #" << zz << ": " << result << " " << promos << endl;
	}

	return 0;
}
