#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <cmath>
#include <stack>
#include <queue>
#include <exception>
#include <numeric>
#include <algorithm> 
#include <sstream>
#include <cstring>
#include <deque>
using namespace std;
 
typedef long long lo;
typedef vector< vector<long long> > vvl;
typedef vector< long long> vl;
typedef pair<lo, lo> ll;
typedef vector< pair<lo, lo> > vll;
typedef vector< vll > vvll;
typedef pair<long, pair<long, long> > lll;
typedef vector<lll> vlll;
typedef vector<vvl> vvvl;
typedef vector<set<lo> > vs;
typedef map<lo, map<lo, lo> > mm;

#define N 1000

// fiven the available number one has to provide the greatest sorted. The naive way of dealing with this task would be iterating via the digits and trying to reduce the next digit, if it is greater than the current one. Once such occurence is found, reduce the left digit and replace all digits to the right with 9; Once reducing some number it makes no sense to keep other numbers intact. 
// Probable scheme of solution: find the furtherst digit left, that is bigger than its immediate successor. Reduce it, fill all the numbers to the left with 9. 
// 2 subproblems: decrease the digit and fill the rest with 9. Can be done by filing the rest with 0 and decrementing 1.

lo getDigit(lo n, lo i){
	for (;i;n/=10, i--);
	return n%10;
}

lo improve(lo n) {
	lo temp, l;
	l=0, temp=n;
	for (;temp;l++, temp/=10);
	for (lo i=l;i;i--){
		lo crr=getDigit(n, i), nxt=getDigit(n, i-1);
		if (crr>nxt){
			for (lo j=0;j<i;j++)
				n/=10;
			for (lo j=0;j<i;j++)
				n*=10;
			n--;
			break;
		}
	}
	return n;	
}

void solve(lo caseNum)  {
	lo n, temp, l;
	cin >> n;
	lo improved=improve(n);
	while (improved!=n) {
		n=improved;
		improved=improve(n);
	}
	cout << "Case #" << caseNum << ": " << n <<"\n";
}

int main() {
	freopen("B-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	lo t;
	cin >> t;
	for (lo i=0;i<t;i++)
		solve(i+1);
	return 0;
}