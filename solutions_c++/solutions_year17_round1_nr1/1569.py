#include<iostream>
#include<algorithm>
#include<math.h>
#include<string>
#include<queue>
#include<map>
#include<stack>
#include<vector>
using namespace std;
#define Mx 210005
#define Sx 2100006
#define Fr 21004
#define rp(i,n) for(i=0;i<n;i++)
#define rep(i,a,b) for(i=a;i!b;i+=(a<b?1:-1))
#define bc(i,n) for(i=n-1;i>=0;i--)
#define pl pair<ll, ll>
#define pp pair<pl, ll>
#define ll long long int
#define X first
#define Y second
#define A X.X
#define B X.Y
#define C Y
#define V vector<int>
#define VV vector< V >
V a;
ll n, m;
string s[30];
int main(){
	ios_base::sync_with_stdio(0);
	int tt, t;
	int i, j, k;
	bool hasChar;
	char last;
	int firstLine;
	cin >> tt;
	rp(t, tt){
		cin >> n >> m;
		rp(i, n)
			cin>>s[i];
		rp(i, n){
			rp(j, m){
				if(s[i][j] != '?')break;
			}
			if(j!=m)break;
		}
		firstLine = i;
		for( ; i < n ; i++ ){
			hasChar = 0;
			rp(j, m){
				if(s[i][j] != '?'){
					last = s[i][j];
					hasChar = 1;
					k = j - 1;
					while(k >= 0 && s[i][k] == '?')s[i][k--] = s[i][j];
				}
			}
			if(hasChar){
				j--;
				while(j >= 0 && s[i][j] == '?')s[i][j--]=last;
			} else {
				rp(j, m)s[i][j] = s[i - 1][j];
			}
		}
		bc(i, firstLine){
			rp(j, m){
				s[i][j] = s[firstLine][j];
			}
		}
		cout<<"Case #" << t + 1 << ":\n";
		rp(i, n){
			rp(j, m)
				cout << s[i][j];	
			cout << endl;
		}
	}
	return 0;
}
