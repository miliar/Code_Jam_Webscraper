#include <iostream>
#include <fstream>
#include <string>
using namespace std;

bool isTidy(long long n){
	int c, p = n % 10;
	n /= 10;
	while (n > 0){
		c = n % 10;
		if (c > p) return false;
		p = c;
		n /= 10;
	}
	return true;
}

long long calTidy(long long n){
	if (isTidy(n)) return n;
	long long div = 10;
	long long tempAns = n - (n%div) - 1;
	while (!isTidy(tempAns)){
		div *= 10;
		tempAns = n - (n%div) - 1;
	}
	return tempAns;
}

void main(){
	int T;
	ifstream infile;
	infile.open("B-large.in");
	if (!infile.is_open()) cout << "Failed to load file!" << endl;

	ofstream outfile;
	outfile.open("output2-L.txt");
	infile >> T;
	int i = T;
	while (i){
		long long K;
		infile >> K;
		long long answer = calTidy(K);
		outfile << "Case #" << T - i + 1 << ": " << answer << endl;
		i--;
	}
	infile.close();
	outfile.close();
	system("pause");
}