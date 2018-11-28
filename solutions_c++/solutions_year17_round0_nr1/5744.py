// ProblemA_OversizedPancakeFlipper.cpp

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

#define FLIPPED 1
#define NOT_FLIPPED 0
#define HAPPY '+'
#define SAD '-'

bool areAllHappy(string s){

	for(int i = 0; i < s.size(); i++)
		if(s.at(i) != HAPPY)
			return false;

	return true;
}

string flipAt(string s, int startingIndex, int k){

	// cout<<"startingIndex = "<<startingIndex<<endl;
	// cout<<"startingIndex + k = "<<startingIndex + k<<endl;

	for(int i = startingIndex; i < startingIndex + k; i++)
		s[i] = (s[i] == HAPPY) ? s[i] = SAD : s[i] = HAPPY;

	return s;
}

bool allPositionsHaveBeenFlipped(int arr[], int size){

	for(int i = 0; i < size; i++)
		if(arr[i] == NOT_FLIPPED)
			return false;

	return true;
}

int requiredMovements(string s, int k){

	int counter = 0;
	int currIndex = 0;
	int arr[s.size()];
	fill_n(arr, s.size(), NOT_FLIPPED);

	while(!areAllHappy(s) && /*currIndex < s.size() - k + 1*/!allPositionsHaveBeenFlipped(arr, s.size()) && counter <= s.size() - k + 1){

		counter++;
		//currIndex %= s.size();

		while(currIndex < s.size() - k + 1 && s[currIndex] == HAPPY)
			currIndex++;

		if(arr[currIndex] == FLIPPED)
			continue;

		if(currIndex >= s.size() - k + 1)
			continue;

		s = flipAt(s, currIndex, k);
		arr[currIndex] = FLIPPED;
		// cout<<"currIndex = "<<currIndex<<endl;
		// cout<<"s = "<<s<<endl;
	}

	return (areAllHappy(s)) ? counter : 2*s.size() + 2;
}

int main(){

	int cases, k;
	scanf("%d", &cases);

	string s;

	for(int i = 1; i <= cases; i++){

		cin>>s;
		scanf("%d", &k);

		int reqMoves = requiredMovements(s, k);

		if(reqMoves <= s.size() - k + 1)
			printf("Case #%d: %d\n", i, reqMoves);

		else
			printf("Case #%d: IMPOSSIBLE\n", i);

		// printf("\n");
	}

	return 0;
}