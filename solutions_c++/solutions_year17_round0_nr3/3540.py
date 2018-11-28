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
	INPUT(ll, N);
	INPUT(ll, K);
	int g = 0;
	int n = 1;
	for (; n <= K; ++g, n *= 2);
	double r = (double)(N - K) / n;
	int maxv = ((r + 0.5) / 2) * 2;
	int minv = r;
	return to_string(maxv) + " " + to_string(minv);
};

#define IONAME "2017Qual/C/C-sample"
#define IONAME "2017Qual/C/C-small-1-attempt0"
#define IONAME "2017Qual/C/C-small-2-attempt1"

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