#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <queue>
#include <numeric>
#include <map>

#pragma warning(disable:4996)
using namespace std;

int T;
string N;

bool check(string ret) {
	for (int i = 0; i < ret.size() - 1; ++i)
		if (ret[i] > ret[i + 1])
			return false;
	return true;
}

bool check(int checked) {
	string ret = to_string(checked);
	for (int i = 0; i < ret.size()-1; ++i) {
		if (ret[i] > ret[i + 1]) 
			return false;
	}
	return true;
}

string non_zero_tiny(string tiny) {
	string ret = tiny;
	for (int i = 0; i < tiny.size(); ++i) {
		int j = i;
		while (j >= 1 && ret[j - 1] > ret[j]) {
			ret[j - 1] = ret[j];
			j--;
		}
	}
	return ret;
}

char minus_char(char c) {
	int num = c - '0';
	num--;
	c = num + '0';
	return c;
}

int main(void)
{
	freopen("./GoogleCodeJam/Input/B-small-attempt5.in", "r", stdin);
	freopen("./GoogleCodeJam/Output/b-small_ans.txt", "w", stdout);
	cin >> T;

	for (int t = 0; t < T; ++t) {
		cin >> N;
		//string ret = N;
		int ret = stoi(N);
		for (int i = ret; i >= 0; --i) {
			if (check(i)) {
				cout << "Case #" << t + 1 << ": " << to_string(i) << endl;
				break;
			}
		}
	}
}
//
//
//int size = N.size();
//if (N.size() != 1) {
//	for (int i = 0; i < N.size() - 1; ++i) {
//		if (ret[i] > ret[i + 1]) {
//			char num_c = minus_char(ret[i]);
//			ret[i] = num_c;
//			if (ret[i] == '0' && i != 0)
//				ret[i] = '9';
//			int k = i - 1;
//			while (k >= 0 && ret[k] > num_c) {
//				ret[k] = minus_char(ret[k]);
//				if (ret[k] == '0' && k != 0)
//					ret[k] = '9';
//				k--;
//			}
//			for (int j = i + 1; j < N.size(); ++j)
//				ret[j] = '9';
//		}
//	}
//	if (ret[0] == '0') ret.erase(0, 1);
//	cout << "Case #" << t + 1 << ": " << ret << endl;
//}



		/*bool zero_flag = false;
		int loc;
		for (int i = 0; i < N.size(); ++i) {
			int j = i;
			while (j >= 1 && ret[j-1] > ret[j]) {
				if(ret[j] != '0')
					ret[j-1] = ret[j];
				else {
					if (!zero_flag) {
						zero_flag = true;
						loc = j;
					}
					
				}
				j--;
			}
			if (zero_flag) {
				for (int k = loc + 1; k < N.size(); ++k) 
					ret[k] = '9';
				break;
			}
			if (ret.size() != 1 && i == ret.size() - 1 && N[i - 1] > N[i]) ret[i] = '9';
		}

		if (ret[0] == '0') ret.erase(0, 1);

		cout << "Case #" << t + 1 << ": " << ret << endl;*/
	//}

//cout << "Case #" << t + 1 << ": " << ret << endl;