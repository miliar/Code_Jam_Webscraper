#include <bits/stdc++.h>

#define vi vector<int>
#define vpii vector< pair<int,int> >
#define pii pair<int,int>
#define mp(x,y) make_pair(x,y)
#define all(x) (x).begin(),(x).end()
#define FOREACH(it,x) for (auto it = (x).begin(); it!=(x).end(); ++it)
#define sz(x) (int)(x).size()
#define FOR(i,n) for (ll i = 0; i < ll(n); i++)
#define ROF(i,n) for (ll i = ((ll)n-1); i >= 0; i--)
#define FOR1(i,n) for (ll i = 1; i < ll(n); i++)
#define READ(a) int a; 0 == scanf("%d", &a);
#define READV(v,n) vi v(n);FOR(i,n){ 0 == scanf("%d", &v[si]);}
#define WRITE(v) FOR(i,sz(v))cout<<v[i]<<" ";
#define gmin(a,b) { if (b < a) a = b; }
#define gmax(a,b) { if (b > a) a = b; }
#define pb push_back
#define ff first
#define ss second
#define oo ((1LL<<62)+((1LL<<31)-1))
const double PI = std::atan(1.0)*4;
#define cpx complex<double>
#define MOD 1000000007ll
typedef long long ll;
typedef unsigned long long ull;
using namespace std;
#define MAXN 1005

int main(int argc, char *argv[]){
	READ(T);
	FOR(t, T){
		READ(r); READ(c);
		vector<string> board(r);
		FOR(i, r) cin>>board[i];
		FOR(k, r){
			char last = ' ';
			FOR(i, c){
				if(board[k][i]!='?'){
					if(i>0 && board[k][i-1]=='?'){
						FOR(ii, i) board[k][ii] = board[k][i];
					}
					last = board[k][i];
				}else	if(last!=' '){
					board[k][i] = last;
				}
			}
		}
		for(int k=r-1;k>0;k--){
			if(board[k][0]!='?' && board[k-1][0]=='?'){
				board[k-1] = board[k];
			}
		}
    FOR(k, r-1){
			if(board[k][0]!='?' && board[k+1][0]=='?'){
				board[k+1] = board[k];
			}
		}


		cout<<"Case #"<<(t+1)<<": "<<endl;
		FOR(k, r){
			cout<<board[k]<<endl;
		}

	}
	return 0;
}