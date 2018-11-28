#include <bits/stdc++.h>
#define ll long long
#define vi vector<int>
#define ii pair<int,int>
#define vii vector<ii>
#define REPN(i,x,y) for(int i=x;i<y;i++)
#define REP(i,y) REPN(i,0,y)
#define REPR(i,y,x) for(int i=y;i>=x;i--)
#define CLR(A,x) memset(A,x,sizeof(A))
#define INF (1<<30)
#define EPS (1e-9)
#define ones(x) __builtin_popcount(x)
#define ALL(v) (v).begin(),(v).end()
#define RALL(v) (v).rbegin(),(v).rend()
#define pb push_back
#define mp make_pair
#define sqr(x) (x)*(x)
#define dbg(x) cout << #x << " = " << x << endl
#define dbg2(x,y)cout<<#x<<"="<<x<<" "<<#y<<"="<<y<<endl
#define dbg3(x,y,z)cout<<#x<<"="<<x<<" "<<#y<<"="<<y<<" "<<#z<<"="<<z<<endl
#define S(x)scanf("%d\n",&x)
#define SS(str) scanf("%[^\n]\n",str)
#define S2(x,y)scanf("%d %d\n",&x,&y)
#define SC(x)scanf("%d",&x)
#define SC2(x,y)scanf("%d %d",&x,&y)
#define P(x)printf("%d\n",x)
#define SZ(v) v.size()
#define f first
#define s second
#define MOD 100007
#define MAXN 100005
using namespace std;
string i2s(int x) { stringstream ss; ss << x; return ss.str();}
int s2i(string str) { istringstream ss(str);int nro; ss >> nro; return nro;}
int main(){
	int n;
	int k;
	string str;
	S(n);
	int cases=0;
	while(n--){
		cases++;
		cin >> str >> k;
		int move=0;
		REP(i,str.size()-k){
			if(str[i]=='-'){
				move++;
				REPN(j,i,i+k){
					str[j] = (str[j]=='+'?'-':'+');
				}
			}
		}
		//REP(i,str.size()){
			//putchar(str[i]);
		//}
		//putchar('\n');
		int existe=0;
		REP(i,str.size()){
			if(str[i]=='-'){
				existe+=1;
			}
		}
		
		if(existe==k or existe==0){
			if(existe==k){
				printf("Case #%d: %d\n",cases,move+1);
			} else {
				printf("Case #%d: %d\n",cases,move);	
			}
		} else {
			printf("Case #%d: IMPOSSIBLE\n",cases);	
		}
		
	}
	return 0;
}