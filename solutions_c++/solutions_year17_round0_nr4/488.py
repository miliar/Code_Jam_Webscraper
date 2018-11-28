#include<bits/stdc++.h>
typedef long long ll;
using namespace std;

void mf(){
	//freopen("input.in","r",stdin);
	freopen("Dsmall6.in","r",stdin);
	freopen("Dsmall6.ou","w",stdout);

	// freopen("Dlarge.in","r",stdin);
	// freopen("Dlarge.ou","w",stdout);
}
int n, m;
char kitu[4] = {'.','+','x','o'};
int cross1[307][4],cross2[307][4], row[107][4], col[107][4];
int a[107][107], b[107][107];
bool fr[107][107];
void apply(int x, int y, int type, int val){
	a[x][y] = (val>0) ? type : 0;
	cross1[x+y+n][type]+= val;
	cross2[x-y+n][type]+= val;
	row[x][type]+= val;
	col[y][type]+= val;
}
bool canPutPlus(int x,int y){
	int x1 = x+y+n, x2 = x-y+n;
	if(cross1[x1][3] >0 || cross1[x1][1] > 0) return false;
	if(cross2[x2][3] >0 || cross2[x2][1] > 0) return false;
	return true;
}
bool canPutCross(int x, int y){	
	if(row[x][3] > 0 || row[x][2] > 0) return false;
	if(col[y][3] > 0 || col[y][2] > 0) return false;
	return true;
}
bool canPutO(int x, int y){
	return canPutCross(x,y) && canPutPlus(x,y);
}
bool canReplace(int x,int y){
	int v = a[x][y];
	if(v > 0) apply(x,y,v,-1);
	bool ok = canPutO(x, y);	
	if(v > 0) apply(x,y,v, 1);
	a[x][y] = v;
	return ok;
}
void saveRoot(){
	for(int i =1 ; i<=n;i++)
		for(int j = 1; j<=n; j++)
			b[i][j] = a[i][j];
}
void init(){
	for(int i = 1; i<= n;i++)
		for(int j = 1; j<= n; j++){
			fr[i][j] = true;
			a[i][j] = 0;
			b[i][j] = 0;
			for(int k = 0; k<=3;k++){
				row[i][k] =0;
				col[j][k] = 0;
				cross1[i+j+n][k] = 0;
				cross2[i-j+n][k] = 0;
			}				

		}
}
void _fillCross(int x, int y){
	for(int i = 1;i<=n-1;i++){
		x = x % n + 1;
		y = y % n + 1;
		if(a[x][y] == 0 ){
			apply(x,y,2,1);
		}
	}
}
void fillCross(){
	for(int i = 1; i<=min(n,2);i++)
		for(int j = 1; j<=n;j++){
			if(a[i][j]==1) continue;
			if(a[i][j]>1){
				_fillCross(i,j);
				return;
			}else{
				if(canPutCross(i,j)){
					apply(i,j,2,1);
					_fillCross(i,j);
					return;
				}
			}
		}
}
void solve(){	
	cin>>n>>m;
	init();
	int x,y; char c;
	while(m--){
		cin>>c>>x>>y;		
		switch(c){
			case 'o': apply(x,y,3,1);break;
			case 'x': apply(x,y,2,1);break;
			case '+': apply(x,y,1,1);break;
		}
	}
	saveRoot();		
	//find x first
	fillCross();		
	for(int i = 1; i<=n;i++){
		if(a[1][i] == 0 && canPutPlus(1,i)){
			apply(1,i,1,1);
		}		
	}	
	for(int i = 1; i <=n;i++){		
		if(a[n][i] == 0 && canPutPlus(n,i)){
			apply(n,i,1,1);
		}
	}
		
	for(int i = 1; i<=n;i++)
		for(int j =1 ; j <=n; j++){
			if(a[i][j] != 0 && a[i][j] != 3){
				if(canReplace(i,j)){
					apply(i,j,3,1);
				}
			}
		}
	int res = 0, rr = 0;
	for(int i = 1; i<=n; i++)
		for(int j = 1; j<=n;j++){
			res+= (a[i][j] + 1)/2;
			if(a[i][j] != b[i][j]) rr++;
		}
	cout<<res<<" "<<rr<<endl;

	for(int i = 1; i<=n; i++)
		for(int j = 1; j<=n;j++){			
	 		if(a[i][j] != b[i][j]){
	 			cout<<kitu[a[i][j]]<<" "<<i<<" "<<j<<endl;
	 		}
	 	}
	// for(int i =1;i<=n;i++){		
	// 	for(int j =1 ;j<=n;j++)
	// 		cout<<a[i][j];
	// 	cout<<endl;
	// }
}

int main(){
	ios_base::sync_with_stdio(false);
	#ifdef tuanh
		mf();
	#endif
	int ntest;
	cin>>ntest;
	for(int nt = 1; nt <= ntest; nt++){
		cout<<"Case #"<<nt<<": ";
		solve();	
	}
	
	return 0;
}