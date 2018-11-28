// ProblemC_BathroomStalls.cpp

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

#define OCCUPIED 1
#define EMPTY 0

long long int getFreeStalls(long long int arr[], long long int size, long long int startingIndex, int direction){

	for(long long int i = startingIndex += direction; (direction < 0) ? i >= 0 : i < size; i += direction)
		if(arr[i] == OCCUPIED){

			//cout<<"abs("<<startingIndex<<" - "<<i<<") = "<<abs(startingIndex - i)<<endl;

			return abs(startingIndex - i);
		}
	
	return -1;
}

pair<long long int, pair<long long int, long long int> > getNextBestIndex(long long int arr[], long long int size){

	long long int bestIndex = -1;
	long long int bestIndex_Ls = -1;
	long long int bestIndex_Rs = -1;
	long long int local_Ls;
	long long int local_Rs;

	for(long long int i = 0; i < size; i++){

		if(arr[i] == OCCUPIED)
			continue;

		local_Ls = getFreeStalls(arr, size, i, -1);
		local_Rs = getFreeStalls(arr, size, i, 1);

	 // 	cout<<"i = "<<i<<endl;
		// cout<<"local_Ls = "<<local_Ls<<endl;
		// cout<<"local_Rs = "<<local_Rs<<endl;

		if(min(local_Ls, local_Rs) > min(bestIndex_Ls, bestIndex_Rs)){

			bestIndex = i;
			bestIndex_Ls = local_Ls;
			bestIndex_Rs = local_Rs;
		}

		else if(min(local_Ls, local_Rs) == min(bestIndex_Ls, bestIndex_Rs)){

			if(max(local_Ls, local_Rs) > max(bestIndex_Ls, bestIndex_Rs)){

				bestIndex = i;
				bestIndex_Ls = local_Ls;
				bestIndex_Rs = local_Rs;
			}
		}

	}

	// cout<<"bestIndex = "<<bestIndex<<endl;
	// cout<<"bestIndex_Ls = "<<bestIndex_Ls<<endl;
	// cout<<"bestIndex_Rs = "<<bestIndex_Rs<<endl;

	return make_pair(bestIndex, make_pair(bestIndex_Ls, bestIndex_Rs));
} 

void displayStalls(long long int arr[], int size){

	for(int i = 0; i < size; i++)
		printf("%lld ", arr[i]);
}

pair<long long int, long long int> getAns(long long int n, long long int k){

	long long int arr[n + 2];
	fill_n(arr, n + 2, EMPTY);
	arr[0] = OCCUPIED;
	arr[n + 1] = OCCUPIED;
	long long int nextIndex;
	pair<long long int, pair<long long int, long long int> > newMove;
	long long int lS, rS;

	for(long long int i = 0; i < k; i++){

		newMove = getNextBestIndex(arr, n + 2);
		nextIndex = newMove.first;
		//cout<<"nextIndex = "<<nextIndex<<endl;
		lS = newMove.second.first;
		rS = newMove.second.second;
		arr[nextIndex] = OCCUPIED;
	}

	//displayStalls(arr, n + 2);
	// printf("\n");

	return make_pair(max(lS, rS), min(lS, rS));
}

int main(){

	int cases;
	scanf("%d", &cases);
	long long int n, k;

	for(int i = 1; i <= cases; i++){

		cin>>n>>k;
		pair<long long int, long long int> ans = getAns(n, k);
		printf("Case #%d: %lld %lld\n", i, ans.first, ans.second);
		// printf("\n");
	}

	return 0;
}