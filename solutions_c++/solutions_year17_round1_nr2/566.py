#include <bits/stdc++.h>

using namespace std;

typedef pair<int, int> ii;
typedef long long ll;

void solvre(){
	int n, p;
	int i;
	ll receita[55];
	vector<ll> mapa[55];
	int point[55];
	cin>>n>>p;
	// cout<<"N = "<<n<<"\tp = "<<p<<endl;
	for(int i = 0; i<n; i++){
		cin>>receita[i];
	}

		// cout<<endl;
	for(int i = 0; i<n; i++){
		mapa[i].resize(p);
		for(int j = 0; j<p; j++){
			cin>>mapa[i][j];
		}
		sort(mapa[i].begin(), mapa[i].end());
		// for(int j = 0; j<p; j++){
		// 	cout<<mapa[i][j]<<" ";
		// }
		// cout<<endl;
		point[i] = 0;
	}


	int ans = 0;
	i = 0;
	ll r = ((long long) ceil(1.0*mapa[0][0]/(1.1*receita[0])));
	while(true){
		if(i<n && point[i]==p) break;
		if(i==n){
			ans++;
			// cout<<r<<" ";
			for(int j = 0; j<n; j++){
				point[j]++;
			}
			i = 0;
		}else if(mapa[i][point[i]]*(10ll)>(11ll)*receita[i]*r){
			r = ((ll) ceil(1.0*mapa[i][point[i]]/(1.1*receita[i])));
			i = 0;
		}else if(mapa[i][point[i]]*(10ll)<(9ll)*receita[i]*r){
			point[i]++;
		}else{
			i++;
		}
	}
	cout<<ans<<endl;
}

int main(){
	int t;
	cin>>t;
	for(int i = 1; i<=t; i++){
		printf("Case #%d: ", i);
		solvre();
	}
}