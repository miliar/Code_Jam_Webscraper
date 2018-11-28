#include <bits/stdc++.h>
using namespace std;
#define vi vector<int>
#define pii pair<int,int>
#define pb push_back
#define mp make_pair
#define all(x) x.begin(),x.end()
#define SZ(x) (int)(x.size())
#define rep(i,a,b) for(int i=a;i<b;i++)
#define per(i,a,b) for(int i=b-1;i>=a;i--)
#define inf 1000000007
#define mod 1000000007
#define ull unsigned long long
#define ll long long
template <class T,class U>inline void Max(T &a,U b){if(a<b)a=b;}
template <class T,class U>inline void Min(T &a,U b){if(a>b)a=b;}

char b[25][25];
bool colEmp[25];
bool rowEmp[25];
int main(){
	ios_base::sync_with_stdio(false);cin.tie(NULL);
	int T,R,C;
	cin >> T;
	for(int t=1;t<=T;++t) {
		cin >> R >> C;
		for(int i=0;i<R;++i){
			for(int j=0;j<C;++j){
				cin >> b[i][j];
			}
		}
		memset(colEmp,true,sizeof colEmp);
		memset(rowEmp,true,sizeof rowEmp);
		for(int i = 0;i<R;++i){
			for(int j=0;j<C;++j){
				if(b[i][j] != '?') {rowEmp[i] = false;colEmp[j] = false;}
			}
		}

		for(int i=0;i<R;++i){
			if(rowEmp[i]) continue;
			for(int j=0;j<C;++j){
				if(colEmp[j]) continue;
				int st = 0;int ed = 0;
				char val = '0';
				while(ed < R){
					if(b[ed][j] == '?') ++ed;
					else{
						val = b[ed][j];
						for(int k=st;k<ed;++k){
							b[k][j] = val;
						}
						st = ed+1;
						ed +=1;
					}
				}
				for(int k=st;k<ed;++k){
					b[k][j] = val;
				}
			}
		}

		for(int i=0;i<R;++i){
			if(rowEmp[i]){
				if(i==0){
					int j=1;
					while(j<R && rowEmp[j]) ++j;
					for(int k=0;k<C;++k){
						b[0][k] = b[j][k];
					}
				}else{
					for(int k=0;k<C;++k){
						b[i][k] = b[i-1][k];
					}
				}
			}
		}

		for(int j=0;j<C;++j){
			if(colEmp[j]){
				if(j==0){
					int i=1;
					while(i<C&&colEmp[i]) ++i;
					for(int k=0;k<R;++k){
						b[k][0] = b[k][i];
					}
				}else{
					for(int k=0;k<R;++k){
						b[k][j] = b[k][j-1];
					}
				}
			}
		}

		cout << "Case #" << t << ":" << endl;
		for(int i=0;i<R;++i){
			for(int j=0;j<C;++j){
				cout << b[i][j];
			}
			cout << endl;
		}
	}
}