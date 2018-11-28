#include<iostream>
#include<set>
#include<algorithm>

using namespace std;

struct LR {
	long LSM;
	long RSM;
};

int main() {
	int t = 0;
	cin >> t;
	for (int p = 1; p <= t; ++p) {
		long N, K;
		cin >> N >> K;
		LR arr[N];
		set<long> setOfInd;
		for (int i = 0; i < N; ++i) {
			arr[i].LSM = -1;
			arr[i].RSM = N;
			setOfInd.insert(i);
		}
		long choice = (N - 1) / 2;
		long new_choice_mini = choice;
		long new_choice_maxi = N - 1 - choice;
		for (int i = 0; i < K - 1; ++i) {
			setOfInd.erase(choice);
			long new_choice = -1;
			for (set<long>::iterator it=setOfInd.begin(); it!=setOfInd.end(); ++it) {
				long cur = *it;
				if (cur < choice) {
					if (arr[cur].RSM > choice) {
						arr[cur].RSM = choice;
					}
				}
				if (cur > choice) {
					if (arr[cur].LSM < choice) {
						arr[cur].LSM = choice;
					}
				}
				long LS = cur - arr[cur].LSM - 1;
				long RS = arr[cur].RSM - cur - 1;
				long mini = min(LS, RS);
				long maxi = max(LS, RS);
				if ((new_choice == -1) || 
					(mini > new_choice_mini) || 
					((mini == new_choice_mini) && (maxi > new_choice_maxi)) ||
					((mini == new_choice_mini) && (maxi == new_choice_maxi) && (cur < new_choice))) {
					new_choice = cur;
					new_choice_mini = mini;
					new_choice_maxi = maxi;
				}
			}
			choice = new_choice;
		}
		cout << "Case #" << p << ": " << new_choice_maxi << " " << new_choice_mini << endl;
	}
}
