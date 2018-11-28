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

//int main17R2_A()
int main()
{
	ifstream fin("A-large.in");
	ofstream fout("A-large.out");
	//ifstream fin("test.in");
	//ofstream fout("test.out");

	unsigned int numberOfCases;
	fin >> numberOfCases;

	for (unsigned int zz = 1; zz <= numberOfCases; ++zz)
	{
		int N, P;
		fin >> N >> P;

		vector<int> cnt(P);
		for (int i = 0; i < N; ++i)
		{
			int x;
			fin >> x;
			x = x % P;
			++cnt[x];
		}

		int result = cnt[0];
		if (P == 2)
		{
			result += (cnt[1] + 1) / 2;
		}
		else if (P == 3)
		{
			int m = min(cnt[1], cnt[2]);
			int extra = max(cnt[1], cnt[2]) - m;
			result += m;
			result += (extra + 2) / 3;
		}
		else if (P == 4)
		{
			int m = min(cnt[1], cnt[3]);
			int extra = max(cnt[1], cnt[3]) - m;
			result += m;

			result += cnt[2] / 2;
			cnt[2] = cnt[2] % 2;

			if (cnt[2] > 0)
			{
				++result;
				extra = max(0, extra - 2);
			}

			result += (extra + 3) / 4;
		}
		
		fout << "Case #" << zz << ": " << result << endl;
	}

	return 0;
}
