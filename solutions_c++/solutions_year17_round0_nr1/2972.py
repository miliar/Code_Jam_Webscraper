#include<iostream>
using std::cin;
using std::cout;
bool arr[1024];
int main() {
	int T;
	cin >> T;
	cin.get();
	for (int caseN = 1; caseN <= T; caseN++) {
		int n = 0;
		char ch = ' ';
		do {
			ch = cin.get();
			switch (ch) {
			case '-':
				arr[n] = false;
				n++;
				break;
			case '+':
				arr[n] = true;
				n++;
				break;
			}
		} while (ch != ' ');
		int K;
		cin >> K;
		cin.get();
		//do calc
		int ans = 0;
		for (int i = n - K; i >= 0; i--) {
			if (arr[i + K - 1] == false) {
				ans++;
				for (int j = 0; j < K; j++) {
					arr[i + j] = !(arr[i + j]);//flip
				}
			}
		}
		//check for last K and must all true
		bool correct = true;
		for (int i = 0; i < K; i++) {
			if (arr[i] != true)correct = false;
		}
		//check for impossible
		cout << "Case #" << caseN << ": ";
		if (correct) cout << ans << std::endl;
		else cout << "IMPOSSIBLE" << std::endl;

	}
	//system("PAUSE");
	return 0;
}