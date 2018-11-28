#include <bits/stdc++.h>
using namespace std;
#define INF 0x3f3f3f3f
#define For(i,a,b) for(int (i)=(a);(i) < (b); ++(i))
#define mp make_pair
#define pb push_back
#define fi first
#define se second
#define endl "\n"
#define PI acos(-1)
typedef long long ll;
typedef vector<int> vi;
typedef vector<bool> vb;
typedef pair<int,int> ii;
typedef complex<double> base;

const int N = 20;
int t;
string num;
int menor[N], res[N];

void fix(int i){
	bool fixed = 0;
	for(int j = i; j > 0; j--){
		if(res[j]-1 >= res[j-1]){
			res[j]--;
			for(int k = j+1; k < num.size(); k++){
				res[k] = 9;
			}
			fixed = 1;
			break;
		}
	}

	if(!fixed){
		res[0]--;
		for(int j = 1; j < num.size(); j++){
			res[j] = 9;
		}
	}
}

int main(void){
	ios_base::sync_with_stdio(false);
	cin >> t;

	for(int caso = 1; caso <= t; caso++){
		memset(res, 0, sizeof res);
		cin >> num;

		int len = num.size();
		For(i,0,len) res[i] = num[i] - '0';

		bool flag = 0;
		For(i,0,len-1){
			if(res[i] > res[i+1]){
				fix(i);
				break;
			}
		}

		int beg = 0;
		if(res[0] == 0) beg = 1;

		cout << "Case #" << caso << ": ";
		for(int i = beg; i < num.size(); i++){
			cout << res[i];
		}
		cout << endl;
	}
	

	return 0;
}
