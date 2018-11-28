#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>
#include <string>
#include <queue>

using namespace std;

const double PI = 3.14159265359;

bool myComparison(const pair<int, double> &a,const pair<int, double> &b)
{
    return a.second < b.second;
}

int main() {
    freopen("AmpleSyrup.in", "rt", stdin);
	freopen("AmpleSyrup.out", "wt", stdout);
	ios_base::sync_with_stdio(false);

    int numTests;
	cin >> numTests;

    for (int t = 0; t < numTests; ++t) {
		int N, K;
		cin >> N >> K;
		vector <int> radius(N);
		vector <int> height(N);
		
		for (int i = 0; i < N; ++i) {
			cin >> radius[i] >> height[i];
		}
		
		double answer = 0.0;
		for (int maxIndex = 0; maxIndex < N; ++maxIndex) {	
			double curAnswer = PI * radius[maxIndex] * radius[maxIndex] + 2 * PI * radius[maxIndex] * height[maxIndex];
			if (K > 1) {
				vector <pair <int, double>> area;
				for (int i = 0; i < N; ++i) {
					if (i != maxIndex) {
						area.push_back(make_pair(i, 2 * PI * radius[i] * height[i]));
					}
				}
				
				sort(area.rbegin(), area.rend(), myComparison);
				
				for (int i = 0; i < (K - 1); ++i) {
					curAnswer += area[i].second;
				}
			}
			
			if (answer < curAnswer) answer = curAnswer;
		}

		cout.precision(9);
		cout << "Case #" << t + 1 << ": " << fixed << answer << endl;
    }
    
    return 0;
}
