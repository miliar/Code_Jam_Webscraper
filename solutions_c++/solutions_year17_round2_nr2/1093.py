#include<bits/stdc++.h>
using namespace std;
#define REP(_x,_y) for(int (_x)=0;(_x)<(_y);(_x)++)
#define FOR(_x,_y,_z) for(int (_x)=(_y);(_x)<=(_z);(_x)++)
#define FORD(_x,_y,_z) for(int (_x)=(_y);(_x)>=(_z);(_x)--)
#define RESET(_x,_y) memset((_x),(_y),sizeof(_x))
#define SZ(_x) ((int)(_x).size())
#define LEN(_x) strlen(_x)
#define ALL(_x) (_x).begin(),(_x).end()
#define LL long long
#define ULL unsigned LL
#define PII pair<int,int>
#define VI vector<int>
#define VII vector< PII >
#define VVI vector< VI >
#define MP make_pair
#define PB push_back
#define FI first
#define SE second
const int INF=1e9;
const int MOD=1e9+7;
// >.<
int t,tc=1,n,r,o,y,g,b,v;
char an[1001];
bool is_valid(int x){
	if(an[x]=='R'){
		if(an[(x-1+n)%n]=='R')return 0;
		if(an[(x-1+n)%n]=='O')return 0;
		if(an[(x-1+n)%n]=='V')return 0;
		if(an[(x+1)%n]=='R')return 0;
		if(an[(x+1)%n]=='O')return 0;
		if(an[(x+1)%n]=='V')return 0;
	}
	if(an[x]=='Y'){
		if(an[(x-1+n)%n]=='Y')return 0;
		if(an[(x-1+n)%n]=='O')return 0;
		if(an[(x-1+n)%n]=='G')return 0;
		if(an[(x+1)%n]=='Y')return 0;
		if(an[(x+1)%n]=='O')return 0;
		if(an[(x+1)%n]=='G')return 0;
	}
	if(an[x]=='B'){
		if(an[(x-1+n)%n]=='B')return 0;
		if(an[(x-1+n)%n]=='G')return 0;
		if(an[(x-1+n)%n]=='V')return 0;
		if(an[(x+1)%n]=='B')return 0;
		if(an[(x+1)%n]=='G')return 0;
		if(an[(x+1)%n]=='V')return 0;
	}
	if(an[x]=='O'){
		if(an[(x-1+n)%n]=='O')return 0;
		if(an[(x-1+n)%n]=='R')return 0;
		if(an[(x-1+n)%n]=='Y')return 0;
		if(an[(x+1)%n]=='O')return 0;
		if(an[(x+1)%n]=='R')return 0;
		if(an[(x+1)%n]=='Y')return 0;
	}
	if(an[x]=='G'){
		if(an[(x-1+n)%n]=='G')return 0;
		if(an[(x-1+n)%n]=='Y')return 0;
		if(an[(x-1+n)%n]=='B')return 0;
		if(an[(x+1)%n]=='G')return 0;
		if(an[(x+1)%n]=='Y')return 0;
		if(an[(x+1)%n]=='B')return 0;
	}
	if(an[x]=='V'){
		if(an[(x-1+n)%n]=='V')return 0;
		if(an[(x-1+n)%n]=='R')return 0;
		if(an[(x-1+n)%n]=='B')return 0;
		if(an[(x+1)%n]=='V')return 0;
		if(an[(x+1)%n]=='R')return 0;
		if(an[(x+1)%n]=='B')return 0;
	}
	return 1;
}
void solve(){
	REP(i,n)an[i]='?';
	REP(i,n){
		bool can=0;
		if(r>0){
			an[i]='R';
			if(is_valid(i)){
				can=1;
				r--;
				continue;
			}
			else{
				REP(j,i){
					swap(an[i],an[j]);
					if(is_valid(i)&&is_valid(j)){
						can=1;
						r--;
						break;
					}
					swap(an[i],an[j]);
				}
			}
			if(!can)an[i]='?';
		}
		if(o>0&&!can){
			an[i]='O';
			if(is_valid(i)){
				can=1;
				o--;
				continue;
			}
			else{
				REP(j,i){
					swap(an[i],an[j]);
					if(is_valid(i)&&is_valid(j)){
						can=1;
						o--;
						break;
					}
					swap(an[i],an[j]);
				}
			}
			if(!can)an[i]='?';
		}
		if(y>0&&!can){
			an[i]='Y';
			if(is_valid(i)){
				can=1;
				y--;
				continue;
			}
			else{
				REP(j,i){
					swap(an[i],an[j]);
					if(is_valid(i)&&is_valid(j)){
						can=1;
						y--;
						break;
					}
					swap(an[i],an[j]);
				}
			}
			if(!can)an[i]='?';
		}
		if(g>0&&!can){
			an[i]='G';
			if(is_valid(i)){
				can=1;
				g--;
				continue;
			}
			else{
				REP(j,i){
					swap(an[i],an[j]);
					if(is_valid(i)&&is_valid(j)){
						can=1;
						g--;
						break;
					}
					swap(an[i],an[j]);
				}
			}
			if(!can)an[i]='?';
		}
		if(b>0&&!can){
			an[i]='B';
			if(is_valid(i)){
				can=1;
				b--;
				continue;
			}
			else{
				REP(j,i){
					swap(an[i],an[j]);
					if(is_valid(i)&&is_valid(j)){
						can=1;
						b--;
						break;
					}
					swap(an[i],an[j]);
				}
			}
			if(!can)an[i]='?';
		}
		if(v>0&&!can){
			an[i]='V';
			if(is_valid(i)){
				can=1;
				v--;
				continue;
			}
			else{
				REP(j,i){
					swap(an[i],an[j]);
					if(is_valid(i)&&is_valid(j)){
						can=1;
						v--;
						break;
					}
					swap(an[i],an[j]);
				}
			}
			if(!can)an[i]='?';
		}
		if(i==n-1){
			if(r>0)an[i]='R';
			if(o>0)an[i]='O';
			if(y>0)an[i]='Y';
			if(g>0)an[i]='G';
			if(b>0)an[i]='B';
			if(v>0)an[i]='V';
			assert(r+o+y+g+b+v<=1);
			REP(j,n-1){
				REP(k,n-1){
					if(j==k)continue;
					swap(an[j],an[k]);
					if(is_valid(i)&&is_valid(j)&&is_valid(k)){
						can=1;
						break;
					}
					swap(an[j],an[k]);
				}
			}
		}
		if(!can){
			puts("IMPOSSIBLE");
			return;
		}
	}
	REP(i,n)printf("%c",an[i]);
	puts("");
}
int main(){
	scanf("%d",&t);
	while(t--){
		scanf("%d %d %d %d %d %d %d",&n,&r,&o,&y,&g,&b,&v);
		printf("Case #%d: ",tc++);
		solve();
	}
	return 0;
}