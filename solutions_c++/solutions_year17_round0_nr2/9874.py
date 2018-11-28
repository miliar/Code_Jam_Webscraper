
#ifdef ONLINE_JUDGE
#include <bits/stdc++.h>
#else
#include "/Users/erikmedina/bits/stdc++.h"
#endif

using namespace std;

typedef pair<int,int> ii;
typedef vector<ii> vii;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<bool> vb;
typedef vector<string> vs;
typedef queue<int> qi;
typedef queue<ii> qii;
typedef long long ll;
typedef pair<ll,int> lli;
typedef priority_queue< ii > cola;

#define MAX LONG_MAX
#define MAXDP 524300
#define PI acos(-1.0)
#define EPS 1e-9


int T;
ll N,R;
string S;
void solve(int pos){
	if(pos == S.size()-1) return;
	if(pos <0) pos =0;
	int ant = S[pos]-'0';
	bool todoNueve = false;
	for(int i = 1; i< S.size();i++){
		int val = S[i]-'0';
		if(todoNueve){ S[i]='9'; continue;}
		if(ant>val){
		// reducir una potencia
			S[i-1]--;
			
			S[i] = '9';
			
				for (int j = i; j < S.size(); ++j)
				{
					S[j]='9';
			
				}
				cerr<<S<<endl;
			solve(i-2); return;
			
		}else{
			ant = val;
		}
	}
}
int main()
{
ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
cin>>T;
int Tc = T;
while(T--){
	cin>>N;
S="";S = to_string(N);R=0;
solve(0);
if(S[0]=='0') S=S.substr(1);
	cout<<"Case #"<<(Tc-T)<<": "<<S<<endl;
}
return 0;
}