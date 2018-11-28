#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef vector<pair<int,int> > vpii;
typedef pair<int,int> pii;
typedef long double ld;

const int N = 1e6+6;
const int M = 1e9+7;

#define fr(i, a,b)	for(int i = a; i <= b; i++)
#define rv(i, a, b)	for(int i = b; i >= b; i--)
#define rep(i,n)	for(int i = 0; i < n; i++)

char flip(char c){
	if(c=='-')	return '+';
	else return '-';
}

void solve(){
	string s;	cin>>s;
	int k;	cin>>k;
	int len = s.length();
	int res = 0; 
	for(int i = 0; i < len - k + 1; i++){
		if(s[i]=='-'){
			for(int j = 0; j < k; j++)	s[i+j] = flip(s[i+j]);
			res++;
		}
	}
	for(int i = 0; i < len; i++)	if(s[i]=='-')	{
		cout<<"IMPOSSIBLE\n";
		return;
	}
	cout<<res<<'\n';
}

int main(){
	freopen("input.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	ios_base::sync_with_stdio(0);	cin.tie();
	int t;	cin>>t;
	fr(i, 1, t){
		cout<<"Case #"<<i<<": ";
		solve();
	}

}