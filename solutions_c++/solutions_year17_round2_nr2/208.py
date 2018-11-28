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

int n, R, O, Y, G, B, V;
char a[1005];
int b[5];
void parse() {	
	cin >> n >> R >> O >> Y >> G >> B >> V;
}

int RG, OB, YV;
int findone(){
	int m = R + B + Y;
	if (R > m/2) return -1;
	if (B > m/2) return -1;
	if (Y > m/2) return -1;

	if (R != 0) { a[0] = 'R'; R--;}
	else if (B != 0) { a[0] = 'B'; B--;}
	else { a[0] = 'Y'; Y--;}

	for (int i = 1; i < m; i++){
		if (a[0] == 'R' && R > 0 && a[0] != a[i-1])	{
			a[i] = a[0]; R--;
			continue;
		}

		if (a[0] == 'B' && B > 0 && a[0] != a[i-1])	{
			a[i] = a[0]; B--;
			continue;
		}

		if (a[0] == 'Y' && Y > 0 && a[0] != a[i-1])	{
			a[i] = a[0]; Y--;
			continue;
		}


		if (a[i-1] == 'R') {
			if (B > Y && B > 0) {
				a[i] = 'B';
				B--;
			}
			else { a[i] = 'Y'; Y--;}
		}

		if (a[i-1] == 'B') {
			if (R > Y && R > 0){
				a[i] = 'R'; R--;
			}
			else {a[i] = 'Y'; Y--;}
		}

		if (a[i-1] == 'Y') {
			if (R > B && R > 0){
				a[i] = 'R'; R--;}
			else { a[i] = 'B'; B--;}
		}
	}

	//if (a[m-1] == a[0])
	//	cout << "ERROR" << endl;


	for (int i = 0; i < m; i++) {
		if (a[i] == 'R'){
			if (RG == 1){
				RG = 0;
				for (int j = 0; j < G; j++)
					cout << "RG";
				cout << "R";
			}
			else cout << a[i];
		}

		if (a[i] == 'B'){
			if (OB == 1) {
				OB = 0;
				for (int j = 0; j < O; j++)
					cout << "BO";
				cout << "B";
			}
			else cout << a[i];
		}

		if (a[i] == 'Y'){
			if (YV == 1) {
				YV = 0;
				for (int j = 0; j < V; j++)
					cout << "YV";
				cout << "Y";
			}
			else cout << a[i];
		}

	}
		
	cout << endl;
	return 0;
}


int solve() {
	 RG = 0;
	 OB = 0;
	 YV = 0;

	if (G != 0) {
		if (R < G) return -1;
		if (R == G && O+Y+B+V > 0) return -1;
		if (R == G && O+Y+B+V == 0) {
			for (int i =0 ; i < G; i++)
				cout << "RG";
			cout << endl;
			return 0;
		}

		R = R - (G+1);
		RG = 1;
		R++;
	}

	if (O != 0) {
		if (B < O) return -1;
		if (O == B && R+Y+G+V > 0) return -1;
		if (O == B && R+Y+G+V == 0) {
			for (int i =0 ; i < O; i++)
				cout << "BO";
			cout << endl;
			return 0;
		}

		B = B - (O+1);
		OB = 1;
		B++;
	}

	if (V != 0) {
		if (Y < V) return -1;
		if (Y == V && R+O+G+B > 0) return -1;
		if (Y == V && R+O+G+B == 0) {
			for (int i =0 ; i < V; i++)
				cout << "YV";
			cout << endl;
			return 0;
		}
		Y = Y - (V+1);
		YV = 1;
		Y++;
	}

	//cout << RG << " " << OB << " " << YV << endl;
	int t = findone();
	if (t==-1) return -1;
	return 0;
}

int main() {
	int T;
	cin >> T;
	for (int kase = 1; kase <= T; kase++) {
		parse();
		printf("Case #%d: ", kase);
		
		int t = solve();
		if (t == -1)
			printf("IMPOSSIBLE\n");
	}
	return 0;
}