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

void solve(){
	string S;
	cin >> S;
	int i = 1;
	while(i < S.size() && S[i] >= S[i-1]) ++i;
	if(i == S.size()){
		cout << S << '\n';
		return;
	}
	S[i-1]--;
	for(int j = i-2;j>=0 && S[j] > S[j+1];--j){
		S[j]--;
		i = j+1;
	}
	while(i < S.size()){
		S[i] = '9';
		++i;
	}
	ll ans = 0;
	for(i = 0;i<S.size();++i){
		ans*=10;
		ans+=(S[i] - '0');
	}
	cout << ans << '\n';
}
int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	int T;
	cin >> T;
	for(int test = 1;test <=T;++test){
		cout << "Case #" << test << ": ";
		solve();
	}
    return 0;
}
