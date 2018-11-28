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
	ll D,N;
	double S;
	cin >> D >> N;
	ll d[N],K[N];
	for(int i = 0;i<N;++i){
		cin >> d[i] >> K[i];
	}
	S = ((double)K[0]*d[0])/(D-d[0]) + K[0];
	for(int i = 1;i<N;++i){
		S = min(S, ((double)K[i]*d[i])/(D-d[i]) + K[i]);
	}
	cout << fixed  << setprecision(8) << S << '\n';

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
