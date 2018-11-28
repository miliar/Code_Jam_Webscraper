#include <iostream>
#include <cmath>
#include <vector>
using namespace std;

class solution {
public:
	long tidy(long N) {
		vector<int> digit;
		bool flag = false;
		for (long num = N; num != 0; num /= 10) {
			digit.push_back(num%10);
		}
		reverse(digit.begin(), digit.end());
		int i = 0;
		for (; i < digit.size()-1; i++) {
			if (digit[i+1] < digit[i]) {
				flag = 1;
				break;
			}
		} 
		if (flag) {
			while ((i > 0) && (--digit[i]<digit[i-1])) {i--;}
			if (i == 0) digit[i]--;
			for (i++; i < digit.size(); i++) {
				digit[i] = 9;
			}
		}
		long res = 0;
		for (i = 0; i<digit.size(); i++) {
			res = res*10 + digit[i];
		}
		return res;
	}
};

int main() {
	long N;
	int cnt;	
	solution A;
	cin>>cnt;
	for (int i = 1; i<=cnt; i++) {
		cin>> N;
		cout<<"Case #" << i << ": " << A.tidy(N) << endl;
	}
}