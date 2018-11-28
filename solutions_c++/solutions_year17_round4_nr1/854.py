#include<bits/stdc++.h>
#include<unordered_set>
#include<unordered_map>
using namespace std;

int tttt;
void outt(){
	tttt++;
	cout << "Case #" << tttt << ": ";
}

int t;

map<int, int> mp;


int dp3[102][102];  //mod 1 mod 2
int dp4[102][102][102];
int main(){
	for (int i = 0; i <= 100; i++){
		for (int j = 0; j <= 100; j++){
			int sum = i + 2 * j;
			sum %= 3;
			dp3[i + 1][j] = max(dp3[i + 1][j], dp3[i][j] + (sum == 0));
			dp3[i][j + 1] = max(dp3[i][j + 1], dp3[i][j] + (sum == 0));
		}
	}
	for (int i = 0; i <= 100; i++){
		for (int j = 0; j <= 100; j++){
			for (int k = 0; k <= 100; k++){
				int sum = i + 2 * j + 3 * k;
				sum %= 4;
				dp4[i + 1][j][k] = max(dp4[i + 1][j][k], dp4[i][j][k] + (sum == 0));
				dp4[i][j + 1][k] = max(dp4[i][j + 1][k], dp4[i][j][k] + (sum == 0));
				dp4[i][j][k + 1] = max(dp4[i][j][k + 1], dp4[i][j][k] + (sum == 0));
			}
		}
	}
	cin >> t;
	while (t--){
		int n;
		cin >> n;
		int p;
		cin >> p;
		int ans = 0;
		mp.clear();
		for (int i = 0; i < n; i++){
			int a;
			scanf("%d", &a);
			a %= p;
			mp[a]++;
		}
		outt();
		if (p == 2){
			int ans = mp[0];
			ans += (mp[1] + 1) / 2;
			cout << ans << endl;
			continue;
		}
		if (p == 3){
			cout << dp3[mp[1]][mp[2]] + mp[0] << endl;
			continue;
		}
		cout << dp4[mp[1]][mp[2]][mp[3]] + mp[0] << endl;
	}
	return 0;
}