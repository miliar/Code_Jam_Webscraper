#define _CRT_SECURE_NO_DEPRECATE //suppress compilation warnings for VC++

#include <vector>
#include <utility>
#include <set>
#include <map>
#include <string>
#include <iostream>
#include <string.h>
#include <stdio.h>
using namespace std;
//Common data types in shortcut form
typedef long long ll; 
typedef vector<int> vi;//vector of ints
typedef pair<int, int> ii; //int int
typedef vector<ii> vii; //vector of pair of int int
typedef set<int> si;
typedef map<string, int> msi; //map from string to int

//Basic forloop, including the starting(a) and ending number(b) using i as the local variable
#define REP(i, a, b) \
	for(int i = int(a); i <= int(b); i++)

//Basic Traverse Vector(c) using it as the pointer
#define TRvi(c, it) \
	for(vi::iterator it = (c).begin(); it != (c).end(); it++)

// //Traverse a vector of pairrpair
// #define TRvii(c, it) \
// 	for(vii::iterator it = (c).begin(); it != (c).end(); it++)

// //Traverse A map of string to int
// #define TRmsi(c, it)
// 	for(msi::iterator it = (c).begin(); it != (c).end(); it++)

// #define INF 2000000000 // 2 billion
// // If you need to recall how to use memset:
// #define MEMSET_INF 127 // about 2B
// #define MEMSET_HALF_INF 63 // about 1B
//memset(dist, MEMSET_INF, sizeof dist); // useful to initialize shortest path distances
//memset(dp_memo, -1, sizeof dp_memo); // useful to initialize DP memoization table
//memset(arr, 0, sizeof arr); // useful to clear array 

bool ifAllPositive(vi c) {
	TRvi(c, it) {
		if(*it == 0) {
			return false;
		}
	}
	return true;
}

void flipPancake(vi & c, int index, int flipNum) {
	for(int i = index; i < index + flipNum; i++) {
		if(c.at(i) == 0) {
			c.at(i) =1;
		} else {
			c.at(i) = 0;
		}
	}
}


int main() {
	int a;
	int b = 1;
	cin>>a;
	while(b <= a) {
		string pancake;
		vi newPan;
		cin>>pancake;
		int numFlips = 0;
		int flipNum;
		cin>>flipNum;
		for (int i = 0; i < pancake.size(); i++) {
			if(pancake.at(i) == '+') { 
				newPan.push_back(1);

			} else {
				newPan.push_back(0);
			}
		}

		for(int i = 0; i<= newPan.size()-  flipNum; i++) {
			if(newPan.at(i) == 0) {
				flipPancake(newPan, i, flipNum);
				numFlips++;
			}
		}
		if(ifAllPositive(newPan)) {
			cout<<"Case #"<<b<<": "<<numFlips<<endl;
		} else {
			cout<<"Case #"<<b<<": IMPOSSIBLE"<<endl;
		}
		b++;
	}
}
