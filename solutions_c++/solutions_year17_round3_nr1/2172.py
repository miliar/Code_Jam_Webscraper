#include <iostream>
#include <string>
#include <fstream>
#include <algorithm>
#include <iomanip> 
#include <vector>

class cake
{
public:
	std::vector<long long> values;
	
	bool operator<(const cake *other)
	{
		//return values[0] < other.values[0];
		return (other -> values[0]) < values[0];
	}
};

struct less_than_key
{
	inline bool operator() (const cake& struct1, const cake& struct2)
	{
		return (struct2.values[0] < struct1.values[0]);
	}
};

using namespace std;



int N, k;
long long dp[10001][10001];
long long sur(int i, int chosen, vector<cake> &cakes) {
	if (chosen == k) return 0;
	if (i == N) return -1;

	if (dp[i][chosen] != 0) return dp[i][chosen];

	long long vY = -1, vN = -1;

	vY = sur(i + 1, chosen + 1, cakes) + 2 * cakes[i].values[0] * cakes[i].values[1] + 
							(chosen == 0? cakes[i].values[0] * cakes[i].values[0] : 0);
	
	vN = sur(i + 1, chosen, cakes);

	if (vY == -1 && vN == -1) return -1;
	return dp[i][chosen] = max(vY, vN);
}

int main() {
	ifstream infile("in.txt");
	ofstream out("p11.txt");

	int T;
	infile >> T;
	
	const double pi = 3.1415926535897932384626433832795028841971;
	
	//cake *cakes[1005];
	
	for (int t = 0; t < T; t++) {
		infile >> N >> k;

		vector<cake> cakes;
		cakes.empty();

		for (int i = 0; i < N; i++) {
			//cakes[i] = new cake();
			//cakes[i]->values.push_back(0);
			//cakes[i]->values.push_back(0);

			//infile >> cakes[i] -> values[0];
			//infile >> cakes[i] -> values[1];

			cakes.push_back(cake());
			cakes[i].values.push_back(0);
			cakes[i].values.push_back(0);

			infile >> cakes[i].values[0];
			infile >> cakes[i].values[1];
		}

		sort(cakes.begin(), cakes.end() ,less_than_key());
		
		memset(dp, 0, sizeof(dp[0][0]) * 1001 * 1001);
		double ans = (double) sur(0, 0, cakes) * pi;
		if (ans == -pi) {
			cout << 1;
		}
		out << "Case #" << t + 1 << ": " << fixed << setprecision(6) << ans << endl;
	}

}