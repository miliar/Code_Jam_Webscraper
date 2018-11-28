#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <math.h>

using std::ifstream; using std::ofstream;
using std::endl;
using std::vector;

typedef unsigned long long ull;

void createStalls(ull, vector<int>&);
void outStalls(const vector<int>&);
void largestOpening(const vector<int>&, ull&, ull&);

int main() {
	ifstream fin("C-small-1-attempt1.in");
	ofstream fout("C-small-1-attempt1.out");

	int T;
	fin >> T;

	for (int c = 0; c < T; ++c) {
		ull z = 0, y = 0, N, K;
		fin >> N; 
		fin >> K; //ppl 

		if (N == K) {
			fout << "Case #" << c + 1 << ": 0 0" << endl;
			continue;
		}
		N += 2; //total stalls

		/*
			0 = stall empty
			1 = stall in use
			stall[0] & stall[n] gaurded (in use)
		*/
		vector<int> stalls;
		createStalls(N, stalls);

		/*
			bestStall = stall to be updated
			begLoc = beggining location for longest opening
			length = size of largest opening
		*/
		ull bestStall, begLoc, length;

		const ull ppl = K;
		for (ull i = 0; i < ppl; ++i) {
			ull ls, rs;
			largestOpening(stalls, begLoc, length);
			
			//stall to use, element in vector (-1 before using)
			bestStall = static_cast<int>(ceil(length / 2.0));
			
			rs = length - bestStall;
			ls = 0 + (bestStall - 1);

			//testing
			//std::cout << "Ls: " << ls << "   Rs:" << rs << endl << "Len: " << length << " Best: " << bestStall << endl;

			stalls[bestStall - 1 + begLoc] = 1;
			y = std::max(ls, rs);
			z = std::min(ls, rs);

			//for testing
			//outStalls(stalls);

		}

		fout << "Case #" << c + 1 << ": " << y << " " << z << endl;

		//test
		//std::cout << endl << endl << "NEW\n";
	}

	fin.close();
	fout.close();

	return 0;
}

void createStalls(ull num, vector<int> &stalls) {
	for (ull i = 0; i < num; ++i) {
		if (i == 0)
			stalls.push_back(1);
		else if (i == num - 1)
			stalls.push_back(1);
		else
			stalls.push_back(0);
	}
}

void outStalls(const vector<int> &stalls) {
	const ull size = stalls.size();
	for (ull i = 0; i < size; ++i)
		std::cout << stalls[i] << " ";
	std::cout << endl;
}

void largestOpening(const vector<int> &stalls, ull &begLoc, ull &length) {
	const ull size = stalls.size();
	length = 0;
	begLoc = 0;
	ull tmpBegLoc = 0;
	ull tmpLength = 0;
	for (ull i = 0; i < size; ++i) {
		if (stalls[i] == 1) {
			if (tmpLength > length) { //assign
				length = tmpLength;
				begLoc = tmpBegLoc;
			}

			tmpLength = 0;
			tmpBegLoc = 0;
		}
		else {
			++tmpLength;
			if (tmpBegLoc == 0)
				tmpBegLoc = i;
		}
	}
}