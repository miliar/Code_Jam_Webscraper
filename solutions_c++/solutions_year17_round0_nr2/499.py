#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <set>
#include <utility>
#include <iomanip>
#include <map>
#include <string>
#define INF 1000000000
#define HAND_TYPE 1
#define TEST 10
#define SMALL 100
#define LARGE 1000
#define INPUT_SITUATION LARGE
#define MAKE_OUTFILE
using namespace std;
typedef long long s64;
typedef unsigned long long u64;
int T,ans;
string s;
int main() {
	if (INPUT_SITUATION == TEST) 
		freopen("test_input.txt","r",stdin);
	else if (INPUT_SITUATION == SMALL)
		freopen("B-small.in","r",stdin);
	else if (INPUT_SITUATION == LARGE)
		freopen("B-large.in","r",stdin);
	#ifdef MAKE_OUTFILE
	freopen("output.txt","w",stdout);
	#endif
	cin >> T;
	char A[20];
	for (int cas=0; cas<T; cas++) {
		cin >> s;
		A[s.length()] = 0;
		int k = 0;
		while (k < s.length()-1 && s[k] <= s[k+1]) k++;
		if (k == s.length()-1)
			A[k] = s[k];
		else
			A[k] = s[k]-1;
		for (int i=k-1; i>-1; --i) {
			if (s[i] < A[i+1])	A[i] = s[i];
			else A[i] = A[i+1];
		}		
		if (A[k] == 0x30) 
			k = -1;
		else {
			k = 0; 
			while (A[k] == s[k]) k++;
		}
		for (int i=k+1; i<s.length(); ++i)
			A[i] = 0x39;
		if (k == -1) {
			A[s.length()-1] = 0;
		}
		cout << "Case #" << cas+1 << ": " << A << '\n';
	}
	return 0;
}
