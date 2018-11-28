#define _CRT_SECURE_NO_DEPRECATE //suppress compilation warnings for VC++

#include <vector>
#include <utility>
#include <set>
#include <map>
#include <string>
#include <iostream>
#include <string.h>
#include <stdio.h>
#include <cmath>
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
ll getNine(int index) {
	if (index < 0) {return 0;}
	ll i = 9;
	while (index >0 ) {
		i = i * 10;
		i = i+9;
		index--;
	}
	return i;
}

ll getNineV2 (int index) {
	return pow(10,index) * 9;
}


ll isNumberTidy(ll num) {
	if(num /10 == 0) {
		return num;
	}
	ll oldNum = num;
	int index = 0;
	int modNum = num % 10;
	while(num != 0) {
		int newmodNum = num % 10;
		if (newmodNum > modNum) {
			ll powNum = pow(10, index);
			oldNum = oldNum - powNum;
			oldNum = oldNum / powNum;
			modNum = oldNum % 10;
			oldNum = oldNum * powNum;
			oldNum = oldNum + getNine(index-1); 
		} else {
			modNum = newmodNum;
		}
		num = num/10;
		index++;
	}


	return oldNum;

}

int main() {
	int a;
	int b = 1;
	cin>>a;
	while(b <= a) {
		ll num;
		cin >> num;
		cout<<"Case #"<<b<<": "<<isNumberTidy(num)<<endl;
		b++;
	}
}
