/*  Coder: Harsh Gupta
	Email: harshgupta.11dec@gmail.com
	Github: harshgupta11
	Linkedin: harshgupta11
	Problem Link: 
*/

#include "bits/stdc++.h"

using namespace std;

#define mp make_pair
typedef long long int ll;
typedef vector<int> vi;
typedef vector<pair<int,int> > vii;


int main()
{
	ios::sync_with_stdio(0);
	cin.tie(0);
	int T, K, ans, check;
	cin >> T;
	for(int test = 1;test <= T;++test){
		string S;
		ans = 0;
		cin >> S >> K;
		for(int i = 0;i<=S.size()-K;++i){
			if(S[i] == '-'){
				++ans;
				for(int j = i;j<i+K;++j){
					if(S[j] == '-') S[j] = '+';
					else            S[j] = '-';
				}
			}
		}
		check = 1;
		for(int i = 0;i<S.size();++i){
			if(S[i] == '-'){
				check = 0;
				break;
			}
		}
		cout << "Case #" << test << ": ";
		if(check) cout << ans << '\n';
		else cout << "IMPOSSIBLE\n";
	}
    return 0;
}
