#include <iostream>
#include <fstream>
#include <string>
//#include <vector>
//#include <algorithm>
#include <queue>
using namespace std;

void main(){
	int T;
	ifstream infile;
	infile.open("C-small-1-attempt4.in");
	if (!infile.is_open()) cout << "Failed to load file!" << endl;

	ofstream outfile;
	outfile.open("output3-1000123.txt");
	infile >> T;
	int i = T;
	while (i){
		int N, K;
		infile >> N >> K;
		priority_queue<long long> mypq;
		mypq.push(N);
		long long n = 0;
		long long j = 0;
		while (j < K){
			n = mypq.top();
			mypq.pop();
			mypq.push((n - 1) / 2);
			mypq.push(n / 2);
			j++;
		}
		if (K == 1) outfile << "Case #" << T - i + 1 << ": " << ((N) / 2) << " " << ((N - 1) / 2) << endl;
		//else if (K == 2) outfile << "Case #" << T - i + 1 << ": " << ((N) / 2) << " " << ((N - 1) / 2) << endl;
		//else if (K >((N + 1) / 2)) outfile << "Case #" << T - i + 1 << ": 0 0" << endl;
		else outfile << "Case #" << T - i + 1 << ": " << (n / 2) << " " << ((n - 1) / 2) << endl;
		i--;
	}
	infile.close();
	outfile.close();
	system("pause");
}