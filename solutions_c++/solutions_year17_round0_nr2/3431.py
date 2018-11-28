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
	INPUT(string, N);

	while (
		[&]()
	{
		for (int i = 0; i<N.size() - 1; ++i)
		{
			if (N[i] > N[i + 1])
			{
				if (N[i] == '0')
				{
					N[i] = '9';
					if (i == 0)
					{
					}
					else
					{
						--N[i - 1];
					}
				}
				else
				{
					N[i] = N[i] - 1;
				}
				fill(&N[i + 1], &N[N.size()], '9');
				return true;
			}
		}
		return false;
	}()
		);
	N.erase(0, N.find_first_not_of('0'));
	return N;
};

#define IONAME "2017Qual/B/B-large"

int main(int argv, char* argc[])
{

	ifstream in(IONAME".in");
	cin.rdbuf(in.rdbuf());
	ofstream ofs(IONAME".out", ios_base::out);
	cout.rdbuf(ofs.rdbuf());
	INPUT(int, caseNum);
	for (int i = 0; i < caseNum; ++i)
	{
		cout << "Case #" << i + 1 << ": " << solve() << endl;
	}
	return 0;
}