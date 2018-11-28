 #include <cstdio>
#include <iostream>
#include <algorithm>
#include <iterator> 
#include <string>
#include <vector>
using namespace std;
typedef long long LL;
#define int LL
typedef pair<int,int> PII;
#define MP make_pair
#define FOR(v,p,k) for(int v=p;v<=k;++v)
#define FORD(v,p,k) for(int v=p;v>=k;--v)
#define REP(i,n) for(int i=0;i<(n);++i)
#define VAR(v,i) __typeof(i) v=(i)
#define FOREACH(i,c) for(VAR(i,(c).begin());i!=(c).end();++i)
#define PB push_back
#define ST first
#define ND second
#define SIZE(x) (int)x.size()
#define ALL(c) c.begin(),c.end()

int32_t main(){
	ios_base::sync_with_stdio(0);
	int t;
	cin>>t;
	REP(_,t){
		string cs = "Case #" + to_string(_ + 1) + ": ";
		
		string s;
		cin>>s;
		int n = s.size();
		/*REP(i, n - 1){
			if(s[i] > s[i + 1]){
				goto nxt;
			}
		}
		cout<<cs<<s<<"\n";
		continue;
		nxt:;*/
		REP(i, n - 1){
			if(s[i] > s[i + 1]){
				while(i != 0 && s[i] == s[i - 1]){
					i--;
				}
				s[i]--;
				i++;
				while(i != n){
					s[i] = '9';
					i++;
				}
			}
		}
		if(s[0] == '0'){
			s = s.substr(1);
		}
		cout<<cs<<s<<"\n";
	}
}
