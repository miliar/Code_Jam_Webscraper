#include<iostream>
#include<fstream>
using namespace std;
void binary(int n, int k,int &max,int &min);
int main() {
	int T;
	ifstream input;
	ofstream output;
	input.open("h.txt");
	output.open("answers2.txt");
	input >> T;
	for (int t = 1; t <= T; t++) {
		int max = 0;
		int min = 0;
		int n, k;
		input >> n >> k;
		binary(n, k, max, min);
		output << "Case #" << t << ": " << max <<" "<< min<<endl;
	}
	system("pause");
	return 0;
}
void binary(int n, int k,int& max,int & min) {
	int level = log2(k) + 1;
	int lower = pow(2,level - 1)-1;
	int higher = (lower + 1) * 2 - 1;
	int place = k - lower;
	min =(n-k) /int(pow(2,level));
	int rem = n - min*pow(2, level) - higher;
	max = min;
	if (rem >= place)
		max++;
	return;
}