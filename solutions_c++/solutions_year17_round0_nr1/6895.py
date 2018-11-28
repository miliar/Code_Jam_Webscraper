#include<iostream>
#include<cstdio>
#include<vector>
#include<map>
#include<set>
#include<string>
#include<algorithm>
#include<math.h>
#include<numeric>
#include<iomanip>

using namespace std;

typedef vector<int> vi;
typedef pair<int, int> pii;
typedef long long ll;
typedef vector<long long> vll;
typedef pair<long long, long long> pll;

const ll INF = 1e9;
const ll MOD = 1e9 + 7;


int main(){
	int T;
	vector<string> S;
	vi K;
	cin >> T;
	int i, j, m;
	for (i = 0; i < T; i++){
		string s;
		cin >> s;
		S.push_back(s);
		int k;
		cin >> k;
		K.push_back(k);
	}
	for (i = 0; i < T; i++){
		int k = K[i];
		string s = S[i];
		int n = s.size();
		int count = 0;
		for (j = 0; j < n - k + 1; j++){
			if (s[j] == '-'){
				count++;
				for (m = 0; m < k; m++){
					if (s[j + m] == '-'){
						s[j + m] = '+';
					}
					else{
						s[j + m] = '-';
					}
				}
			}
		}

		bool flg = 0;
		for (j = n - k + 1; j < n; j++){
			if (s[j] == '-'){
				cout << "Case #" << i + 1 << ": IMPOSSIBLE" << endl;
				flg = 1;
				break;
			}
		}
		if (flg == 0){
			cout << "Case #" << i + 1 << ": " << count << endl;
		}
	}
	return 0;
}
