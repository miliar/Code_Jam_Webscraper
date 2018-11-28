#include <bits/stdc++.h>

#define i64 long long
#define u64 unsigned long long
#define i32 int
#define u32 unsigned int

#define pii pair<int, int>
#define pll pair<long long, long long>

#define ld long double
#define defmod 1000000007

#define mati64(a,b) vector<vector<i64>>(a, vector<i64>(b, 0));
using namespace std;

void solve1(){
	int n, p; cin >> n >> p;
	int a[110];
	int m[4] = {0};
	for(int i = 0; i < n; ++i){
		cin >> a[i];
		m[a[i]%p]++;
	}
	int ans = 0;
	if(p == 2){
		int ans = m[0];
		if(m[1]){
			ans+=1+(m[1]-1)/2;
		}
		cout << ans << endl;
	}
	else if(p == 3){
		int a1 = m[0];
		if(m[1]){
			a1+=1+(m[1]-1)/3;
		}
		if(m[2]){
			if(m[1]%p == 0){
				if(m[2] > 0)
					a1+=1+(m[2]-1)/3;
			}
			if(m[1]%p == 1){
				if(m[2] > 1)
					a1+=1+(m[2]-2)/3;
			}
			if(m[1]%p == 2){
				if(m[2] > 2)
					a1+=1+(m[2]-3)/3;
			}
		}
		int a2 = m[0];
		if(m[2]){
			a2+=1+(m[2]-1)/3;
		}
		if(m[1]){
			if(m[2]%p == 0){
				if(m[1]){
					a2+=1+(m[1]-1)/3;
				}
			}
			if(m[2]%p == 1){
				a2+=m[1]/3;
			}
			if(m[2]%p == 2){
				if(m[1] > 1)
					a2+=1+(m[1]-2)/3;
			}
		}
		int a3 = m[0];
		a3+=min(m[1], m[2]);
		if(m[1] > m[2])
			a3+=1+(m[1]-m[2]-1)/3;
		else if(m[2] > m[1])
			a3+=1+(m[2]-m[1]-1)/3;
		cout << max(a1, max(a2, a3)) << endl;
	}
	else if(p == 4){

	}
}

void solve2(){
	int n, p; cin >> n >> p;
	int a[110];
	int m[4] = {0};
	for(int i = 0; i < n; ++i){
		cin >> a[i];
		m[a[i]%p]++;
	}
	int cc = 100000;
	int be = 0;
	while(cc--){
		random_shuffle(a, a+n);
		int mo = 0;
		int a1 = 0;
		for(int i = 0; i < n; ++i){
			if(mo == 0)
				a1++;
			mo = (mo+a[i])%p;
		}
		be = max(be, a1);
	}
	cout << be << endl;
}
int main(){
	srand(time(0));
	cin.sync_with_stdio(0);
	cin.tie(0);
	

	int tests; cin >> tests;
	for(int i = 1; i <= tests; ++i){
		cout << "Case #" << i << ": ";
		solve1();
	}
	return 0;
}
