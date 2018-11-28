
#define PROBLEM_NAME "A"
#define PROBLEM_SMALL_INPUT "-small-attempt0"
#define PROBLEM_LARGE_INPUT "-large"

#include <list>

using namespace std;


struct part
{
	int r_from, r_to, c_from, c_to;
	part(int _r_from, int _r_to, int _c_from, int _c_to) : r_from(_r_from), r_to(_r_to), c_from(_c_from), c_to(_c_to) {}

	int area() const
	{
		if (r_to >= r_from && c_to >= c_from)
		{
			return (r_to - r_from + 1)*(c_to - c_from + 1);
		}
		else
			return 0;
	}
};

int get_q_count(part a, const vector<string>& v, int R, int C)
{
	int count = 0;
	for (int r=a.r_from; r<=a.r_to; ++r)
	{
		for (int c=a.c_from; c<=a.c_to; ++c)
		{
			if (r >= R) continue;
			if (c >= C) continue;

			if (v[r][c] == '?')
				count++;
		}
	}
	return count;
}


void cut(list<part>& p, const vector<string>& v, int R, int C)
{
	auto it = p.begin();
	while (true)
	{
		if (it == p.end())
			break;

		part& a = (*it);
		int count = get_q_count(a, v, R, C);
		if (count == 0)
		{
			++it;
			continue;
		}
		//else if (count == 1)
		{
		}

		bool found = false;
		for (int r=a.r_from; r <= a.r_to && !found; ++r)
		{
			for (int c=a.c_from; c <= a.c_to && !found; ++c)
			{
				if (r == a.r_from && c == a.c_from)
					continue;

				part pLU(a.r_from, r-1, a.c_from, c-1);
				part pLD(r, a.r_to, a.c_from, c-1);
				part pRU(a.r_from, r-1, c, a.c_to);
				part pRD(r, a.r_to, c, a.c_to);

				int countLU, countLD, countRU, countRD;
				countLU = get_q_count(pLU, v, R, C);
				countLD = get_q_count(pLD, v, R, C);
				countRU = get_q_count(pRU, v, R, C);
				countRD = get_q_count(pRD, v, R, C);

				int areaLU = pLU.area();
				int areaLD = pLD.area();
				int areaRU = pRU.area();
				int areaRD = pRD.area();

				if (areaLU != 0 && countLU == areaLU)
					continue;
				if (areaLD != 0 && countLD == areaLD)
					continue;
				if (areaRU != 0 && countRU == areaRU)
					continue;
				if (areaRD != 0 && countRD == areaRD)
					continue;

				if (areaLU != 0) p.push_back(pLU);
				if (areaLD != 0) p.push_back(pLD);
				if (areaRU != 0) p.push_back(pRU);
				if (areaRD != 0) p.push_back(pRD);
				it = p.erase(it);
				found = true;
				break;
			}
		}

		if (!found)
		{
			++it;
			continue;
		}
	}
}


void fill(const list<part>& p, vector<string>& v, int R, int C)
{
	for (auto it = p.begin(); it != p.end(); ++it)
	{
		const part& a = (*it);
		int count = get_q_count(a, v, R, C);
		if (count == 0)
		{
			continue;
		}
		else if (count +1 == a.area())
		{
			char ch = '?';
			bool found = false;
			for (int r=a.r_from; r <= a.r_to && !found; ++r)
			{
				for (int c=a.c_from; c <= a.c_to && !found; ++c)
				{
					if (v[r][c] != '?')
					{
						ch = v[r][c];
						found = true;
						break;
					}
				}
			}
			for (int r=a.r_from; r <= a.r_to; ++r)
			{
				for (int c=a.c_from; c <= a.c_to; ++c)
				{
					v[r][c] = ch;
				}
			}
		}
		else
		{
			int should_not_reach_here = 1;
		}
	}
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
		int R, C;
		fin >> R >> C;
		vector<string> v;
		for (int i=0; i<R; ++i)
		{
			string S;
			fin >> S;
			v.push_back(S);
		}

		list<part> p;
		p.push_back(part(0, R-1, 0, C-1));
		cut(p, v, R, C);

		fill(p, v, R, C);

		fout << "Case #" << cases << ":"<<endl;
		for (int i=0; i<R; ++i)
			fout << v[i] << endl;
	}

	return 0;
}
