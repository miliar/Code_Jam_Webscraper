#include <iostream>
#include <string>
#include <cstdint> 
#include <stdint.h>
#include <chrono>
#include <cstdint>
#include <fstream>
using namespace std;
int main() {
	ifstream myfile;
	myfile.open("./C-large.txt");
	fstream myfile2;
	myfile2.open("./output.txt");
	string s;
	int t;
	myfile >> t;
	uint64_t n[100], k[100];
	for (int i = 0;i<t;i++) {
		myfile >> n[i] >> k[i];
	}

	for (int i = 0;i<t;i++) {
		myfile2 << "Case #" << i + 1 << ": ";
		uint64_t dev = 1;
		uint64_t prevDev = 0;
		while (dev<k[i]) {
			prevDev = dev;
			dev = dev * 2 + 1;
		}
		uint64_t mean = (n[i] - prevDev) / (prevDev + 1);
		uint64_t remain = (n[i] - prevDev) % (prevDev + 1);
		uint64_t choseInterval = mean;
		if ((k[i] - prevDev) <= remain) {
			choseInterval = mean + 1;
		}
		if (choseInterval % 2 == 0) {
			myfile2 << choseInterval / 2 << " " << choseInterval / 2 - 1;
		}
		else {
			myfile2 << choseInterval / 2 << " " << choseInterval / 2;
		}
		myfile2 << endl;
	}
	return 0;
}

