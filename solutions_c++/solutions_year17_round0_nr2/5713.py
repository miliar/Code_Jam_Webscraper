// B_TidyNumbers.cpp

#include <iostream>
#include <vector>
#include <queue>
#include <string>
#include <math.h>
#include <functional>
#include <sstream>
#include <cstring>
#include <set>
#include <map>
#include <cstdio>
#include <algorithm>
#include <bitset> 	
#include <ctime> 
#include <chrono>
#include <thread> 	
using namespace std;

// Shortcuts for "common" data types in contests

#define rep(i, a, b) for(int i = a; i < b; i++)
#define S(x) scanf("%d", &x)
#define S2(x, y) scanf("%d%d", &x, &y)
#define P(x) printf("%d\n", x)
#define all(v) v.begin(), v.end()
#define mp make_pair
#define mt make_tuple
#define fi first
#define se second
#define pb push_back
#define forn(i, n) for (int i = 0; i < (int)(n); ++i)
#define for1(i, n) for (int i = 1; i <= (int)(n); ++i)
#define ford(i, n) for (int i = (int)(n) - 1; i >= 0; --i)
#define fore(i, a, b) for (int i = (int)(a); i <= (int)(b); ++i)

int computeProblemIndex(string s){

	for(int i = 1; i < s.size(); i++)
		if(s.at(i) < s.at(i - 1))
			return i;

	return -1;
}

string deleteLeadingZeroes(string s){

	string ans = "";
	int i = 0;

	while(i < s.size() && s.at(i) == '0')
		i++;

	return s.substr(i);
}

string fillWithRightNines(string s, int leftMostProblemAt){

	//cout<<"leftMostProblemAt = "<<leftMostProblemAt<<endl;

	for(int i = leftMostProblemAt; i < s.size(); i++)
		s.at(i) = '9';

	return s;
}

string getAns(string s){

	int problemAt;
	int leftMostProblemAt = 100;

	while(true){

		problemAt = computeProblemIndex(s);
		//cout<<"problemAt = "<<problemAt<<endl;

		if(problemAt < 0){

			return deleteLeadingZeroes(fillWithRightNines(s, leftMostProblemAt));
		}

		s.at(problemAt) = '9';
		s.at(problemAt - 1)--;
			
		leftMostProblemAt = min(leftMostProblemAt, problemAt);

		//cout<<"s = "<<s<<endl;
	}

	return "ERROR_VALUE";
}

int main(){

	int cases;
	scanf("%d", &cases);
	string strNumber;

	for(int i = 1; i <= cases; i++){

		cin>>strNumber;
		cout<<"Case #"<<i<<": "<<getAns(strNumber)<<endl;
		//cout<<endl;
	}

	return 0;
}