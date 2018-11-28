
#include <bits/stdc++.h>

#define REP(i, a) for(int i = 0; i < a; i++)
#define RFOR(i,x,y) for(int i = x; i>= y; i--)
#define FOR(i,x,y) for (int i = x; i < y; i++)
#define ITFOR(it,A) for(typeof A.begin() it = A.begin(); it!=A.end(); it++)
#define all(v) (v).begin(), (v).end()
#define rall(v) (v).rbegin(), (v).rend()
#define VE vector <int>
#define mset(A,x) memset(A, x, sizeof A)
#define PB push_back
#define ones(x) __builtin_popcount(x)
#define cua(x) (x)*(x)
#define debug(x) cout <<#x << " = " << x << endl
#define adebug(x,n) cout <<#x<<endl; REP(i,n)cout<<x[i]<<char(i+1==n?10:32)
#define mdebug(x,m,n) cout <<#x<<endl; REP(i,m)REP(j,n)cout<<x[i][j]<<char(j+1==n?10:32)
#define LSOne(S) (S&(-S))

using namespace std;

#define ll long long
#define lli long long int
#define PI acos(-1.0)
#define ii pair<int,int>
#define inf_ll (((1LL<<62)-1)<<1)+1
#define inf_i (1<<30)-1

int main(){
/*
freopen("B-large.in", "r", stdin);
freopen("out.txt", "w", stdout);
*/
	int T,tam,c=0; scanf("%d",&T);
	string cad;
	while(T--){
		cin>>cad; tam=cad.size(); c++;
		REP(i,tam-1){
			if(cad[i]>cad[i+1]){
				cad[i]=cad[i]-1;
				FOR(j,i+1,tam) cad[j]='9';
				RFOR(j,i-1,0){
					if(cad[j]>cad[j+1]){
						cad[j]=cad[j]-1;
						cad[j+1]='9';
					}
					else break;
				}
				break;
			}
		}
		printf("Case #%d: ",c);
		REP(i,tam){
			if(i==0&&cad[i]=='0');
			else cout<<cad[i];
		}
		cout<<endl;
	}
/*
fclose(stdin);
fclose(stdout);
*/
  return 0;
}




