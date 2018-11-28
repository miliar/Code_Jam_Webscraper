#include <bits/stdc++.h>
using namespace std;
#define REP(i, n) for (int i = 0; i < int(n); i++)
#define FOREACH(i, v) for (__typeof((v).begin()) i = (v).begin(); i != (v).end(); i++)
#define SIZE(v) ((int)(v).size())
#define pb push_back
#define mp make_pair
#define st first
#define nd second
#define ll long long
#define pii pair<int, int>

bool ok(int N){
	//printf("N = %d\n", N);
	int d = N%10;
	N /= 10;
	while(N != 0){
		int d0 = N%10;
		//printf("d0 = %d, d = %d\n", d0, d);
		if(d0 > d) return false;
		else d = d0;
		N /= 10;
	}
	//getchar();
	return true;
}

int dp[1010];

void init(){
	for(int i = 1; i <= 1000; i++)
		for(int j = i; j >= 1; j--){
			if(ok(j)){
				dp[i] = j;
				break;
			}
		}
}


int main(){
	
	init();

	int T;
	cin >> T;
	REP(t, T){
		int NN;
		string N;
		cin >> N;
		//cin >> NN;
		int len = SIZE(N);
		int id = 1;
		cout << "Case #" << t + 1 << ": ";
		while(id < len && N[id - 1]  <= N[id]) id++;
		if(id == len) cout << N << endl;
		else{
			int j = id;
			id--;
			while(j - 1 >= 0 && N[j - 1] == N[id]) j--;
			N[j]--;
			for(int i = j + 1; i < len; i++) N[i] = '9';
			if(N[0] == '0') N = N.substr(1, len - 1);
			cout << N << endl;
		}
		//cout << "Here = " << dp[NN] << endl;
	}
}
