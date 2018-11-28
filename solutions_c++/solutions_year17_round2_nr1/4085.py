#include<iostream>
#include<string>
#include<vector>
#include<map>
#include<fstream>
#include<algorithm>
#include<set>
#include <iomanip>
#include<cstdio>

using namespace std;

int main(){

	ifstream cin("datain.txt");
	ofstream cout("dataout.txt");

	int t;
	cin >> t;

	int n;
	double  d, k, s;
	vector<pair<double, double>> vec;
	vector<double> times;

	for (size_t i = 0; i < t; i++)
	{
		cin >> d >> n;
		for (size_t j = 0; j < n; j++)
		{
			cin >> k >> s;
			vec.push_back(make_pair(k, s));
		}
		sort(vec.rbegin(), vec.rend());

		double time;
		for (size_t k = 0; k < n; k++)
		{
			time = (d - vec[k].first)/vec[k].second;
			times.push_back(time);
			
			if (k){
				// shevamowmo tu daeweva winas
				if (vec[k].second > vec[k - 1].second){
					double dtime = (vec[k - 1].first - vec[k].first) / (vec[k].second - vec[k - 1].second);
					if (dtime < times[k - 1]){
						//finishamde tu daewia
						times[k] = times[k - 1];
					}
				}
			}
		}
		double res;
		res = d / times[n - 1];
		cout << "Case #" << i+1 << ": " << fixed << setprecision(6) << res << endl;
		vec.clear();
		times.clear();
	}


	return 0;
}