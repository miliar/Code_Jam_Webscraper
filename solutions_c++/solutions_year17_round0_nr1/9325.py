
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
typedef priority_queue< ii > cola;



int T, K,R,s,pI;
string S;
bool REV[1005];
void flip(int p){
	int c = 0;
	for(int i = p ; i<s;i++){
		if(c==K) break;
		c++;
		REV[i] = !REV[i];
	}
	R++;
}
bool check(){
	//revisa inicio hasta el tamano de la espatula
	for(int i =pI; i< pI+K;i++){
		if(i>=s){
			pI=i;
			return true;
		}
		if(!REV[i]){
			pI = i;
			return false;
		}
	}
	pI +=K; 
	return true;
}
void solve(){
	while(pI < s){
		if(!check()){
			if(s-pI<K){
				R=-1;
				break;
			}else
				flip(pI);
		}
	}
}

int main()
{
ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
cin>>T;
int Tc = T;
while(T--){
	memset(REV,0,sizeof REV);
 R = 0;
 cin>>S>>K;
 s = S.size();
 pI =0;
 for(int i =0 ; i< s; i++){
 	if(S[i]=='+')REV[i]=true;
 }
 	solve();
	cout<<"Case #"<<(Tc-T)<<": "<<(R<0?"IMPOSSIBLE":to_string(R))<<endl;
}

return 0;
}