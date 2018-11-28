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
	cin >> T;
	int i, j, k;
	for (i = 0; i < T; i++){
		string N;
		cin >> N;
		int L = N.length();
		char num = 9;
		for (j = 0; j < L - 1; j++){
			if (N[j] > N[j + 1]){
				num = N[j];
				break;
			}
		}
		int pos = L;
		for (j = 0; j < L; j++){
			if (N[j] == num){
				pos = j;
				break;
			}
		}
		cout << "Case #" << i + 1 << ": ";

		for (j = 0; j < pos; j++){
			if (num != '1'){
				cout << N[j];
			}
		}
		if (pos == L){
			cout << endl;
			continue;
		}
		if (num != '1'){
			cout << char(int(num) - 1);
		}
		for (j = pos + 1; j < L; j++){
			cout << '9';
		}
		cout << endl;
	}
}
