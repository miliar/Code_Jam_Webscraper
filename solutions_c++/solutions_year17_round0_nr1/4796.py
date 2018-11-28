#include <bits/stdc++.h>
 
using namespace std;
 
typedef long long ll;
typedef pair<int, int> pii;
typedef pair<ll, int> plli;
typedef pair<double,double> pdd;
typedef pair<string,int> psi;
const int MOD = 1e9 + 7;

int n,k;
string s;

int main() {
    freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	cin >> n;
	for(int it = 1 ; it <= n ; it++){
		cin >> s >> k;
		int cnt = 0;
		for (int i = 0; i + k - 1< s.size(); ++i){
			if(s[i] == '+')
				continue;
			for(int j = i ; j <= i + k - 1;j++){
				if(s[j] == '-')
					s[j] = '+';
				else
					s[j] = '-';
			}
			cnt++;
		}
		bool can = true;
		for (int i = 0; i < s.size(); ++i){
			if(s[i] == '-')
				can = false;
		}
		if(can){
			printf("Case #%d: %d\n", it,cnt);
		}else{
			printf("Case #%d: IMPOSSIBLE\n", it);
		}
	}   	
    return 0;
}