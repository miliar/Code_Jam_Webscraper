#include <bits/stdc++.h>
#define F first
#define S second
#define X real()
#define Y imag()
using namespace std;
typedef long long ll;
typedef long double ld;

void solve(){
	string s;
	cin>>s;
	int n=s.size();
	string fo(n, '0');
	for (int i=0;i<n;i++){
		for (char t='0';t<='9';t++){
			string nfo=fo;
			for (int j=i;j<n;j++){
				nfo[j]=t;
			}
			if (nfo<=s){
				fo=nfo;
			}
		}
	}
	if (fo[0]=='0'){
		assert(n>1);
		fo=string(n-1, '9');
	}
	cout<<fo<<endl;
}

int main(){
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	int tcs;
	cin>>tcs;
	for (int tc=1;tc<=tcs;tc++){
		cout<<"Case #"<<tc<<": ";
		solve();
	}
}