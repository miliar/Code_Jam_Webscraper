
#include <iostream>
#include <vector>
#include <stack>
#include <string>
#include <algorithm>

using namespace std;

typedef long long i64;
typedef unsigned long long ui64;

int main(){
	int T;
	cin >> T;
	for (int t=1;t<=T;t++){
		int N, P;
		cin >> N >> P;
		vector<int> R(N);
		for (int i=0;i<N;i++) cin >> R[i];
		vector< vector<int> > Q(N, vector<int>(P));
		for (int n=0;n<N;n++){
			for (int p=0;p<P;p++){
				cin >> Q[n][p];
			}
			sort(Q[n].begin(), Q[n].end());
		}

		vector<int> S(N);
		for (int n=0;n<N;n++) {
			S[n]=Q[n][P-1];
			Q[n].pop_back();
		}
		bool done = false;
		int score = 0;
		while (!done){
			int limit_min = -1;
			int limit_max = 1e8;
			for (int n=0;n<N;n++){
				int l_min = ((S[n] * 10) + ((R[n] * 11) -1))  / (R[n] * 11);
				int l_max = (S[n] * 10) / (R[n] * 9);

				//cout << "local: "<< S[n] << " " << R[n]<<": "<<l_min <<  " " << l_max << endl;

				if (limit_min < l_min) limit_min = l_min;
				if (limit_max > l_max) limit_max = l_max;
			}
			//cout <<"global: "<< limit_min << " " << limit_max << endl;
			if (limit_min > limit_max){
				for (int n=0;n<N;n++){
					int l_min = ((S[n] * 10) + ((R[n] * 11) -1))  / (R[n] * 11);
					int l_max = (S[n] * 10) / (R[n] * 9);
					if (l_min > limit_max || l_min > l_max){
						if (Q[n].size() == 0){
							done = true;
							break;
						}
						else {
							S[n] = Q[n][Q[n].size()-1];
							Q[n].pop_back();
						}
					}
				}
			}
			else {
				for (int n=0;n<N;n++){
					if (Q[n].size() == 0){
							done = true;
							break;
					}
					else {
						S[n] = Q[n][Q[n].size()-1];
						Q[n].pop_back();
					}
				}
				score += 1;
			}
		}



		cout << "Case #"<<t<<": " << score << "\n";

	}

}