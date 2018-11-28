#include <vector>
#include <iostream>
#include <map>
#include <functional>
#include <algorithm>

using namespace std;

void output(const std::map<long long, long long, greater<long long>>& temp,  long long people) {
	cout << "* " << people << endl;
	for (auto it = temp.begin(); it != temp.end(); ++it) {
		cout << it->first << " => " << it->second << endl;
	}
}

void main() {
	size_t testCount;
	cin >> testCount;

	long long stalls, people;
	for (size_t i = 0; i < testCount; i++) {
		cin >> stalls >> people;

		//cout << stalls << " " << people << endl;

		std::map<long long, long long, greater<long long>> temp;
		temp[stalls] = 1;

		for (;;) {

			map<long long, long long, greater<long long>>::iterator it = temp.begin();

			long long num = it->second;
			long long value = it->first;
			value -= 1;

			long long one = value / 2;
			long long two = value - one;

			if (people <= num) { 
				cout << "Case #" << i + 1 << ": " << two << " " << one << endl;
				break;
			}

			temp.erase(it);

			if (temp.count(one)) {
				temp[one] += num;
			} else {
				temp[one] = num;
			}
			if (temp.count(two)) {
				temp[two] += num;
			} else {
				temp[two] = num;
			}

			people -= num;

			//output(temp, people);
		}

		//cout << "---------------" << endl;
	}

}