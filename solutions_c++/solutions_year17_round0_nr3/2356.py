#include <iostream>
#include <fstream>
#include <algorithm>
#include <utility>
using namespace std;
typedef long long ll;

ifstream fin ("C.in"); ofstream fout ("C.out");

ll f(ll N, ll n, ll m, ll k) {
	if (n >= k) return N;
	else if (n+m >= k) return N-1;
	else if (N%2==0) return f(N/2, n, n+2*m, k-n-m);
	else return f((N-1)/2, 2*n+m, m, k-n-m);
}

void onerun(int t) {
	ll N, k; fin >> N >> k;
	ll ans = f(N,1,0,k);
	fout << "Case #" << t << ": " << ans/2 << " " << (ans-1)/2 << endl;
}

int main() {
	int T; fin >> T;
	for (int t=1; t<=T; t++) onerun(t);
	fin.close(); fout.close();
}