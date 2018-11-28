
#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <algorithm>
#include <math.h>

using namespace std;

struct stall {
	bool empty = true;
	long int LS, RS;
	long int idx, min, max;
};

bool cmpMin(const stall& ls, const stall& rs) {
	return ls.empty && rs.empty && ls.min < rs.min;
}

bool cmpMax(const stall& ls, const stall& rs) {
	return ls.empty && rs.empty && ls.max < rs.max;
}

vector<stall> getMinMaxElement(vector<stall> &list) {
	auto max_it = max_element(list.begin(), list.end(), cmpMin);
	long int tempMaxMin = max_it->min;

	vector<stall> result;
	for (long int i = 0, leng = list.size(); i < leng; i++) {
		if (list[i].empty && list[i].min == tempMaxMin) {
			result.push_back(list[i]);
		}
	}
	return result;
}

void setStallData(vector<stall> &list, long int left, long int right) {
	long int ls = 0, rs = right - left;
	for (long int i = 0, leng = rs + 1; i < leng; i++) {
		list[left + i].LS = ls++;
		list[left + i].RS = rs--;
		list[left + i].min = min(list[left + i].LS, list[left + i].RS);
		list[left + i].max = max(list[left + i].LS, list[left + i].RS);
	}
}

int main()
{
	ifstream fin("C-small-1-attempt0.in");
	ofstream fout("C-small-1-attempt0.out");

	int T;
	string tStr;
	getline(fin, tStr);
	istringstream is(tStr);
	is >> T;

	string sStr;
	long int N, K;

	for (int i = 1; i <= T; i++) {
		getline(fin, sStr);
		istringstream is(sStr);
		is >> N >> K;

		vector<stall> stallList(N);
		for (long int a = 0; a < N; a++){
			stallList[a].idx = a;
		}

		long int idx;
		vector<long int> ocStIdxList;
		for (long int b = 0; b < K; b ++) {
			long int leftIdx = 0, rightIdx = 0;
			for (long int c = 0, leng = ocStIdxList.size(); c <= leng; c++) {
				if (c < leng && ocStIdxList[c] == leftIdx) {
					leftIdx++;
					continue;
				}

				rightIdx = (c == leng) ? N-1 : ocStIdxList[c]-1;

				if (leftIdx <= rightIdx) {
					setStallData(stallList, leftIdx, rightIdx);
				} 
				if (c < leng) leftIdx = ocStIdxList[c] + 1;
			}

			vector<stall> minMaxList = getMinMaxElement(stallList);
			auto max_it = max_element(minMaxList.begin(), minMaxList.end(), cmpMax);
			idx = minMaxList[distance(begin(minMaxList), max_it)].idx;
			stallList[idx].empty = false;

			ocStIdxList.push_back(idx);
			sort(ocStIdxList.begin(), ocStIdxList.end());
		}
		
		fout << "Case #" << i << ": " << stallList[idx].max << " " << stallList[idx].min << endl;
	}

	fin.close();
	fout.close();
	return 0;
}
