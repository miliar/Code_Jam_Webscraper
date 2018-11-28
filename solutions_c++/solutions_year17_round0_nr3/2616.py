#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <fstream>
#include <bitset>
#include <cstdio>
#include <sstream>
#include <string>
#include <queue>
#include <map>
#include <stack>
#include <set>
#include <cctype>
#include <iomanip>
#include <list>
#include <cstring>

#define INF 2000000000
#define ull unsigned long long int
#define vi vector<int>
#define vii vector<ii>

#define UNVISITED 0
#define OPENED 1
#define CLOSED 2

#define PI 3.14159265359

#define dbg(x) cout<<#x<<" : "<<x<<endl


using namespace std;



long long int n, k;

long long int fct(long long int nLeft,long long int nRight,long long int left,long long int right,long long int k) {
	left--; right--;	
	
	long long int nextLeft = max((long long int) 0, min(min(left/2, left-left/2), min(right/2, right-right/2)));
	long long int nextRight = max(max(left/2, left-left/2), max(right/2, right-right/2));
	
	long long int nbLeft = 0, nbRight = 0;
	if(max((long long int )0, left/2) == nextLeft) 
		nbLeft += nLeft;	
	else
		nbRight += nLeft;

	if(max((long long int) 0, left - left/2) == nextLeft) 
		nbLeft += nLeft;	
	else
		nbRight += nLeft;

	if(right/2 == nextLeft) 
		nbLeft += nRight;	
	else
		nbRight += nRight;
		
	if(right - right/2 == nextLeft) 
		nbLeft += nRight;	
	else
		nbRight += nRight;

	//cout << nextLeft << " " << nextRight << " " << nbLeft << " " << nbRight << endl;

	if(k <= (nLeft+nRight)) {
		//cout << k << " " << nRight << endl;
		if(k <= nRight) return right+1;
		else return left+1; 
	}	
	else {
		return fct(nbLeft, nbRight, nextLeft, nextRight, k -(nLeft+nRight));
	}	
}

int main () {
	int nTest;
	scanf("%d", &nTest);
	
	for(int iTest = 0; iTest < nTest; iTest++) {
		scanf("%lld %lld", &n, &k);
		
		
		long long int ans = fct(1, 0, n,n, k);
		//cout << ans << endl;
		printf("Case #%d: %lld %lld\n", iTest+1, max((long long int) 0, (ans-1)-(ans-1)/2), max((long long int) 0, (ans-1)/2));
				
	}
	
		
    return 0;
}
