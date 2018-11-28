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

const int INF = 0x3f3f3f3f;
const double EPS = 1e-6;

using namespace std;

string line;
bool change(){
	bool res = true;
	for(int i = 0; i < line.size(); i++){
		if(!res) line[i] = '9';
		else if(i < line.size()-1 && line[i] > line[i+1]){
			res = false;
			line[i]--;
		}
	}
	return res;
}

int main(){
	int t, caso = 1; 
	scanf("%d%*c", &t);
	while(t--){
		cin >> line;
		while(!change());
		while(!line.empty() && line[0] == '0') line.erase(line.begin());
		printf("Case #%d: ", caso++); cout << line << endl;
	}
	return 0;
}
