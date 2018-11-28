#include <iostream>
#include <fstream>
#include <string>
#include <cstdlib>
#include <iomanip>
#include <deque>

using namespace std;

deque<int> longToStr(long i) {
	deque<int> v;
	int lastDig = 0;
	while (i > 0) {
		int dig = i % 10;
		v.push_front(dig);
		i = i / 10;
	}
	return v;
}

void printVec(deque<int> v) {
	for (int j = 0; j < v.size(); j++) {
		cout << v[j] << " ";		
	}
	cout << endl;
}

long findTidy(long i) {
	deque<int> vec = longToStr(i);
	int pos = 1;
	while (pos < vec.size()) {
		if (vec[pos] < 0) {
			if (pos == 0) {
				vec[pos] = 0;
				pos++;
			} else {
				--vec[pos-1];
				for (int j = pos; j < vec.size(); j++) {
					vec[j] = 9;
				}
				pos--;
			}
		} else if (vec[pos] < vec[pos-1]) {
			--vec[pos];
		} else {
			pos++;
		}
	}

	long mult = 1;
	long sum = 0;
	for (int i = vec.size()-1; i >= 0; --i) {
		sum += vec[i]*mult;
		mult *= 10;
	}
	return sum;
	
}

int main() {
	ifstream inData("small.in");
	ofstream outData("output-small.txt");
	int num;
	inData >> num;
	for(int i = 0; i < num; i++) {
		long n;
		inData >> n;
		long tidyN = findTidy(n);
		outData << "Case #" << i+1 << ": " << tidyN << endl;
	}
	return 0;
}

