#include <cstdio> 
#include <cstdlib> 
#include <ctime> 
#include <cstring> 
#include <iostream> 
#include <cmath> 
#include <string> 
#include <vector> 
#include <algorithm> 
#include <set> 
#include <map> 
#include <queue> 
#include <stack> 

using namespace std; 

typedef unsigned int uint; 
typedef long long int64; 
typedef unsigned long long uint64; 
typedef unsigned short ushort; 
typedef unsigned char uchar; 
typedef pair<int,int> ipair; 
typedef vector<int> VI; 
typedef vector<string> VS; 
typedef vector<double> VD; 
#define SIZE(A) ((int)(A.size()))
#define LENGTH(A) ((int)(A.length()))
#define MP(A,B) make_pair(A,B)
const double pi = acos(-1.0); 
#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define REP(i,a) for(int i=0;i<(a);++i)
#define ALL(a) (a).begin(),(a).end()

template<class T> T sqr(const T &x) { return x*x; } 
template<class T> T lowbit(const T &x) { return (x^(x-1))&x; } 
template<class T> int countbit(const T &n) { return (n==0)?0:(1+countbit(n&(n-1))); } 
template<class T> void ckmin(T &a,const T &b) { if (b<a) a=b; } 
template<class T> void ckmax(T &a,const T &b) { if (b>a) a=b; } 


int a[105];
int n, P;

void parse() {	
	cin >> n >> P;
	for (int i = 0; i < n; i++) {
		cin >> a[i];
		a[i] = a[i] % P;
	}
	sort(a, a+n);
}

void solve() {
	int one, zero , two, three, sum;
	if (P == 2) {
		zero = 0;
		for (int i = 0; i < n; i++)
			if (a[i] == 0)
				zero++;
		one = n - zero;
		if (one % 2 == 1)
			one = (one + 1) / 2;
		else one = one / 2;
		cout << zero + one << endl;
	}

	if (P == 3) {
		zero = 0, one = 0;
		for (int i = 0; i < n; i++) {
			if (a[i] == 0)
				zero++;
			if (a[i] == 1)
				one++;
		}
		 two = n - one - zero;
		sum = zero;
		if (one > two){
			sum = sum + two;
			one = one - two;
			if (one % 3 == 0) sum += one / 3;
			else sum += (one / 3) + 1;
		}
		else {
			sum += one;
			two = two - one;
			if (two % 3 == 0) sum += two / 3;
			else sum += (two / 3) + 1;
		}
		cout << sum << endl;
	}

	if (P == 4) {
		zero = 0, one = 0, two =0, three = 0;
		for (int i = 0; i < n; i++) {
			if (a[i] == 0)
				zero++;
			if (a[i] == 1)
				one++;
			if (a[i] == 2)
				two++;
		}
		three = n - one - two - zero;
		sum = zero + two / 2;
		two = two % 2;
		if (one > three){
			sum += three; one -= three;
			if (two == 1){
				if (one >= 2) {
					sum += 1;
					one -= 2;
					if (one % 4 == 0) sum += one / 4;
					sum += (one / 4) + 1;
				}
				else sum += 1;
			}
			else {
				if (one % 4 == 0) sum += one / 4;
					sum += (one / 4) + 1;
			}
		}
		else {

			sum += one; three -= one;
			if (two == 1){
				if (three >= 2) {
					sum += 1;
					three -= 2;
					if (three % 4 == 0) sum += three / 4;
					sum += (three / 4) + 1;
				}
				else sum += 1;
			}
			else {
				if (three % 4 == 0) sum += three / 4;
					sum += (three / 4) + 1;
			}
		}

		cout << sum << endl;
	}
}

int main() {
	int T;
	cin >> T;
	for (int kase = 1; kase <= T; kase++) {
		printf("Case #%d: ", kase);
		parse();
		solve();
	}
	return 0;
}