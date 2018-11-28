#include <bits/stdc++.h>
#define endl '\n'
#define lli long long int
#define forn(i, n) for(int i=0;i<n;i++)

using namespace std;

int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	int t, u = 1,k;
	string cad;
	cin>>t;
	while(t--) {
		cin>>cad>>k;
		int cont = 0;
		for(int i=cad.size()-k;i>=0;i--) {
			if(cad[i + k - 1] == '+') continue;
			cont++;
			for(int j=0;j<k;j++)
				cad[i + j] = (cad[i + j] == '-' ? '+' : '-');
		}
		int f = 1;
		forn(i, cad.size())
			if(cad[i] == '-')
				f = 0;
		cout<<"Case #"<<u++<<": ";
		if(f) cout<<cont<<endl;
		else cout<<"IMPOSSIBLE"<<endl;
	}
	return 0;
}
