#define _CRT_SECURE_NO_WARNINGS
#include <bits/stdc++.h>
using namespace std;
typedef long long               ll;
typedef pair<int, int>          pii;
typedef vector<int>             vi;
#define SYNC		ios_base::sync_with_stdio(0);cin.tie(0); 
ll MOD = 1000000007;
#define rep(i,b)   for (int i=0; i < b; i++)
#define fi           first
#define se           second
#define pb           push_back
#define mp           make_pair
#define dzx 		cerr<<"here";
#define deb(x)		cerr << #x << " here "<< x;
#define debn(x)		cerr << #x << " here " << x << "\n"; 
//START
int main()
{
	SYNC
	int t;
	cin>>t;
	int temp = t;
	while(t--){
		int r,c;
		cin>>r>>c;
		char A[r+5][c+5];
		rep(i,r) rep(j,c) cin>>A[i][j];
		rep(i,r){
			rep(j,c){
				if(A[i][j]!='?'){
					int x = j+1;
					int y = j-1;
					while(x<c && A[i][x]=='?'){
						A[i][x]=A[i][j];
						x++;
					}
					while(y>=0 && A[i][y]=='?'){
						A[i][y]=A[i][j];
						y--;
					}
				}
			}
		}
		rep(i,r){
			if(A[i][0] != '?'){
				int x = i+1;
				int y = i-1;
				while(x<r && A[x][0] == '?'){
					rep(j,c){
						A[x][j] = A[i][j];
					}
					x++;
				}
				while(y>=0 && A[y][0] == '?'){
					rep(j,c){
						A[y][j] = A[i][j];
					}
					y--;
				}
			}
		}

		cout<<"Case #"<<temp-t<<":"<<endl;
		rep(i,r) {
			rep(j,c)
				cout<<A[i][j];
				cout<<endl;
		}
	}
	return 0;
}