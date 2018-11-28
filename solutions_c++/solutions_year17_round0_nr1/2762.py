#include <bits/stdc++.h>

#define FOR(i, a, n) for(int i = (int)(a); i < (int)(n); ++i)
#define REP(i, n) FOR(i, 0, n)
#define all(a) a.begin(),a.end()
#define pb push_back
#define LSOne(S) (S & (-S))
#define dbg(x) cerr << ">>>> " << x << endl;
#define _ << " , " <<
#define mp make_pair
#define f first
#define s second
#define ii pair<int,int>
#define maxn 7777

typedef unsigned long long llu;
typedef long long int ll;
typedef long double ld;

const int INF = 1000000000;
const double EPS = 1e-6;

using namespace std;

int n,k;

int check(string line){
	int res = 0;
	REP(i,line.size()-k+1){
		if(line[i] == '-'){
			res++;
			for(int j = i; j < i+k; j++){
				line[j] = (line[j] == '+'? '-':'+');
			}
		}
	}
	REP(i,line.size()) if(line[i] == '-') return -1;
	return res;
}

int main(){
	int caso = 1;
	scanf("%d%*c", &n);
	while(n--){
		string line;
		cin >> line >> k;
		int r1 = check(line);
		reverse(all(line));
		int r2 = check(line);
		if(r1 == -1 && r2 == -1) printf("Case #%d: IMPOSSIBLE\n", caso++);
		else if(r1 == -1) printf("Case #%d: %d\n", caso++, r2);
		else if(r2 == -1) printf("Case #%d: %d\n", caso++, r1);
		else printf("Case #%d: %d\n", caso++, min(r1,r2));
	}
	return 0;
}





















