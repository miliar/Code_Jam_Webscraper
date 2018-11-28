#include "com.hpp"

vector<string> split(const string& input, char delimiter)
{
	istringstream stream(input);

	string field;
	vector<string> result;
	while (getline(stream, field, delimiter)) {
		result.push_back(field);
	}
	return result;
}

static auto solve = []()
{
	INPUT(int, R);
	INPUT(int, C);
	vvc S = vvc(R,vc(C));
	vi y;
	vi x;
	REP(r, R) REP(c, C)
	{
		cin >> S[r][c];
		if (S[r][c] != '?')
		{
			y.push_back(r);
			x.push_back(c);
		}
	}
	vi yy = vi(y);
	sort(yy.begin(), yy.end());
	yy.erase(unique(yy.begin(), yy.end()), yy.end());
	auto next = yy.begin();
	++next;
	REP(i, y.size())
	{
		if (next == yy.end())
		{
		}
		else if (*next == y[i])
		{
			++next;
		}
		int l = 0;
		int r = C-1;
		REP(j,y.size())
		{
			if (i == j)continue;
			if (y[i] == y[j])
			{
				if (x[i] < x[j])
				{
					r = min(x[j] - 1, r);
				}
				else
				{
					l = max(x[j] + 1, l);
				}
			}
		}
		REP(j, x.size())
		{
			if (i == j)continue;
			if (y[i] == y[j])
			{
				if (x[i] < x[j])
				{
					r = min(x[j] - 1, r);
				}
				else
				{
					l = max(x[j] + 1, l);
				}
			}
		}
		int t = y[i] == *yy.begin() ? 0 : y[i];
		int b = (next == yy.end()   ? R : *next);
		
		for (int rr = t; rr < b; ++rr)
		{
			for (int c = l; c <= r; ++c)
			{
				if (x[i] == c && y[i] == rr)continue;
				if (S[rr][c] == '?')
				{
					S[rr][c] = S[y[i]][x[i]];
				}
				else
				{
					//cout << "?‚¶‚á‚È‚¢I" << endl;
					//abort();
				}
			}
		}
	}

	REP(r, R)
	{
		REP(c, C)
		{
			cout << S[r][c];
		}
		cout << endl;
	}
};

#define IONAME "2017R1/A/A-large"

int main(int argv, char* argc[])
{

	ifstream in(IONAME".in");
	cin.rdbuf(in.rdbuf());
	ofstream ofs(IONAME".out", ios_base::out);
	cout.rdbuf(ofs.rdbuf());
	INPUT(int, caseNum);
	for (int i = 0; i < caseNum; ++i)
	{
		cout << "Case #" << i + 1 << ":" << endl;
		solve();
		//cout << "Case #" << i + 1 << ": " << solve() << endl;
	}
	return 0;
}