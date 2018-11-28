#define _CRT_SECURE_NO_WARNINGS
#include<iostream>
#include<sstream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<climits>
#include<cmath>
#include<string>
#include<vector>
#include<set>
#include<map>
#include<queue>
#include<numeric>
#include<functional>
#include<algorithm>
#include<bitset>
#include<tuple>
#include<unordered_set>
#include<random>
#include<array>
#include<cassert>
using namespace std;
#define INF (1<<29)
#define rep(i,n) for(int i=0;i<(int)(n);i++)
#define all(v) v.begin(),v.end()
#define uniq(v) v.erase(unique(all(v)),v.end())




int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	int n;
	long long ans,a;


	cin>>n;
	rep(i,n){
		string s;
		cin>>s;
		stringstream ss;
		ss<<s;
		long long in;
		ss>>in;

		int mi[20];
		mi[s.size()]=INF;
		for(int j=s.size()-1;j>=0;j--){
			mi[j] = min(mi[j+1],s[j]-'0');
		}
		bool f=false;
		ans=0;
		rep(j,s.size()){
			for  (int d=9;d>=0;d--){
				a=ans;
				for (int k=j; k<s.size();k++){
					a = a * 10 + d;
				}
				if (a <= in){
					ans = ans * 10 + d;
					break;
				}
			}
		}
		a=0;
		rep(j, s.size()-1){
			a = a * 10 + 9;
		}
		ans = max(ans,a);
		cerr << s << ' '<<ans<<endl;
		cout << "Case #" << (i + 1) << ": "<<ans<<endl;
	}

	return 0;
}