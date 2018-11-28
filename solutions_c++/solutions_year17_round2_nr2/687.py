//Aleksander Łukasiewicz
#include<bits/stdc++.h>
using namespace std;

#define fru(j,n) for(int j=0; j<(n); ++j)
#define tr(it,v) for(typeof((v).begin()) it=(v).begin(); it!=(v).end(); ++it)
#define x first
#define y second
#define pb push_back
#define mp make_pair
#define ALL(G) (G).begin(),(G).end()

typedef long long LL;
typedef pair<int,int> PII;
typedef vector<int> VI;

const int INF = 1000000009;
const int MAXN = 1000000;

struct unicorn{
	int cnt;
	char c;
	
	unicorn(int _cnt, char _c){
		cnt = _cnt;
		c = _c;
	}
	
	friend bool operator < (unicorn A, unicorn B){
		return A.cnt > B.cnt;
	}
};

string Solve(int n, int R, int Y, int B){
	vector< unicorn > cand;
	cand.pb(unicorn(R, 'R'));
	cand.pb(unicorn(Y, 'Y'));
	cand.pb(unicorn(B, 'B'));
	
	string prev = "#";
	string suf = "$";
	
	while(n > 1){
		sort(cand.begin(), cand.end());
		if(cand[1].cnt == 0)
			return "IMPOSSIBLE";
		
		cand[0].cnt--;
		cand[1].cnt--;
		char X = cand[0].c;
		char Z = cand[1].c;
		
		prev += X;
		suf += Z;
		
		int k = prev.size()-1;
		if(prev[k-1] == X || suf[k-1] == Z)
			swap(prev[k], suf[k]);
		n -= 2;
	}
	
	if(n == 1){
		sort(cand.begin(), cand.end());
		char X = cand[0].c;
		int k = prev.size()-1;
		if(prev[k] == X || suf[k] == X)
			return "IMPOSSIBLE";
		prev += X;
	}
	
	prev.erase(0, 1);
	suf.erase(0, 1);
	reverse(suf.begin(), suf.end());
	return prev + suf;
}

int main(){
    int t;
	scanf("%d", &t);
	for(int pp=1; pp<=t; pp++){
		int n, R, O, Y, G, B, V;
		scanf("%d %d %d %d %d %d %d", &n, &R, &O, &Y, &G, &B, &V);
		printf("Case #%d: %s\n", pp, Solve(n, R, Y, B).c_str());
	}
    
return 0;
}