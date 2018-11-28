#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <math.h>
#define PI 3.1415926535897932384626433832795
using namespace std;

class Pancake {
public:
	int R;
	int H;
};
double GetMaxSyrupSize(int index, int from, int K, int N, vector<Pancake>* pancakes) {
	if (index == K)
		return 0;
	double result = 0;
	for (int i = from; i < N - K + index + 1; i++) {
		double temp = PI * 2 * (*pancakes)[i].R * (*pancakes)[i].H;
		if (index == 0)
			temp += PI * pow((*pancakes)[i].R, 2);
		temp += GetMaxSyrupSize(index + 1, i + 1, K, N, pancakes);
		if (temp > result)
			result = temp;
	}
	return result;
}

void SolveA(ifstream* inp, ofstream* out) {
	int N, K;
	*inp >> N >> K;
	vector<Pancake> pancakes;
	for (int i = 0; i < N; i++) {
		Pancake p;
		*inp >> p.R;
		*inp >> p.H;
		pancakes.push_back(p);
	}
	sort(pancakes.begin(), pancakes.end(), [](const Pancake& lhs, const Pancake& rhs)
	{
		return lhs.R > rhs.R;
	});
	double result = GetMaxSyrupSize(0, 0, K, N, &pancakes);
	(*out).precision(numeric_limits<double>::digits10 + 1);
	*out << result;
}

void main() {
	ifstream input = ifstream(fopen("d:\\input.txt", "r"));
	ofstream output = ofstream(fopen("d:\\output.txt", "w"));
	int T;
	input >> T;
	for (int i = 0; i < T; i++) {
		output << "Case #" << (i + 1) << ": ";
		SolveA(&input, &output);
		output << endl;
	}
	//system("pause");
}
