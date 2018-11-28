#include <bits/stdc++.h>
using namespace std;
#define rep(i,n) for(int i=0;i<n;i++)
#define repu(i,a,b) for(int i=a;i<=b;i++)
#define repd(i,b,a) for(int i=b;i>=a;i--)
typedef long long LL;
typedef pair<int,int> ii;
typedef vector<int> vi;

string str;

string sub(const string& a, long long k){
	long long num = stoll(a);
	return to_string(num - k);
}
int valid(string& s) {
	rep(i, s.size()) {
		if(i > 0 && s[i]<s[i-1]){
			return i;
		}
	}
	return -1;
}

string solve(string s){
	int k;
	if((k = valid(s)) != -1) {
		string right(s.size() - k, '9');
		string left = solve(sub(s.substr(0, k), 1));
		int tt = 0;
		while(left[tt] == '0') tt++;
		return left.substr(tt) + right;
	}
	else{
		return s;
	}
}
int main()
{
	ios_base::sync_with_stdio(false);
	
	int kase = 0, Tc;
	cin >> Tc;
	while(kase < Tc){
		cin >> str;
		cout<<"Case #"<<++kase<<": ";
	    cout << solve(str) << endl;
	}
	return 0;
}