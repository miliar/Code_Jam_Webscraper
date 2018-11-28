// ProblemB.cpp : コンソール アプリケーションのエントリ ポイントを定義します。
//

#include <iostream>
#include <vector>
#include <string>

using namespace std;

string print_v(vector<int> v)
{
	string result;
	for (int i : v) {
		result += to_string(i) + ", ";
	}
	return result;
}

auto tidy_number(vector<int> reverse_number, const int index) -> decltype(reverse_number)
{
	// cout << "tidy_number {" << print_v(reverse_number) << "} " << index << endl;

	if (reverse_number.size() == (index + 1)) {
		if (reverse_number.back() == 0) {
			reverse_number.pop_back();
		}
		return reverse_number;
	}

	int left = reverse_number[index];
	int right = reverse_number[index + 1];
	if (left < right) {
		for (int i = 0; i <= index; i++) {
			reverse_number[i] = 9;
		}
		reverse_number[index + 1] -= 1;
	}
	return tidy_number(reverse_number, index + 1);
}

int main()
{
	int T;
	cin >> T;
	// cout << "T " << T << endl;

	for (int i = 0; i < T; i++) {
		string N;
		cin >> N;
		// cout << "N " << N << endl;

		vector<int> reverse_number;
		for (auto itr = N.rbegin(); itr != N.rend(); itr++) {
			reverse_number.push_back((*itr) - '0');
		}
		// cout << "reverse_number ";
		for (int e : reverse_number) {
			// cout << e << ", ";
		}
		// cout << endl;

		cout << "Case #" << (i + 1) << ": ";
		auto v = tidy_number(reverse_number, 0);
		for (auto itr = v.rbegin(); itr != v.rend(); itr++) {
			cout << *itr;
		}
		cout << endl;
	}

    return 0;
}

