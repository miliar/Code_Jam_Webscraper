#include<stdio.h>
#include<string.h>
#include<assert.h>
#include<algorithm>
using namespace std;
int r,ry,y,yb,b,br,n;
char out[1111];
char ttt[1111];int lttt;
void output(char a,char b,int w){
	for(int i=0; i<w; i++){
		ttt[lttt++] = a;
		ttt[lttt++] = b;
	}
}
int pnt,tot;
void put(int c,char ch){
	for(int i=0; i<c; i++){
		while(out[pnt] != 0){
			pnt++;if(pnt == tot)pnt=0;
		}
		out[pnt] = ch;
		pnt++;if(pnt == tot)pnt=0;
		if(i == c-1)break;
		pnt++;if(pnt == tot)pnt=0;
	}
}
bool proc(){
	if(b < ry)return false;
	if(r < yb)return false;
	if(y < br)return false;

	if(b == ry && b > 0){
		if(b+ry == n){
			output('B','O', n/2);
			return true;
		}
		return false;
	}
	b -= ry;

	if(r == yb && r > 0){
		if(r+yb == n){
			output('R','G', n/2);
			return true;
		}
		return false;
	}
	r -= yb;

	if(y == br && y > 0){
		if(y+br == n){
			output('Y','V', n/2);
			return true;
		}
		return false;
	}
	y -= br;

	if(max(max(r,y),b) * 2 > b + r + y)return false;

	tot = b + r + y;
	pnt = 0;
	memset(out,0,sizeof(out));
	if(b >= r && r >= y){put(b,'B'); put(r,'R'); put(y,'Y');}else
	if(b >= y && y >= r){put(b,'B'); put(y,'Y'); put(r,'R');}else
	if(r >= b && b >= y){put(r,'R'); put(b,'B'); put(y,'Y');}else
	if(r >= y && y >= b){put(r,'R'); put(y,'Y'); put(b,'B');}else
	if(y >= b && b >= r){put(y,'Y'); put(b,'B'); put(r,'R');}else
	if(y >= r && r >= b){put(y,'Y'); put(r,'R'); put(b,'B');}
	bool fb = false, fr = false, fy = false;
	for(int i=0; i<tot; i++){
		ttt[lttt++] = out[i];
		if((out[i] == 'B') && !fb){
			fb = true;
			output('O','B', ry);
		}else
		if((out[i] == 'R') && !fr){
			fr = true;
			output('G','R', yb);
		}else
		if((out[i] == 'Y') && !fy){
			fy = true;
			output('V','Y', br);
		}		
	}
	return true;
}
int R,_R,Y,_Y,B,_B;
bool chk(){
	if(n != lttt)return false;
	int R1 = 0, _R1 = 0, Y1 = 0, _Y1 = 0, B1 = 0, _B1 = 0;
	for(int i=0; i<n; i++){
		char c = ttt[i];
		char c2 = ttt[(i+1)%n];
		if(c == 'R')R1++;
		if(c == 'B')B1++;
		if(c == 'Y')Y1++;
		if(c == 'O')_B1++;
		if(c == 'G')_R1++;
		if(c == 'V')_Y1++;
		if(c == 'R' && (c2 == 'R' || c2 == 'O' || c2 == 'V'))return false;
		if(c == 'B' && (c2 == 'B' || c2 == 'G' || c2 == 'V'))return false;
		if(c == 'Y' && (c2 == 'Y' || c2 == 'O' || c2 == 'G'))return false;
		if(c == 'O' && c2 != 'B')return false;
		if(c == 'G' && c2 != 'R')return false;
		if(c == 'V' && c2 != 'Y')return false;
	}
	if(R != R1)return false;
	if(Y != Y1)return false;
	if(B != B1)return false;
	if(_R != _R1)return false;
	if(_Y != _Y1)return false;
	if(_B != _B1)return false;
	return true;
}
int main(){
	int _,t;
	scanf("%d",&_);
	for(t=1; t<=_; t++){
		printf("Case #%d: ",t);
		scanf("%d%d%d%d%d%d%d",&n,&r,&ry,&y,&yb,&b,&br);
		R = r;
		_R = yb;
		Y = y;
		_Y = br;
		B = b;
		_B = ry;
		lttt = 0;
		if(!proc())puts("IMPOSSIBLE");else{
			ttt[lttt] = 0;
			puts(ttt);
			assert(chk());
//			puts("");
		}
	}
	return 0;
}
