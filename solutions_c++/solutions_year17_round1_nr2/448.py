#include <bits/stdc++.h>
using namespace std;

#define ll long long
const int N = 1e6 + 5;

ll R[55], cntr[55], Q[55][55];

void solve(){
	int n, p;
	cin>>n>>p;
	for(int i = 1; i <= n; i++){
		cin>>R[i];
		cntr[i] = 1;
	}
	for(int i = 1; i <= n; i++){
		for(int j = 1; j <= p; j++){
			cin>>Q[i][j];
		}
		sort(Q[i] + 1, Q[i] + p + 1);
	}

	int ans = 0;

	for(int i = 1; i < N; i++){
		int wow = 0;
		for(int j = 1; j <= n; j++){
			
			ll Lamt = i * 9LL *  R[j], Ramt = (i * 11LL * R[j]) / 10LL;
			
			if(Lamt % 10 != 0)	Lamt /= 10, Lamt++;
			else Lamt /= 10;

			while(cntr[j] <= p and Q[j][cntr[j]] < Lamt)	cntr[j]++;

			if(cntr[j] > p)	break;

			if(Q[j][cntr[j]] >= Lamt and Q[j][cntr[j]] <= Ramt){
				wow++;
			}
		}
		if(wow == n){
			for(int j = 1; j <= n; j++)	cntr[j]++;
			ans++;
			i--;
		}
	}
	cout<<ans<<endl;
}

int main(){
	int t;
	cin>>t;
	for(int big = 1; big <= t; big++){
		cout<<"Case #"<<big<<": ";
		solve();
	}
}