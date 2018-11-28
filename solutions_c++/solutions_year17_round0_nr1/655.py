#include <bits/stdc++.h>
using namespace std;

#define fr(i,a,b) for(int i = a; i < (b); i++) 
#define fi first
#define se second
#define pb push_back
#define sc(a) scanf("%d", &a)
#define sc2(a,b) scanf("%d %d", &a, &b)
#define sc3(a,b,c) scanf("%d %d %d", &a, &b)
#define pri(a) printf("%d\n", a)
#define mp make_pair
#define DESYNC ios_base::sync_with_stdio(false)

typedef pair<int,int> ii;
typedef vector<ii> vii;
typedef vector<int> vi;
typedef long long int ll;

const int INF = 0x3f3f3f3f;
const ll LINF = 0x3f3f3f3f3f3f3f3f;
const int MOD = 1000000007;
const double PI = acos(-1);

int main(){
	string row;
	int t, n, cnt, k;
	int caseNum;
	
	cin>>t;
	
	fr(caseNum,1,t+1){
		cin>>row>>k;
		//cout<<row<<'\n';
		n = (int)row.size();
		cnt = 0;
		fr(i, 0, n-k+1){
			if(row[i] == '-'){
				fr(j,i,i+k){
					//cout<<j<<' ';
					if(row[j] == '+') row[j] = '-';
					else row[j] = '+';
				}
				cnt++;
				//cout<<'\n'<<row<<'\n';
			}
		}
		bool solved = 1;
		fr(i,0,n) if(row[i] == '-') solved = 0;
		
		cout<<"Case #"<<caseNum<<": ";
		if(solved) cout<<cnt<<'\n';
		else cout<<"IMPOSSIBLE\n";
	}
	
	return 0;
}
