#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <assert.h>
#include <unordered_map>
#include <limits.h>
#include <assert.h>
#include <string.h>
#include <Util.h>

using namespace std;

enum { MAX = 1024 };

int I[MAX];
int Ik[MAX];
int IkL[MAX];
int IkU[MAX];
int IP[MAX][MAX];
int IPN[MAX];
int N, P;

bool debug = false;

void solve(int CASE) {
	int MAXK = -1;

	for (int i = 0; i < N; i++)
		IPN[i] = P;  // current count;

	int kitCount = 0;
	int k = 1;
	for (int i = 0; i < N; i++) {
		Ik[i] = I[i] * k;
		IkL[i] = int(Ik[i] * 0.9) - 1;
		IkU[i] = int(Ik[i] * 1.1) + 1;
		while (IkL[i] < Ik[i] * 0.9) IkL[i]++;
		while (IkU[i] > Ik[i] * 1.1) IkU[i]--;
			// [IkL[i], IkU[i]] is good;
	}
	if (debug) cout << endl;

	while (true) {
		bool end = false;
		for (int i = 0; i < N; i++) {
			if (IPN[i] == 0) { end = true; break; }
		}
		if (end) break;

		if (debug) cout << "-------- k = " << k << endl;
		for (int i = 0; i < N; i++) {
			if (debug) cout << "(" << IkL[i] << ", " << IkU[i] << ")" << " ";
		}
		if (debug) cout << endl;
		if (debug) cout << "PACKAGES: " << endl;
		for (int i = 0; i < N; i++) {
			if (debug) cout << "  ";
			for (int j = 0; j < IPN[i]; j++) {
				if (debug) cout << " " << IP[i][j];
			}
			if (debug) cout << endl;
		}

		int inCount = 0;
		bool restart = false;
		bool inrange = true;
		for (int i = 0; i < N; i++) {
			if (IP[i][0] < IkL[i]) {
				for (int j = 1; j < IPN[i]; j++)
					IP[i][j - 1] = IP[i][j]; 
				IPN[i]--;  // kill this;
				restart = true;
if (debug) cout << "RESTART" << IPN[i] << endl;

				break;
			} else if (IP[i][0] > IkU[i]) {
				inrange = false;
			}
		}
	if (debug) cout << "inrange = " << inrange << ", restart = " << restart << endl;
		if (restart) continue;

if (debug) cout << "HERE" << endl;
		if (inrange) {  // all in range;
			kitCount++;
			for (int i = 0; i < N; i++) {
				for (int j = 1; j < IPN[i]; j++)
					IP[i][j - 1] = IP[i][j]; 
				IPN[i]--;
				if (IPN[i] == 0) end = true;
			}
		} else {
if (debug) cout << "HERE2" << endl;
			k++;
			for (int i = 0; i < N; i++) {
				Ik[i] = I[i] * k;
				IkL[i] = int(Ik[i] * 0.9) - 1;
				IkU[i] = int(Ik[i] * 1.1) + 1;
				while (IkL[i] < Ik[i] * 0.9) IkL[i]++;
				while (IkU[i] > Ik[i] * 1.1) IkU[i]--;
					// [IkL[i], IkU[i]] is good;
			}
		}
	}
	cout << "Case #" << CASE << ": " << kitCount << endl;
}

int main(int argc, const char * argv[]) {

	istream &fin = cin;
	// fstream fin("tiny.in");

	int T;
	fin >> T;
	string s;
	int K;
	for (int CASE = 1; CASE <= T; CASE++) {
		fin >> N >> P;
		for (int i = 0; i < N; i++) {
			fin >> I[i];
		}
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < P; j++) {
				fin >> IP[i][j];
			}
			sort(IP[i], IP[i] + P);
		}
		solve(CASE);
	}
    return 0;
}
