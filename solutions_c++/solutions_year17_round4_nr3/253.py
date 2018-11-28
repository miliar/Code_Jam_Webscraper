#include <bits/stdc++.h>

using namespace std;

#define pb push_back
typedef long long LL;

string b[60];
int r,c;
map<pair<int,int>, char > mp;
bool vis[60][60];

bool checkH(int x, int y){	
	int tx = x, ty = y-1;
	while( ty > -1 ){
		if( b[tx][ty] == '|' || b[tx][ty] == '-'  ) return false;
		if( b[tx][ty] == '#' ) break;
		ty--;
	}
	tx = x, ty = y+1;
	while( ty < c ){
		if( b[tx][ty] == '|' || b[tx][ty] == '-'  ) return false;
		if( b[tx][ty] == '#' ) break;
		ty++;
	}
	return true;
	
}

bool checkV(int x, int y){	
	int tx = x-1, ty = y;
	while(tx>=0){
		if( b[tx][ty] == '|' || b[tx][ty] == '-'  ) return false;
		if( b[tx][ty] == '#' ) break;
		tx--;
	}
	tx = x+1, ty = y;
	while(tx < r ){
		if( b[tx][ty] == '|' || b[tx][ty] == '-'  ) return false;
		if( b[tx][ty] == '#' ) break;
		tx++;
	}
	return true;
	
}

bool check(int x, int y){
	
	int r = 0;
	if(checkH(x,y)) r++;
//	cout << x << " " << y << " " << r << endl;
	if( checkV(x,y) ) r++;
//	cout << x << " " << y << " " << r << endl;
	if(!r) return false;
	if(r==1){
		if( checkH(x,y) ) mp[{x,y}] = '-';
		else mp[{x,y}] = '|';
	}
	return true;
}

void dfs(int x, int y){
	if(mp[{x,y}] == '|'){
		int tx = x-1, ty = y;
		while(tx>=0){			
			if( b[tx][ty] == '#' ) break;
			vis[tx][ty] = true;
			tx--;
		}
		tx = x+1, ty = y;
		while(tx < r ){			
			if( b[tx][ty] == '#' ) break;
			vis[tx][ty] = true;
			tx++;
		}
	}else{
		int tx = x, ty = y-1;
		while( ty > -1 ){			
			if( b[tx][ty] == '#' ) break;
			vis[tx][ty] = true;
			ty--;
		}
		tx = x, ty = y+1;
		while( ty < c ){			
			if( b[tx][ty] == '#' ) break;
			vis[tx][ty] = true;
			ty++;
		}
	}
}

int f(int x, int y){
	
	bool flagH = 0;
	int tx = x-1, ty = y;
	while(tx>=0){			
		if( b[tx][ty] == '#' ) break;
		if( b[tx][ty] == '|' || b[tx][ty] == '-'  ) {
			if( !mp[{tx,ty}]  ){
				flagH=true;
				break;
			} 
		}		
		tx--;
	}
	tx = x+1, ty = y;
	while(tx < r ){			
		if( b[tx][ty] == '#' ) break;
		if( b[tx][ty] == '|' || b[tx][ty] == '-'  ) {
			if( !mp[{tx,ty}]  ){
				flagH=true;
				break;
			} 
		}		
		tx++;
	}
	
	bool flagV = 0;
	tx = x, ty = y-1;
	while(ty>=0){			
		if( b[tx][ty] == '#' ) break;
		if( b[tx][ty] == '|' || b[tx][ty] == '-'  ) {
			if( !mp[{tx,ty}]  ){
				flagV=true;
				break;
			} 
		}		
		ty--;
	}
	tx = x, ty = y+1;
	while(ty < c ){			
		if( b[tx][ty] == '#' ) break;
		if( b[tx][ty] == '|' || b[tx][ty] == '-'  ) {
			if( !mp[{tx,ty}]  ){
				flagV=true;
				break;
			} 
		}		
		ty++;
	}
	return flagH+flagV;
}

void cover(int x, int y){
	int tx = x-1, ty = y;
	while(tx>=0){			
		if( b[tx][ty] == '#' ) break;
		if( b[tx][ty] == '|' || b[tx][ty] == '-'  ) {
			if( !mp[{tx,ty}]  ){
				mp[{tx,ty}] = '|';
				dfs(tx,ty);
				return;
			} 
		}		
		tx--;
	}
	tx = x+1, ty = y;
	while(tx < r ){			
		if( b[tx][ty] == '#' ) break;
		if( b[tx][ty] == '|' || b[tx][ty] == '-'  ) {
			if( !mp[{tx,ty}]  ){
				mp[{tx,ty}] = '|';
				dfs(tx,ty);
				return;
			} 
		}		
		tx++;
	}
	
	tx = x, ty = y-1;
	while(ty>=0){			
		if( b[tx][ty] == '#' ) break;
		if( b[tx][ty] == '|' || b[tx][ty] == '-'  ) {
			if( !mp[{tx,ty}]  ){
				mp[{tx,ty}] = '-';
				dfs(tx,ty);
				return;
			} 
		}		
		ty--;
	}
	tx = x, ty = y+1;
	while(ty < c ){			
		if( b[tx][ty] == '#' ) break;
		if( b[tx][ty] == '|' || b[tx][ty] == '-'  ) {
			if( !mp[{tx,ty}]  ){
				mp[{tx,ty}] = '-';
				dfs(tx,ty);
				return;
			} 
		}		
		ty++;
	}
}

void solve(int test){
	cout << "Case #" << test + 1 << ": ";
	cin >> r >> c;
	for(int i=0; i<r; i++){
		cin >> b[i];		
	}
	mp.clear();
	int num=0;
	for(int i=0; i<r; i++){
		for(int j=0; j<c; j++){
			if(b[i][j] == '|' || b[i][j] == '-' ){
				num++;	
				if(!check(i,j) ){
					cout <<  "IMPOSSIBLE" << endl;
					return;
				}
			}
		}
	}	
	memset(vis,0,sizeof vis);
	for(int i=0; i<r; i++){
		for(int j=0; j<c; j++){
			if( b[i][j] == '|' || b[i][j] == '-' || b[i][j]  == '#' ) vis[i][j] = true;
			if( b[i][j] == '|' || b[i][j] == '-'){
				if(mp[{i,j}]){
					dfs(i,j);
				}
			}
		}
	}
	while(true){
		bool flag=true;
		int ix = -1, iy = -1;
		for(int i=0; i<r; i++){
			if(flag)
				for(int j=0; j<c; j++){
					if(!vis[i][j]){
						int cnt = f(i,j);
						if(!cnt){
							cout <<  "IMPOSSIBLE" << endl;
							return;
						}
						if(cnt == 1){
							flag=false;
							ix = i;
							iy=j;	
							break;					
						}
					}
				}
		}
		if(!flag) cover(ix,iy);
		else break;		
	}
	cout << "POSSIBLE" << endl;
	for(int i=0; i<r; i++){
		for(int j=0; j<c; j++){
			if( b[i][j] == '|' || b[i][j] == '-'){
				if(mp[{i,j}]) cout << mp[{i,j}];
				else cout << '|';
			}
			else{
				cout << b[i][j];
			}
		}
		cout << endl;
	}
			
}


int ntest;
int main(){
	//freopen("test.in","r",stdin);
	freopen("C-small-attempt2.in","r",stdin);
	freopen("test.out","w",stdout);
	cin >> ntest;
	for(int test=0; test<ntest; test++){
		solve(test);
	}
	return 0;
}
