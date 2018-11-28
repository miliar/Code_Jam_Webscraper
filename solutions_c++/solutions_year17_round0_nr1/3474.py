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
	INPUT(string, S);
	INPUT(int, K);
	size_t len = S.size();
	int c = 0;
	for (int i = 0; i + K - 1 < len; ++i)
	{
		if (S[i] == '-')
		{
			transform(&S[i], &S[i + K], &S[i], [](const char& c){return c == '+' ? '-' : '+'; });
			++c;
		}
	}
	if (S.find('-') != string::npos)
		return string("IMPOSSIBLE");
	return to_string(c);
};

#define IONAME "2017Qual/A/A-large"

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