#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
	int T;
	cin >> T;
	for(int t=1 ; t <= T ; t++) {
		string num;
		cin >> num;
		int n = num.size();

		int i;
		for(i=0 ; i+1 < n && num[i] <= num[i+1] ; i++);
		if(i+1 < n && num[i] > num[i+1]) {
			while(i > 0 && num[i-1] == num[i]) {
				i--;
			}
			num[i]--;
			for(i++ ; i < n ; i++)
				num[i] = '9';
		}
		
		cout << "Case #" << t << ": ";
		i = 0;
		for(; num[i] == '0' && i < n ; i++);
		if(i == n)
			cout << 0;
		else for(; i < n ; i++)
			cout << num[i];
		cout << endl;
	}
}

// https://code.google.com/codejam/contest/3264486/dashboard#s=p1
