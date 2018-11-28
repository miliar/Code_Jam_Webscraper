#include<bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<int, int> PII;

const int MM = 1e9 + 7;
const double eps = 1e-8;
const int MAXN = 2e6 + 10;

int n, m;

void prework(){

}

void read(){

}

int d[MAXN], s[MAXN];

void solve(int casi){
	cout << "Case #" << casi << ": ";
	ll D, n;
	cin>>D>>n;
	double t = -1;
	for(int i = 1; i <= n; i++){
		cin>>d[i]>>s[i];
		t = max(t, (D - d[i]) * 1.0 / s[i]);
	}
	printf("%.16f\n", D / t);
}

void printans(){

}


int main(){
//	std::ios::sync_with_stdio(false);
	prework();
	int T = 1;
	cin>>T;
	for(int i = 1; i <= T; i++){
		read();
		solve(i);
		printans();
	}
	return 0;
}

