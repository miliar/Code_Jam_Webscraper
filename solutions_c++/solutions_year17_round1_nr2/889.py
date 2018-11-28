
#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <deque>
#include <cmath>
using namespace std;
#define txt
#ifdef txt
ofstream out("out.txt");
ifstream in("in.txt");
#else
ofstream& out = cout;
ofstream& in = cin;
#endif

bool Pred(pair<int, int>p1, pair<int, int>p2)
{
	if (p1.first < p2.first)return true;
	else if (p1.first == p2.first)
	{
		if (p1.second < p2.second)return true;
		else return false;
	}
	else return false;
}



int main()
{
int T;
in >> T;

for (int cn = 1; cn <= T; cn++)
{
	int N, P;
	in >> N >> P;
	vector<int> R(N);
	for (int i = 0; i < N; i++)
		in >> R[i];
	vector<vector<pair<int, int>>> Q(N, vector<pair<int, int>>());
	int temp;

	for (int i = 0; i < N; i++)
		for (int j = 0; j < P; j++)
		{
			in >> temp;
			pair<int, int> pt;
			pt.first = (int)ceil((double)temp / 1.1 / R[i]);
			pt.second = (int)floor((double)temp / 0.9 / R[i]);
			if (pt.first <= pt.second)
				Q[i].push_back(pt);
		}
	for (int i = 0; i < N; i++)
	{
		sort(Q[i].begin(), Q[i].end(), Pred);
	}
	vector<pair<int, int>> Res;
	Res.reserve(P);
	Res = Q[0];
	for (int i = 1; i < N; i++)
	{
		vector<pair<int, int>> Tv;
		auto ri = Res.begin();
		auto qi = Q[i].begin();
		while (1)
		{
			if (ri == Res.end() || qi == Q[i].end())break;
			if (ri->first > qi->second) qi++;
			else if (ri->second < qi->first) ri++;
			else
			{
				Tv.push_back(pair<int, int>(max(ri->first, qi->first), min(ri->second, qi->second)));
				ri++; qi++;
			}

		}
		sort(Tv.begin(), Tv.end(), Pred);
		Res.swap(Tv);
	}
	out << "Case #" << cn <<": " << Res.size() << endl;
}

}
