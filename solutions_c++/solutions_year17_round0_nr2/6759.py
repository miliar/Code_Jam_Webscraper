#include <bits/stdc++.h>
using namespace std;

#define ri(x) scanf("%d",&x)
#define rii(x,y) scanf("%d %d",&x,&y)
#define riii(x,y,z) scanf("%d %d %d",&x,&y,&z)
#define FOR(i,j,k) for(int i = j; i<k; i++)
#define ROF(i,j,k) for(int i = j; i>=k; i--)
#define ms(obj,val) memset(obj,val,sizeof(obj))
#define pb push_back
string S;
int main(){
	int T; ri(T);
	for(int t = 1; t<=T; t++){
		printf("Case #%d: ",t);
		cin >> S;
		reverse(S.begin(),S.end());
		FOR(i,0,S.size()-1){
			if(S[i] < S[i+1]){
				S[i] = '9';
				S[i+1] = ((S[i+1] -'0') - 1) + '0';
			}
		}
		ROF(i,S.size()-1,1){
			if(S[i] > S[i-1]){
				S[i-1] = '9';
			}
		}
		reverse(S.begin(),S.end());
		for(int i = (S[0] == '0'); i<S.size(); i++) printf("%c",S[i]);
		printf("\n");
	}
}


