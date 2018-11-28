//============================================================================
// Name        : JamBSmall.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <cstdlib>
#include <unordered_set>
#include <unordered_map>
#include <list>
#include <vector>
#include <cmath>
#include <string>
#include <climits>
#include <algorithm>
using namespace std;

int main() {
	int T;
	cin>>T;
	for (int t = 0; t < T; t++) {
		int N;
		int colors [6];
		cin>>N;
		cin>>colors [0];
		cin>>colors [1];
		cin>>colors [2];
		cin>>colors [3];
		cin>>colors [4];
		cin>>colors [5];
		int RYB [3];
		string RYBColorChars = "RYB";
		RYB[0] = colors[0];
		RYB[1] = colors[2];
		RYB[2] = colors[4];
		bool impossible = false;
		for(int i=0;i<3;i++) {
			if(RYB[i]>N/2) {
				impossible = true;
			}
		}
		if(impossible) {
			cout << "Case #" << t + 1 << ": IMPOSSIBLE" << endl;
			continue;
		}
		cout << "Case #" << t + 1<<": ";
		int totalCount = RYB[0]+RYB[1]+RYB[2];
		//cout<<RYB[0]<<" "<<RYB[1]<<" "<<RYB[2]<<endl;
		int lastChoice=-1;
		string lastTwo;
		char first;
		for(int i=0;i<totalCount;i++) {
			int maxIndex = 0, max = 0;
			for(int j=0;j<3;j++) {
				if(RYB[j]>max && j!=lastChoice) {
					max = RYB[j];
					maxIndex = j;
				}
			}
			lastChoice = maxIndex;
			RYB[maxIndex]--;
			if(i<totalCount-2) {
				if(i==0) {
					first = RYBColorChars[maxIndex];
				}
				cout<<RYBColorChars[maxIndex];
			}
			else {
				lastTwo+=RYBColorChars[maxIndex];
			}

		}
		if(lastTwo.size() > 0 && lastTwo[lastTwo.size()-1]==first) {

			reverse(lastTwo.begin(), lastTwo.end());
		}
		cout<<lastTwo<<endl;


	}
	return 0;
}
