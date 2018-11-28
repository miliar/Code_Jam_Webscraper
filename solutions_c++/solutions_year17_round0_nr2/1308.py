#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#include <algorithm>
#include <set>
#include <map>

#define rep(i,n) for(int i=0; i<(n); i++)
#define reps(i,x,n) for(int i=x; i<(n); i++)
#define rrep(i,n) for(int i=(n)-1; i>=0; i--)
#define all(X) (X).begin(),(X).end()
#define X first
#define Y second
#define pb push_back
#define eb emplace_back

using namespace std;
typedef long long int ll;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;

template<class T> bool chmax(T &a, const T &b) { if (a<b) { a=b; return 1; } return 0; }
template<class T> bool chmin(T &a, const T &b) { if (a>b) { a=b; return 1; } return 0; }

template<class A, size_t N, class T> void Fill(A (&a)[N], const T &v){ fill( (T*)a, (T*)(a+N), v ); }

const ll INF = 0x3fffffff;


int main(){
	//ios_base::sync_with_stdio(0);
	int T;

	cin >> T;
	for(int kase=1; kase<=T; kase++){
		string S, ans;

		cin >> S;
		rep(i,S.length()) if(i){
			if( S[i-1] > S[i] ){
				for(int j=i-1; j>=0; j--){
					if( S[j] > S[j+1] ){
						S[j+1] = '9';
						S[j]--;
						if( S[j] < '0' ) S[j] = '9';
					}else{
						break;
					}
				}
				for(int j=i; j<S.length(); j++) S[j] = '9';
				if( S[0] == '0' ){
					S = S.substr(1);
					rep(j,S.length()) S[j] = '9';
				}
				break;
			}
		}

		cout << "Case #" << kase << ": ";
		cout << S << endl;
	}

	return 0;
}
