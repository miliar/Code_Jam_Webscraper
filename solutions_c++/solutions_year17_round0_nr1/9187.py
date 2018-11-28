#include <bits/stdc++.h>
using namespace std; 
const int dx[]={1,0,-1,0,1,-1,-1,1}; 
const int dy[]={0,1,0,-1,1,1,-1,-1}; 
const int INF = 1e9; 
const long long LINF = 1e18; 
const double EPS = 1e-8; 
#define pb push_back
#define mk make_pair 
#define fr first 
#define sc second 
#define ll long long 
#define reps(i,j,k) for(int i = (j); i < (k); ++i) 
#define rep(i,j) reps(i,0,j) 
#define all(a) (a).begin(),(a).end() 
#define MOD 1000000007 
typedef pair<int,int> Pii;
typedef pair<Pii,int> P;
typedef vector<int> vi;
int main(){
	int T;
	cin >> T;
	reps(q,1,T+1){
		int cnt = 0;
		bool used[1024] = {};
		string str;
		cin >> str;
		int s;
		cin >> s;
		rep(i,str.size()){
			bool flg = false;
			if(str[i] == '-'){
				flg = true;
			}
			if(flg && !(i+s > str.size())){
				reps(j,i,i+s){
					if(used[j]){
						break;
					}
				}
				++cnt;
				//printf("%d ",i);
				//cout << str << endl;;
				reps(j,i,i+s){
					
					if(str[j] == '-'){
						used[j] = true;
						str[j] = '+';
					}
					else{
						str[j] = '-';
					}
				}	
			}
		}
		bool ok = true;
		rep(i,str.size()){
			if(str[i] == '-'){
				ok = false;
				break;
			}
		}
		printf("Case #%d: ",q);
		ok ? printf("%d\n",cnt) : puts("IMPOSSIBLE");
	}
	return 0;
}
