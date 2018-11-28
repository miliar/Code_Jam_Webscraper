#include <iostream>
#include <fstream>
//#include <algorithm>
#include <vector>
#include <math.h>

using namespace std;

long long int getTidyNum(long long int num)
{
	long long int ans = 0;
	//cout << "=====" << endl;
	//cout << num << endl;
	/// split to digit array
	vector<int> vec;
	while (((float)num / 10) > 0) {
		vec.push_back(num % 10);
		num /= 10;
	}
#if 0
	for (int i = 0; i < vec.size(); i++)
		cout << vec[i] << " ";
	cout << endl;
#endif
	for (int i = vec.size()-1 ; i > 0; i--) {
		bool blLarger = false;

		if (vec[i] > vec[i-1]) {
			while (1) {
				if (i == vec.size() - 1)
					break;

				if (vec[i] == vec[i+1])
					i++;
				else
					break;
			}

			vec[i]--;

			for (int j = i-1; j >=0; j--) {
				vec[j] = 9;
			}
		}
	}
#if 0
	for (int i = 0; i < vec.size(); i++)
		cout << vec[i] << " ";
	cout << endl;
#endif	
	for (int i = vec.size() -1; i >= 0; i--) {
		ans = ans*10 + vec[i];
	}
	//cout << ans << endl;

	return ans;
}

int main()
{
	ifstream File;
	File.open("/Users/lester/Downloads/B-large.in");
	//File.open("./test.in");

	if (!File.is_open()) {
		cout << "faild" << endl;
		return 0;
	}

	int Times = -1;

	File >> Times;
	//cout << Times << endl;

	for (int i = 1; i <= Times; i++) {	
		long long int number;
		File >> number;
		//cout << "#"<< number << endl;
		//getTidyNum(number);
		cout << "Case #" << i << ": "<< getTidyNum(number) << endl;
	}

	return 0;
}
