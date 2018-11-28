#include <iostream>
#include <map>
#include <queue>
#include <stdio.h>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <vector>
#include <cmath>
#include <fstream>


using namespace std;

long long tidy_nums(long long N) {
	if (N<10) return N;
	
	while(N >= 0) {
		int nd = 0;
		long long N2 = N;
		while(N2) {nd++; N2/=10;}
		// cout<<nd<<" aa"<<endl;
		long long cur = N;
		int flag = 0;
		int count = 0;
		int prev = 10;
		while(cur) {
			count++;
			auto d = cur%10;
			if (d <= prev) {flag++;}
			else {
				N = cur*(long)pow(10, count-1) - 1;
				// cout <<"making N "<<4
				break;
			}
			cur /= 10;
			prev = d;
		}

		if (flag == count) {return N;}
	}
	return -1;
}

int main(void) {
	int t;
	long long n;
	
	vector<long long> v;

	ifstream myfile;
	myfile.open("B-large.in");
	myfile>>t;

	ofstream myfile2;
	myfile2.open("B-large.out");

	for (int i=0; i<t; i++) {
		myfile>>n;
		v.push_back(n);
		// cout<<"Case #"<<i+1<<": "<<tidy_nums(n)<<endl;
	}
	for (int i = 0; i<v.size(); i++) {
		myfile2<<"Case #"<<i+1<<": "<<tidy_nums(v[i])<<endl;
		cout<<"Case #"<<i+1<<": "<<tidy_nums(v[i])<<endl;
	}

	myfile2.close();
	// long long N = 111111111111111110;

	// cout<<tidy_nums(N)<<endl;

	return 0;
}