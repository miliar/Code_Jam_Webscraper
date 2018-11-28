#include <bits/stdc++.h>
#define FOR(i,a,b) for(ut i=(a);i<(ut)(b);i++)
#define REP(i,b) FOR(i,0,b)
#define ALL(c) c.begin(),c.end()
#define PB push_back
#define cat //cout << __LINE__ << endl;
using namespace std;
typedef long long LL;
typedef double ld;
typedef LL ut;
typedef vector<ut> VI;
typedef pair<ut,ut> pr;
typedef vector<pr> Vpr;
typedef pair<ut,ut> prs;
const LL p=7+1e9;
const LL INF=1<<30;
const LL INFLL=1LL<<30;
inline void IN(ut &x){cin >> x;}
inline void INA(ut n,ut x[]){REP(i,n) cin >> x[i];}
inline void INE(ut m,VI edges[]){
	ut a,b;
	REP(i,m){
		cin >> a >> b;
		edges[a].PB(b);
		edges[b].PB(a);
	}
}
inline void INEC(ut m,Vpr edges[]){
	ut a,b,c;
	REP(i,m){
		cin >> a >> b >> c;
		edges[a].PB(pr(c,b));
		edges[b].PB(pr(c,a));
	}
}
const int SIZE=55;
LL N,M,C,H,W;
LL maps[SIZE][SIZE];
LL painted[SIZE][SIZE];
LL last[SIZE][SIZE];
const int dx[]={1,-1,0, 0};
const int dy[]={0, 0,1,-1};

void paint(int y,int x,int dir,int c){
	y+=dy[dir];
	x+=dx[dir];
	while(maps[y][x]==1){
		painted[y][x]+=c;
		y+=dy[dir];
		x+=dx[dir];
	}
}
void paints(int y,int x,int dir,int c){
	last[y][x]=dir;
	paint(y,x,dir,c);
	paint(y,x,dir+1,c);
}
bool avoid(int y,int x){
	REP(i,4){
		int ny=y,nx=x;
		REP(j,INF){
			ny+=dy[i];
			nx+=dx[i];
			if(maps[ny][nx]==0) break;
			else if(maps[ny][nx]>=2){
				if(i/2==0){ 
					maps[y][x]=3;
					break;
				}
				else{
					if(maps[y][x]==3) return false;
					maps[y][x]=4;
					break;
				}
			}		
		}
	}
	if(maps[y][x]==4) {
		paints(y,x,0,1);
	}
	else if(maps[y][x]==3){
		paints(y,x,2,1);
	}
	return true;
}
bool solve2(int y,int x){
	bool ans=false;
	if(x==W+1){
		FOR(i,1,H+1) FOR(j,1,W+1){
			if(maps[i][j]==1 and painted[i][j]==0) return false;
		}
		return true;
	}
	else if(y==H+1){
		return solve2(1,x+1);
	}
	else if(maps[y][x]==2){
		paints(y,x,0,1);
		ans|=solve2(y+1,x);
		paints(y,x,0,-1);
		if(ans) return true;
		paints(y,x,2,1);
		ans|=solve2(y+1,x);
		paints(y,x,2,-1);
	}
	else{
		return solve2(y+1,x);
	}
	return ans;
}
bool needs(int y,int x){
	if(painted[y][x]) return true;
	int times=0;
	int last=0;
	int my,mx;
	REP(i,4){
		int ny=y,nx=x;
		REP(j,INF){
			ny+=dy[i];
			nx+=dx[i];
			if(maps[ny][nx]==0) break;
			else if(maps[ny][nx]==2){
				times++;
				last=i;
				my=ny;
				mx=nx;
			}		
		}
	}
	if(times==0) return false;
	else if(times==1){
		if(last<=1){
			maps[my][mx]=4;
			paints(my,mx,0,1);
		}
		else{
			maps[my][mx]=3;
			paints(my,mx,2,1);
		}
	}
	return true;
}
bool solve(){
	REP(i,SIZE) REP(j,SIZE){
		maps[i][j]=0;
		painted[i][j]=0;
	}
	cin >> H >> W;
	LL mecas=0;
	string s;
	FOR(i,1,H+1){
		cin >> s;
		FOR(j,1,W+1){
			if(s[j-1]=='|' or s[j-1]=='-'){
				maps[i][j]=2;
				mecas++;
			}
			else if(s[j-1]=='#')
				maps[i][j]=0;
			else if(s[j-1]=='.')
				maps[i][j]=1;
		}
	}
	FOR(i,1,H+1) FOR(j,1,W+1){
		if(maps[i][j]==2){
			if(!avoid(i,j)) return false;
		}
	}
	FOR(i,1,H+1) FOR(j,1,W+1){
		if(maps[i][j]==1){
			if(!needs(i,j)) return false;
		}
	}
	
	return solve2(1,1);
}
int main(){
	int T;
	cin >> T;
	REP(i,T){
		cout << "Case #"<<i+1 <<": ";
		if(solve()){
			cout << "POSSIBLE" << endl;
			FOR(i,1,H+1) {
				FOR(j,1,W+1){
					if(maps[i][j]==0) cout <<"#";
					else if(maps[i][j]==1) cout <<".";
					else if(last[i][j]==0) cout <<"-";
					else cout << "|";
				}
				cout << endl;
			}
		}
		else cout << "IMPOSSIBLE" << endl;
	}
	return 0;
}