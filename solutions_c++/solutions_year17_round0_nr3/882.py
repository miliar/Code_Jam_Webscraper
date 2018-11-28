#include <iostream>
#include <fstream>
#include <sstream>
using namespace std;

string BathroomStalls(string n, string k) {
	int nl = n.length(), kl = k.length();
	int* bn = new int[nl];
	int* bk = new int[kl];
	for(int i = 0; i < nl; i++)
		bn[i] = (int)n[i] - (int)'0';
	for(int i = 0; i < kl; i++)
		bk[i] = (int)k[i] - (int)'0';

	if(kl == nl) {
		bool equal = true;
		for(int i = 0; equal && i < nl; i++)
			if(bn[i] != bk[i])
				equal = false;
		if(equal)
			return "0 0";
	}

	bool* bn2 = new bool[4*nl];
	bool* bk2 = new bool[4*kl];

	int firstDigitN = 0, nl2 = 0;
	while(firstDigitN < nl-1 || bn[nl-1] > 0) {
		for(int j = firstDigitN; j < nl-1; j++) {
			if(bn[j] % 2 == 1) {
				bn[j+1] += 10;
				bn[j]--;
			}
			bn[j]/=2;

			if(j == firstDigitN && bn[j] == 0)
				firstDigitN++;
		}
		bn2[nl2++] = (bn[nl-1] % 2 == 1);
		bn[nl-1]/=2;
	}

	int firstDigitK = 0, kl2 = 0;
	while(firstDigitK < kl-1 || bk[kl-1] > 0) {
		for(int j = firstDigitK; j < kl-1; j++) {
			if(bk[j] % 2 == 1) {
				bk[j+1]+=10;
				bk[j]--;
			}
			bk[j]/=2;

			if(j == firstDigitK && bk[j] == 0)
				firstDigitK++;
		}
		bk2[kl2++] = bk[kl-1] % 2;
		bk[kl-1]/=2;
	}

	int power2 = kl2-1;

	int firstOneN = power2;
	while(!bn2[firstOneN])
		bn2[firstOneN++] = 1;
	bn2[firstOneN] = 0;
	int firstZeroN = 0;
	while(bn2[firstZeroN])
		bn2[firstZeroN++] = 0;
	bn2[firstZeroN] = 1;
	if(bn2[nl2-1] == 0)
		nl2--;

	bk2[power2] = 0;
	int firstZeroK = 0;
	while(bk2[firstZeroK])
		bk2[firstZeroK++] = 0;
	bk2[firstZeroK] = 1;
	if(bk2[power2] == 0)
		kl2--;

	bool kIsBigger = false, kIsSmaller = false;
	if(power2 < kl2)
		kIsBigger = true;
	else {
		for(int i = power2-1; !kIsBigger && !kIsSmaller && i >= 0; i--) {
			if(bk2[i] && !bn2[i])
				kIsBigger = true;
			else if(!bk2[i] && bn2[i])
				kIsSmaller = true;
		}
	}

	int nnl2 = nl2 - power2;
	bool* bnn2 = new bool[nnl2+1];
	for(int i = 0; i < nnl2; i++)
		bnn2[i] = bn2[i+power2];
	bnn2[nnl2] = 0;
	if(!kIsBigger) {
		int firstZeroNN = 0;
		while(bnn2[firstZeroNN])
			bnn2[firstZeroNN++] = 0;
		bnn2[firstZeroNN] = 1;
		if(bnn2[nnl2] == 1)
			nnl2++;
	}

	bool odd = bnn2[0];

	int* bnn = new int[nl];
	for(int i = 0; i < nl; i++)
		bnn[i] = 0;
	int* temp2Power = new int[nl];
	temp2Power[0] = 1;
	for(int i = 1; i < nl; i++)
		temp2Power[i] = 0;

	for(int i = 1; i < nnl2; i++) {
		if(bnn2[i]) {
			for(int j = 0; j < nl; j++) {
				bnn[j] += temp2Power[j];
				if(bnn[j] > 9) {
					bnn[j] -= 10;
					bnn[j+1]++;
				}
			}
		}
		for(int j = nl-1; j >= 0; j--) {
			temp2Power[j] *= 2;
			if(temp2Power[j] > 9) {
				temp2Power[j] -= 10;
				temp2Power[j+1]++;
			}
		}
	}

	int nnl = nl;
	while(bnn[nnl - 1] == 0)
		nnl--;
	if(nnl == 0)
		nnl++;

	ostringstream s;
	for(int i = nnl-1; i >= 0; i--)
		s << bnn[i];
	s << " ";
	if(!odd) {
		bnn[0]--;
		int firstPositive = 0;
		while(bnn[firstPositive] < 0) {
			bnn[firstPositive++] += 10;
			bnn[firstPositive]--;
		}
		if(bnn[nnl-1] == 0 && nnl > 1)
			nnl--;
	}
	for(int i = nnl-1; i >= 0; i--)
		s << bnn[i];
	
	return s.str();
}

int main() {
	ifstream fin;
	fin.open("C-large.in");
//	fin.open("C-small-2-attempt1.in");
//	fin.open("C-small-2-attempt0.in");
//	fin.open("C-small-1-attempt0.in");
//	fin.open("C-small-practice.in");
//	fin.open("C-large-practice.in");

	ofstream fout;
	fout.open("C-large.out");
//	fout.open("C-small-2-attempt1.out");
//	fout.open("C-small-2-attempt0.out");
//	fout.open("C-small-1-attempt0.out");
//	fout.open("C-small-practice.out");
//	fout.open("C-large-practice.out");

	int t;
	fin >> t;
	for (int i = 1; i <= t; ++i) {
		string n, k;
		fin >> n;
		fin >> k;

		fout << "Case #" << i << ": " << BathroomStalls(n, k) << endl;
	}
	fin.close();
	fout.close();
	return 0;
}

