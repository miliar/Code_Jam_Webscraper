#include<vector>
#include<cmath>
#include<map>
#include<cstdlib>
#include<iostream>
#include<sstream>
#include<fstream>
#include<string>
#include<algorithm>
#include<cstring>
#include<cstdio>
#include<set>
#include<stack>
#include<bitset>
#include<functional>
#include<ctime>
#include<queue>
#include<deque>
#include<complex>
#include<cassert>
using namespace std;
#define pb push_back
#define pf push_front
typedef long long lint;
typedef complex<double> P;
#define mp make_pair
#define fi first
#define se second
typedef pair<int,int> pint;
#define All(s) s.begin(),s.end()
#define rAll(s) s.rbegin(),s.rend()
#define REP(i,a,b) for(int i=a;i<b;i++)
#define rep(i,n) REP(i,0,n)
vector<lint> zyo;
string moji(int a){
	string ret="";string r="";int amari;
	if(a==0) return "0";if(a<0) return "-"+moji(-a);
	while(a>0){
		amari=a%10;r+=(amari+'0');a/=10;
	}
	for(int i=0;i<r.size();i++) ret+=r[r.size()-(i+1)];
	return ret;
}
bool ch(string s){
	int n=s.size();
	rep(i,n-1){
		if(s[i]>s[i+1]) return false;
	}
	return true;
}
int main()
{
	zyo.pb(1);
	rep(i,18) zyo.pb(zyo[i]*10+1);
	int t;lint n;
	cin>>t;
	rep(i,t){
		cin>>n;
		lint ret=0;int now=0;
		for(int j=18;j>=0;j--){
			while(ret+zyo[j]<=n && now<9) now++,ret+=zyo[j];
		}
		printf("Case #%d: ",i+1);
		cout<<ret<<endl;
	}
}
