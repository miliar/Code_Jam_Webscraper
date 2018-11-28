/*
	Be ashamed to die .. until you have Scored some Victory for Humanity
*/

#include <iostream>
#include <string>
#include <iomanip>
#include <cmath>
#include <math.h>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <cstdlib>
#include <iterator>
#include <queue>
#include <fstream>
#include <stack>
#include <sstream>

using namespace std;


typedef long long ll;
typedef vector<int> vi;
typedef vector<string> vs;
typedef vector<double> vd;
typedef map<string ,int> mpsi;



#define _OO (ll) -1e12
#define  OO (ll) 1e12
#define mem(arr,value) memset(arr,value,sizeof(arr))
#define pb push_back

// i,j+1 | i+1,j | i-1,j | i,j-1

int di[] = {1, -1, 0, 0};
int dj[] = {0, 0, 1, -1};

/*const int n = (int)1e6+1;
bool isPrime[n];
void Seive(){
	mem(isPrime, true);
	isPrime[0] = isPrime[1] = false;
	lpi(2,(int)1e6){
		if (isPrime[i]){
			for(int j=2*i;j<=(int)1e6;j+=i){
				isPrime[j] = false;
			}
		}
	}
}*/

string S;
int K;

bool good(){
	int c = 0;
	for(int i=0;i<S.size();i++)
		c += (S[i]=='+');
	return (c==S.size());
}

void flip(int a,int b){
	for(int i=a;i<b;i++){
		S[i] = (S[i]=='-')?'+':'-';
	}
}

int main(){
	ifstream in("A-large.in", ios::in);
	ofstream out("out.txt", ios::out);
	int T;
	in >> T;
	for(int t=1; t<=T; t++){
		in >> S >> K;
		int C = 0;
		for(int j=0; j<10000 && !good(); j++){
			for(int i=0;i<=S.size()-K;i++){
				if (S[i] == '-'){
					flip(i,i+K);
					++C;
				}
			}
		}
		out << "Case #" << t << ": ";
		if (good())
			out << C << endl;
		else
			out << "IMPOSSIBLE" << endl;
	}
return 0;
}