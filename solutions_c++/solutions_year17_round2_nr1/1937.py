#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <iomanip>

using namespace std;

typedef long long ll;


ll f1(ll n, ll k)
{
	int exponent = log2(k) + 1;
	ll numRepeats = 1;
	for (int i = 0; i < exponent; ++i)
		numRepeats *= 2;

	return (n - (k - numRepeats / 2)) / numRepeats;
}

ll f2(ll n, ll k)
{
	int exponent = log2(k) + 1;
	ll numRepeats = 1;
	for (int i = 0; i < exponent; ++i)
		numRepeats *= 2;

	return (n - k) / numRepeats;
}

int main()
{
	ofstream output;
	ifstream input;
	input.open("input.txt");
	output.open("output.txt");
	output  << std::fixed;
	output << std::setprecision(10);
	//	FILE * input;
	//	input = fopen("input.txt","r");

	int T;

	//	fread(&n, sizeof(int), 1, input);cout<<n<<endl; char cc=getchar();

	input >> T;// cout<<n<<endl;
	//cin >> T;

	//string s;
	long long d, n;
	long long k, s;
	double ans = 0;

	vector<pair<long long, long long>> horses;

	for (int t = 0; t < T; ++t)
	{
		input >> d >> n;
		horses.clear();
		for (int i = 0; i < n; ++i)
		{
			input >> k >> s;
			horses.push_back(make_pair(k, s));
		}
				
		std::sort(horses.begin(), horses.end(), [](const std::pair<int, int> &left, const std::pair<int, int> &right) {
			return left.first< right.first;
		});

		int right = n - 1;
		int left = n - 2;
		while (left >= 0){
			if (horses[left].second < horses[right].second ||
				(horses[right].first - horses[left].first) * horses[left].second >= (d - horses[left].first)*(horses[left].second - horses[right].second)){
				right = left;
				left = right - 1;
			}
			else {
				--left;
			}
		}

		ans = double(d) * double(horses[right].second) / (double(d - horses[right].first));

		output << "Case #" << t + 1 << ": " << ans<<endl;
		


	}
	//	fclose(input);
	input.close();
	output.close();
	//	system("pause");
	return 0;
}
