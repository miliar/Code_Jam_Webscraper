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

int d, n;


void parse() {	
	int ki, si;
	cin >> d >> n;
	double max_temps = 0;
	for (int i = 0; i < n; i++){
		cin >> ki >> si;
		double t = (d-ki)*1.0/si;
		ckmax(max_temps, t);
	}
	printf("%.6f\n", d/max_temps);
}

int main() {
	int T;
	cin >> T;
	for (int kase = 1; kase <= T; kase++) {
		printf("Case #%d: ", kase);
		parse();
		
	}
	return 0;
}