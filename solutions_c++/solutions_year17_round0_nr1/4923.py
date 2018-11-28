#include <iostream>
#include <string>
using namespace std;


void testcase(int ncase, string row, int K){
	cout << "Case #" << ncase << ": ";
	int ans=0;
	for (int i = 0; i <= row.size()-K; ++i){
		if ( row[i] == '-' ){
			ans++;
			for (int j = i; j < i+K; ++j){
				if (row[j] == '+')
					row[j] = '-';
				else
					row[j] = '+';
			}
		}
	}
	// cout << row << endl;
	for (int i = 0; i < row.size(); ++i){
		if (row[i] == '-'){
			cout << "IMPOSSIBLE" << endl;
			return;
		}
	}
	cout << ans << endl;
	return;
}

int main(){
	int T;
	cin >> T;
	string row;
	int K;
	for (int i = 0; i < T; ++i)
	{
		cin >> row >> K;
		testcase(i+1, row, K);
	}

	return 0;
}