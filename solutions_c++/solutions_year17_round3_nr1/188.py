#include <algorithm>
#include <iostream>
#include <iomanip>
#include <utility>
#include <string>
#include <vector>

using namespace std;

int main(){
	int cases;
	cin>>cases;

	for (int cas=1; cas<=cases; ++cas){
		cout << "Case #"<<cas << ": ";

		int N,K;
		cin>>N>>K;

		vector <pair <long long, long long> > pancake;

		for(int i=0;i<N;++i){
			int tmpr,tmph;
			cin>>tmpr>>tmph;
			pancake.push_back(make_pair(tmpr,tmph));
		}

		sort(pancake.begin(), pancake.end());

		long long res = 0;

		for (int largest = K-1; largest < N; ++largest) {
			vector <long long> side;

			for (int i=0; i<largest; ++i) {
				side.push_back(2*pancake[i].first*pancake[i].second);
			}

			sort(side.begin(), side.end());

			long long tmp = 0;
			for (int i=largest+1-K; i<largest; ++i){
				tmp += side[i];
			}

			tmp += 2 * pancake[largest].first * pancake[largest].second;

			tmp += pancake[largest].first * pancake[largest].first;

			res = max(res, tmp);
		}


		cout << setprecision(12) << (double)res * 3.14159265358979 << endl;



	}
}

