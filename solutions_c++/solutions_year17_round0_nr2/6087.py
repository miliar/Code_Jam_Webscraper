#include <iostream>
#include <stdio.h>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <vector>
#include <queue>
#include <algorithm>
#include <math.h>
#include <set>
#include <map>
#include <limits>
#include <stdarg.h>
using namespace std;

typedef long long LL;
typedef pair<int,int> ii;
typedef vector<ii> vii;
typedef vector<int> vi;
typedef set<int> si;
typedef set<ii> sii;
typedef map<int,int> mii;

double EPS = 1e-9;
double PI = acos(-1);
const bool VUPRINT = true;

const int _r[8] = { 0, 0,-1, 1, 1, 1, -1, -1};
const int _c[8] = { 1,-1, 0, 0, 1, -1, 1, -1};

int INF = numeric_limits<int>::max();
LL LL_INF = numeric_limits<LL>::max();

void pr(const char *fmt, ...) {
    if (VUPRINT) {
    	va_list args;
	    va_start(args, fmt);
	    vprintf(fmt, args);
	    va_end(args);	
    }
}






// int grid[3][3];
// void printGrid(){
// 	if (!pr) return;

// 	int maxR = 3;
// 	int maxC = 3;

// 	for (int i=0;i<maxR;i++) {
// 		for (int j=0;j<maxC;j++){
// 			pr("%5d", gr[i][j]);
// 		}
// 		pr("\n");
// 	}
// 	pr("\n");
// }

LL T,N,cases;
LL tenPower[19];

LL countDigit(LL n){
	LL result = 0;
	while (n!=0){
		result++;
		n /= 10;
	}
	return result;
}

void getDigits(LL *d, LL n){
	LL cdigit = countDigit(n);
	LL pos = cdigit-1;

	while (n!=0){
		d[pos] = n % 10;
		pos --;
		n /= 10;
	}
}

LL bestTidyBefore(LL n){
	// printf("YOOOOOO\n");
	// printf("Calculating for n = %lld\n", n);

	LL noDigits = countDigit(n);
	LL digits[22];

	getDigits(digits,n);
	// printf("No of digits is: %lld\n", noDigits);

	// printf("digits are: ");
	// for (int i=0;i<noDigits;i++){
	// 	printf(" %d:%lld , ", i, digits[i]);
	// }

	if (noDigits==1) return n;


	// firstDigit = n / tenPower[noDigits-1];
	// secondDigit = n / tenPower[noDigits-2] % 10;
	if (digits[0] < digits[1]) return bestTidyBefore(n % tenPower[noDigits-1]) + digits[0]*tenPower[noDigits-1];

	if (digits[0] > digits[1]) return digits[0] * tenPower[noDigits-1] - 1;

	//now, firstDigit == secondDigit, we have to find the next digit that is not equal to firstDigit
	int ind = 1;

	while (true){
		if (ind == noDigits) {
			//all the digits are the same;
			return n;
		}
		if (digits[ind] > digits[0]){
			return bestTidyBefore(n % tenPower[noDigits-1]) + digits[0]*tenPower[noDigits-1];
		}
		if (digits[ind] < digits[0]){
			return digits[0] * tenPower[noDigits-1] - 1;
		}
		ind++;
	}
	return 0;
}

int main() {
	freopen("in.in","r",stdin);
	freopen("out.out","w",stdout);

	// int T,cases,K,result;
	// int W[120], array[1000];

	// char row[1100];
	// bool up[1100];
	// memset(array, 0, sizeof array);
	// memset(grid, 0, sizeof grid);
	// printf("Start\n");
	LL temp = 1;
	for (int i=0;i<19;i++){
		tenPower[i]=temp;
		temp*= 10;
	}
	// printf("Done precompute\n");

	scanf(" %lld", &T);
	for (cases=1;cases<=T;cases++){
		// scanf("%s", row);
		scanf(" %lld", &N);
		// printf("cases = %lld, N = %lld\n", cases, N);

		// memset(up, 0, sizeof up);

		LL result = bestTidyBefore(N);

		printf("Case #%lld: %lld\n",cases,result);

	}

}
