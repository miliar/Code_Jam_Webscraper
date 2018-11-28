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
bool istidy(int nro){
	if(nro/10 == 0) return 1;
	int id = nro%10,id2;
	nro /=10;
	int comparacion=0;
	int cont=0;
	while(nro){
		id2=nro%10;
		comparacion += (id2<=id);
		nro/=10;
		cont++;
		id = id2;
	}
	return cont==comparacion;
}
int main(){
	int cases;
	int n;
	S(cases);
	//dbg(cases);
	REP(i,cases){
		S(n);
		//dbg(n);
		REPR(j,n,1){
			//dbg(j);
			if(istidy(j)){
				// Prints solution
				//dbg(j);
				printf("Case #%d: %d\n",i+1,j);
				break;
			}
		}
	}
	return 0;
}