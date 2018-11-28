#include<iostream>
#include<algorithm>
#include<math.h>
#include<string>
#include<queue>
#include<map>
#include<stack>
#include<vector>
using namespace std;
#define Mx 210005
#define Sx 2100006
#define Fr 21004
#define rp(i,n) for(i=0;i<n;i++)
#define rep(i,a,b) for(i=a;i!b;i+=(a<b?1:-1))
#define bc(i,n) for(i=n-1;i>=0;i--)
#define pl pair<ll, ll>
#define pp pair<pl, ll>
#define ll long long int
#define X first
#define Y second
#define A X.X
#define B X.Y
#define C Y
#define V vector<int>
#define VV vector< V >
V a;
string s;
inline int change(char x){
	return x=='-'?1:0;
}
int main(){
	ios_base::sync_with_stdio(0);
	int tt, t;
	cin>>tt;
	rp(t,tt){
		a.clear();
		int c = 0, l, total = 0, loc = 0, k;
		int i, j;
		cin>>s>> k;
		l = s.size();
		rp(i,l){
			if(change(s[i]) ^ (c%2)){
				if(l - i < k)break;
				c++;
				total++;
				a.push_back(i);
			}
			if(loc < a.size() && a[loc] == i - k + 1){
				loc++;
				c--;
			}
		}
		cout << "Case #"<<t+1<<": ";
		if(i < l){
			cout<< "IMPOSSIBLE\n";
		}
		else{
			cout<<total<<endl;
		}
	}
	return 0;
}
