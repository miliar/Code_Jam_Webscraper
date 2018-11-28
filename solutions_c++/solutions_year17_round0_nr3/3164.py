#include <bits/stdc++.h>
using namespace std;

long long disp[1000002][4];
int ini, fin;

void solve(int t, long long n){
	long long pos;
	if (n % 2) pos = (n / 2LL) + 1LL;
	else pos = (n / 2LL);
	long long a = pos - 1LL;
	long long b = n - pos;
	cout << "Case #" << t << ": ";
	cout << max (a, b) << " " << min (a, b) << "\n";
}

void inserta(int pos, long long x, long long tam){
	while (pos <= fin && disp[pos][1] != x)
		pos++;
	if (pos > fin){
		fin++;
		disp[fin][1] = x;
		disp[fin][2] = tam;
	}else{
		disp[pos][2] += tam;
	}
}

int main (){

	freopen ("C-large.in", "r", stdin);
	freopen ("solLarge.out", "w", stdout);
	int casos;
	cin >> casos;
	for (int t = 1; t <= casos; t++){
		long long n, k;
		cin >> n >> k;
		ini = 1, fin = 1;
		disp[ini][1] = n;
		disp[ini][2] = 1LL;
		while (k > disp[ini][2]){
			k -= (disp[ini][2]);
			long long a, b;
			b = (disp[ini][1] - 1LL) / 2LL;
			a = disp[ini][1] - 1LL - b;
			if (a == b){
				long long sizeA = (2LL * disp[ini][2]);
				inserta(ini + 1, a, sizeA);
			}else{
				long long sizeA = disp[ini][2], sizeB = disp[ini][2];
				int pos = ini + 1;
				inserta(ini + 1, a, sizeA);
				inserta(ini + 1, b, sizeB);
			}
			ini++;
		}
		solve(t, disp[ini][1]);
	}
	return 0;
}