#include <iostream>
#include <vector>
#include <climits>


using namespace std;

int findMin(const vector<int>& d, int end){
	int min = INT_MAX, idx = 0;
	for (int i = 0; i < end; ++i){
		if (d[i] < min){
			idx = i;
			min = d[i];
		}
	}
	return idx;
}

int getLeftMax(const vector<int>& d, int start)
{
	int max = -1;
	for (int i = start; i < d.size(); ++i)
		if (d[i] > max) max = d[i];
	return max;
}
void minusOne(vector<int>& d, int start){
	int carry = -1;
	for (int i = start; i < d.size(); ++i)
		if (d[i]+carry < 0)
			d[i] = 9;
		else{
			d[i]+=carry;
			carry = 0;
		}
}
int main()
{
	int test = 0;
	cin >> test;
	long N = 0;
	vector<int> digits;
	for (int t = 0; t < test; ++t){
		cin >> N;
		digits.clear();
		for (int i = 0; N != 0; ++i){
			digits.push_back(N % 10);
			N /= 10;
		}
//for (int i = 0; i<digits.size(); ++i)
//cout << digits[i];
//cout << endl;
		int n = digits.size();
		for (int i = 0; i < n; ++i){
			int leftMax = getLeftMax(digits, i+1);
			if (leftMax > digits[i]){
				minusOne(digits, i+1);
				for (int k = 0; k <=i; ++k)
					digits[k] = 9;
			}
		}
	
	int startDigit = digits.size()-1;
	cout << "Case #"<<t+1 << ": ";
	while (digits[startDigit] == 0)
		--startDigit;
	while (startDigit >=0)
		cout << digits[startDigit--];
	cout << endl;
	}
	return 0;
}
