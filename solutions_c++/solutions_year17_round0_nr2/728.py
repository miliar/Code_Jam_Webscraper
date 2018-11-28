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
#define rep(i,a,b) for(i=a;i!=b;i+=(a<b?1:-1))
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
ll l;
string s;
int main(){
	ios_base::sync_with_stdio(0);
	int tt, t;
	cin>>tt;
	rp(t, tt){
		int i, j;
		char tm;
		cin>>s;
		l = s.size();
		rep(i, 1, l)
			if(s[i]<s[i-1])break;
		if(i!=l){
			i--;
			j = i;
			while(j > 0 && s[j]==s[i]){
				j--;
			}
			i = j + (s[j]!=s[i]?1:0);
			s[i]--;
			for(i++;i<l;i++)s[i]='9';
			//i = 0;
			//while(s[i] == '0')i++;
			if(s[0]=='0')s=s.substr(1);
		}
		cout<<"Case #"<< t+1<<": "<<s<<endl;
	}
	return 0;
}
