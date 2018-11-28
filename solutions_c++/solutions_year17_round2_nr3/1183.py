#include "stdafx.h"

#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>
#include <stdio.h>
#include <iomanip>
using namespace std;
typedef long long ll;

int T;
vector<vector<int> > carte;
vector<pair<int, int> > H;
int N, Q;

double proc(pair<int, int> horse, int id) {
	//cout << "Chemin de " << id - 1 << " a " << id << endl;
	pair<int, int> horseA = horse, horseB = H[id - 1];
	if (id == N) {
		return 0;
	}
	
	double wayA = -1, wayB = -1;
	//cout << "CAN A ? " << horseA.first << " " << carte[id - 1][id] << endl;
	if (horseA.first >= carte[id - 1][id]) {
		wayA = (double)carte[id - 1][id] / (double)horseA.second;
		//cout << "A:" << wayA << endl;
		horseA.first -= carte[id - 1][id];
		wayA += proc(horseA, id + 1);
	}
	//cout << "CAN B ? " << horseB.first << " " << carte[id - 1][id] << endl;
	if (horseB.first >= carte[id - 1][id]) {
		wayB = (double)carte[id - 1][id] / (double)horseB.second;
		//cout << "B:" << wayB << endl;
		horseB.first -= carte[id - 1][id];
		wayB += proc(horseB, id + 1);
	}

	//cout << "A:" << wayA << " " << "B:" << wayB << endl;
	if (wayA == -1) {
		return wayB;
	}
	if (wayB == -1) {
		return wayA;
	}
	return (wayA < wayB) ? wayA : wayB;
}

int main()
{
	cin >> T;
	for (int testcase = 0; testcase < T; testcase++) {
		cin >> N >> Q;
		H.clear();
		for (int i = 0; i < N; i++) {
			int tmpe, tmps;
			pair<int, int> tmp;
			cin >> tmpe >> tmps;
			tmp = pair<int, int>(tmpe, tmps);
			H.push_back(tmp);
		}
		carte.clear();
		carte = vector<vector<int> >(N, vector<int>(N));
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				int tmp;
				cin >> tmp;
				carte[i][j] = tmp;
			}
		}
		vector<pair<int, int> > deliv;
		for (int i = 0; i < Q; i++) {
			int tmpu, tmpv;
			cin >> tmpu >> tmpv;
			pair<int, int> tmp = pair<int, int>(tmpu-1, tmpv-1);
			deliv.push_back(tmp);
		}
		/*
		double time = 0;
		pair<int, int> curH = H[0];
		for (int i = 0; i < N-1; i++) {
			if (curH.first >= carte[i][i + 1]) {
				if (curH.second > H[i].second) {
					//keep horse
				}
				else {
					curH = H[i];
				}
			}
			double Hspeed = H[i].second;
			double dist = carte[i][i + 1];
			time += dist / Hspeed;
			curH.first -= carte[i][i + 1];
		}
		*/
		cout << fixed << setprecision(6) << "Case #" << testcase + 1 << ": " << proc(H[0], 1) << endl;
	}
	return 0;
}

