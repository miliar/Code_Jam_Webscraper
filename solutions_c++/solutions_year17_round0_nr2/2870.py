#include <bits/stdc++.h>
using namespace std;

const int N = 1e6+6;
const int M = 1e9+7;

typedef long long ll;
typedef long double ld;
typedef vector<int> vi;
typedef vector<pair<int,int> > vpii;
typedef pair<int,int> pii;

#define fr(i ,a, b)	for(int i = a; i <= b; i ++)
#define rep(i, n)	for(int i = 0; i < n; i++)
#define rv(i, a, b)	for(int i = a; i >=b;i --)

bool check(string s){
	int len = s.length();
	rep(i, len){
		fr(j, i+1, len - 1){
			if(s[i]>s[j])	return false;
		}
	}
	return true;
}

void reduce(string &s, int idx){
	int len = s.length();
	for(int i = idx+1; i < len; i++)	s[i] = '9';
	while(idx>0&&s[idx]=='0'){
		s[idx]='9';
		idx--;
	}
	s[idx] = s[idx] - 1;
}

ll to_int (string &s){
	ll res = 0;
	for(int i = 0; i < s.length();i ++){
		res*=10;
		res+=s[i] - '0';
	}
	return res;
}

void solve(string &s){
	for(int i = s.length() - 1; i >=0; i--)	{
		if(check(s))	break;
		else reduce(s, i);
	}
	cout<<to_int(s)<<'\n';
}

int main(){
	ios_base::sync_with_stdio(0);	cin.tie();
	freopen("input.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t;	cin>>t;
	for(int i =1; i <=t; i ++){
		cout<<"Case #"<<i<<": ";
		string s;	cin>>s;
		solve(s);
	}
}