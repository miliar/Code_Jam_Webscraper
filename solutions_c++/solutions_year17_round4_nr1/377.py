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

int p;
int a[MAXN];

void gao2(){
	int cnt = 0;
	for(int i = 1; i <= n; i++)
		cnt += (a[i] == 0);
	cnt += (n - cnt + 1) / 2;
	cout << cnt << endl;
}

void gao3(){
	int cnt = 0;
	int u = 0, v = 0;
	for(int i = 1; i <= n; i++){
		cnt += (a[i] == 0);
		u += (a[i] == 1);
		v += (a[i] == 2);
	}
	int w = min(u, v);
	cnt += w;
	u -= w, v -= w;
	cnt += v / 3;
	cnt += u / 3;
	v %= 3, u %= 3;
	cout << cnt + (u != 0) + (v != 0) << endl;
}

int f[100];

void gao4(){
	for(int i = 0; i <= 4; i++)
		f[i] = 0;
	for(int i = 1; i <= n; i++)
		f[a[i]]++;
	int cnt = f[0];
	cnt += f[2] / 2;
	f[2] %= 2;
	int u = min(f[1], f[3]);
	cnt += u;
	f[1] -= u;
	f[3] -= u;
	cnt += f[1] / 4;
	f[1] %= 4;
	cnt += f[3] / 4;
	f[3] %= 4;
	if (f[2]){
		if (f[1] >= 2){
			cnt++;
			f[2]--;
			f[1] -= 2;
		}
		if (f[3] >= 2){
			cnt++;
			f[2]--;
			f[3] -= 2;
		}
	}
	if (f[2] || f[3] || f[1])
		cnt++;
	cout << cnt << endl;
}

void solve(int casi){
	cout << "Case #" << casi << ": ";
	cin >> n >> p;
	for(int i = 1; i <= n; i++){
		cin >> a[i];
		a[i] %= p;
	}
	if (p == 2) gao2();
	else if (p == 3) gao3();
	else gao4();
}

void printans(){

}

int main(){
	std::ios::sync_with_stdio(false);
	prework();
	int T = 1;
	cin >> T;
	for(int i = 1; i <= T; i++){
		read();
		solve(i);
		printans();
	}
	return 0;
}

