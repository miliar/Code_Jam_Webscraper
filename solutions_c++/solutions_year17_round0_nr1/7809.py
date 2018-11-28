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
		int k;
		string s;
		cin>>s>>k;
		int n = s.size();
		vector<bool> flipped(n + 1);
		bool flag = 0;
		int res = 0;
		REP(i, n){
			flag ^= flipped[i];
			bool ok = (s[i] == '+') ^ flag;
			if(!ok){
				res++;
				flag = !flag;
				if(i + k > n){
					goto end;
				}
				flipped[i + k] =  flipped[i + k] ^ 1;
			}
		}
		cout<<"Case #"<<_ + 1<<": "<<res<<"\n";
		continue;
		end:;
		cout<<"Case #"<<_ + 1<<": IMPOSSIBLE\n";
	}
}
