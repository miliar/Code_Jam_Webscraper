#include <bits/stdc++.h>
#define isNum(c) c<='9' && c>='0'
#define islettre(c) c<='z' && c>='a'
#define isLETTRE(c) c<='Z' && c>='A'
#define MS0(x) memset(x,0,sizeof(x))
#define MS(x,s) memset(x,s,sizeof(x))
#define rep(i,n) for(i=0;i<n;i++)
#define rev(i,n) for(i=n;i>=0;i--)
#define repv(i,v) for(i=0;i<v.size();i++)
#define repa(i,a,n) for(i=a;i<n;i++)
#define all(c) c.begin(),c.end()
#define rall(c) c.rbegin(),c.rend()
#define NOT_VISITED 0
#define IS_VISITED 1
#define MOD 1000000009
#define INF 1000000009
#define COL 100002
#define trMap(c,i) for(map<char,int>::iterator i = (c).begin(); i != (c).end(); i++)
#define trSet(c,i) for(set< pair <int,char> >::iterator i = (c).begin(); i != (c).end(); i++)
#define PB(val) push_back(val)
#define MP(f,s) make_pair(f,s)
#define abs(i) (i<0)?-i:i
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> ii;
typedef vector< ii > vii;

void solve(int t){
	long long N;
	vector<int> v;
	cin >> N;
	long long n = N;
	while(n){
		v.push_back(n%10); n /= 10;
	}
	int i = 0;
	int fl = -1;
	while(i < v.size()-1){
		if(v[i] < v[i+1]){
			v[i] = 9;
			v[i+1] = (v[i+1] - 1 + 10)%10;
			fl = i;
		}
		i++;
	}
	cout << "Case #" << t << ": ";
	i = 0;
	while(i < fl) v[i++] = 9;
	i = 0;
	while(v[v.size() - 1 - i++] == 0);
	i--;
	while(i < v.size()) cout << v[v.size() - 1 - i++];
	cout << endl;
	return;
}

int main(){
	int T,i,j,k;
	cin >> T;
	i = 1;
	while(T--){
		solve(i++);
	}
	return 0;
}
