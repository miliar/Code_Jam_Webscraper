//Qualification Round 2017
//Problem B. Tidy Numbers
#include <bits/stdc++.h>
using namespace std;
#define F first
#define S second
#define mp make_pair
#define pb push_back
#define CLEAR(a) memset(a,0,sizeof a)
#define REP(i,n) for(int i=0;i<n;i++)
#define FOR(i,a,b) for(int i=a;i<=b;i++)
#define fr freopen("input.txt", "r", stdin);
#define fw freopen("output.txt", "w", stdout);
typedef long long LL;
typedef pair<int,int> pii;
const int MOD = 1e9 + 7;
const int MAX = 1e5 + 5;

bool check(string n){
REP(i, n.size()-1){
if(n[i] > n[i+1]) return 0;
}
return 1;
}

int main() {
    fr;fw;
    int T, cases = 1;
    cin >> T;
    while(T--){
    	string N, ret= "";
    	cin >> N;
    	REP(i, N.size()) ret += '#';
        cout << "Case #" << cases++ <<": ";
    	if(check(N)){
    		cout << N <<"\n";
    		continue;
    	}

    	int flag = 0, sz = 0;

    	for(int i=0;i<N.size()-1;i++){
    		if(flag) break;
    		if(N[i] <= N[i+1]) {
    			ret[sz] = N[i];
    			sz++;
    		}
    		else{
    			if(sz){
    				ret[sz] = N[i]-1;
    				sz++;
    				while(sz >= 2 && ret[sz-1] < ret[sz-2]){
    					sz--;
    					ret[sz-1]--;
    				}
    				if(sz){
    					if(ret[sz-1] == '0') break;
    				}
    			}
    			else{
    				if(N[i]-1 == '0') break;
    				ret[sz] = N[i]-1;
    				sz++;
    			}
    			flag = 1;
    		}
    	}

    	if(flag){
    		while(sz < N.size()){
    		 ret[sz] = '9';
    		 sz++;
    		}
    	}

    	if(sz < N.size()){
    		REP(i, N.size()-1) cout << "9" ;
    		cout <<"\n";
    	}
    	else{
    		cout << ret <<"\n";
    	}
    }
    return 0;
}