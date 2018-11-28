#include<bits/stdc++.h>
using namespace std;


void solvetwo(vector<long long> G){
	long long zero = 0;
	long long one = 0;
	for(long long i = 0; i < G.size(); i++){
		if(G[i]%2 == 0){
			zero++;
		}else{
			one++;
		}
	}
	//cout << "zero " << zero << " one " << one << endl;
	if(one%2 == 1){
		cout << zero + one/2 + 1 << endl;
	}else{
		cout << zero + one/2 << endl;
	}
}

void solvethree(vector<long long> G){
	long long zero = 0;
	long long one = 0;
	long long two = 0;
	for(long long i = 0; i < G.size(); i++){
		if(G[i]%3 == 0){
			zero++;
		}else if(G[i]%3 == 1){
			one++;
		}else{
			two++;
		}
	}
	long long ans = 0;
	ans += zero;

	if(one > two){
		ans += two;
		one -= two;
		two = 0;
		if(one % 3 == 0){
			ans += one/3;
		}else{
			ans += one/3 + 1;
		}
	}else{
		ans += one;
		two -= one;
		one = 0;
		if(two % 3 == 0){
			ans += two/3;
		}else{
			ans += two/3 + 1;
		}
	}
	cout << ans << endl;
}


long long dp[105][105][105];


void solvefour(vector<long long> G){
	long long zero = 0;
	long long one = 0;
	long long two = 0;
	long long three = 0;
	for(long long i = 0; i < G.size(); i++){
		if(G[i]%4 == 0){
			zero++;
		}else if(G[i]%4 == 1){
			one++;
		}else if(G[i]%4 == 2){
			two++;
		}else{
			three++;
		}
	}

	for(int i = 0; i <= one; i++){
		for(int j = 0; j <= two; j++){
			for(int k = 0; k <= three; k++){
				dp[i][j][k] = 0;
			}
		}
	}

	for(int i = 0; i <= one; i++){
		for(int j = 0; j <= two; j++){
			for(int k = 0; k <= three; k++){
				if((i + 2*j + 3*k)%4 == 0){
					dp[i+1][j][k] = max(dp[i+1][j][k], dp[i][j][k] +1);
					dp[i][j+1][k] = max(dp[i][j+1][k], dp[i][j][k] +1);
					dp[i][j][k+1] = max(dp[i][j][k+1], dp[i][j][k] +1);
				}else{
					dp[i+1][j][k] = max(dp[i+1][j][k], dp[i][j][k]);
					dp[i][j+1][k] = max(dp[i][j+1][k], dp[i][j][k]);
					dp[i][j][k+1] = max(dp[i][j][k+1], dp[i][j][k]);
				}
			}
		}
	}


	cout << zero +  dp[one][two][three] << endl;
}

void solve(){
	long long N, P;
	vector<long long> G;
	cin >> N >> P;
	for(long long i = 0; i < N; i++){
		long long tmp;
		cin >> tmp;
		G.push_back(tmp);
	}
	if(P == 2){
		solvetwo(G);
	}else if(P == 3){
		solvethree(G);
	}else if(P == 4){
		solvefour(G);
	}
}

int main(){
	long long T;
	cin >> T;
	for(int i = 0; i < T; i++){
		cout << "Case #" << i + 1 << ":" << " ";
		solve();
	}
}

