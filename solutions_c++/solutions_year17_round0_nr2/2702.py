#include <bits/stdc++.h>

using namespace std;

int main()
{
	int t;
	cin >> t;
	for(int k = 1; k <= t; k++) {
		string num;
		cin >> num;
		int i = 0;
		int n = num.length();
		while(i < n-1 && (num[i] < num[i + 1] || num[i] == num[i + 1]) ) {
			i++;
		}
		if(i != n - 1) {
			while(i > 0 && num[i] == num[i-1]){
				i--;
			}
			num[i] = num[i] - 1;
			for(int j = i + 1; j < n; j++)
				num[j] = '9';
			num.erase(0, num.find_first_not_of('0'));
		}
		cout << "Case #" << k << ": " << num << endl;
	}
}