#include <iostream>
#include <iterator>
#include <vector>
#include <set>
#include <algorithm>
#include <numeric>
#include <string>
#include <iomanip>

using namespace std;

const long double EPS = 1e-8;
const long double Pi = 3.14159265358979323846264338327950288;
double const_pi() { return std::atan(1) * 4; }

long double MaxSurface_anotherpi(vector<pair<double, double>>& pancakes, int N, int K)
{
	sort(pancakes.begin(), pancakes.end(), [](const pair<double, double>& l, const pair<double, double>& r) {
		return (l.first > r.first) || ((abs(l.first - r.first) < EPS) && (l.second > r.second));
	});

	long double globalmax = 0.0;

	vector<vector<long double>> dp(1 + N, vector<long double>(1 + K, 0.0));

	vector<long double> surf(1 + N, 0.0);

	for (int i = 0; i < N; ++i)
	{
		const auto& p = pancakes[i];

		surf[i + 1] = (2 * const_pi() * p.first /*R*/ * p.second /*H*/);

		dp[i + 1][1] = const_pi() * p.first /*R*/ * p.first /*R*/ + surf[i + 1];
		globalmax = max(dp[i + 1][1], globalmax);
	}


	for (int k = 2; k <= K; ++k)
	{
		for (int i = 1; i <= N; ++i)
		{
			dp[i][k] = max(dp[i][k - 1], surf[i] + dp[i - 1][k - 1]);
			globalmax = max(dp[i][k], globalmax);
		}
	}

	return globalmax;
}

long double MaxSurface(vector<pair<double, double>>& pancakes, int N, int K)
{

	sort(pancakes.begin(), pancakes.end(), [] (const pair<double, double>& l, const pair<double, double>& r){
		return (l.first > r.first) || ((abs(l.first - r.first) < EPS) && (l.second > r.second));
	});

	long double globalmax = 0.0;

	vector<vector<long double>> dp(1 + N, vector<long double>(1 + K, 0.0));

	vector<long double> surf(1 + N, 0.0);

	for (int i = 0; i < N; ++i)
	{
		const auto& p = pancakes[i];

		surf[i + 1] = (2 * Pi * p.first /*R*/ * p.second /*H*/);

		dp[i + 1][1] = Pi * p.first /*R*/ * p.first /*R*/ + surf[i + 1];
		globalmax = max(dp[i + 1][1], globalmax);
	}


	for (int k = 2; k <= K; ++k)
	{
		for (int i = k; i <= N; ++i)
		{
			for (int j = 1; j < i; ++j)
			{
				dp[i][k] = max(dp[i][k], surf[i] + dp[j][k - 1]);
				globalmax = max(dp[i][k], globalmax);
			}
		}
	}

	return globalmax;
}

int main(int, char*[])
{   
   ios_base::sync_with_stdio(false);
   cin.tie(NULL);
  
   int T = 0;

   cin >> T;

   const int c_T = T;

   while (--T >= 0)
   {


      //N, R, O, Y, G, B, and V
	   int N = 0;
	   int K = 0;
	   cin >> N >> K;

	   vector<pair<double, double>> pancakes(N);
	   for (int i = 0; i < N; ++i)
	   {
		   //double Ri, Hi;
		   //cin >> Ri >> Hi;
		   cin >> pancakes[i].first >> pancakes[i].second;
	   }

      //vector<int> colors(6, 0);


      //cout << "Case #" << c_T - T << ": " << getStale2(colors, N);
	  //cout << "Case #" << c_T - T << ": " << std::fixed << std::setprecision(8) <<  MaxSurface(pancakes, N, K);
	  cout << "Case #" << c_T - T << ": " << std::fixed << std::setprecision(7) << MaxSurface(pancakes, N, K);

      if (T)
         cout << endl;
   }

   return 0;
}