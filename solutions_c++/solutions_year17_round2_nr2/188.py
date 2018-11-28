#include <cstdio>
#include <algorithm>
#include <iostream>
#include <cmath>
#include <cstring>
#include <vector>
#include <map>
#include <set>

using namespace std;

#define X first
#define Y second

int ry,rb,yb,r,y,b,TT,n;

void goB(){
	if (!b)	return	;
	printf("B");
	b--;
	while (ry){
		ry--;
		printf("OB");
	}	
}

void goR(){
	if	(!r)	return	;
	printf("R");
	r--;
	while (yb){
		yb--;
		printf("GR");
	}
}

void goY(){
	if	(!y)	return	;
	printf("Y");
	y--;
	while (rb){
		rb--;
		printf("VY");
	}
}

bool test(){
	if	(ry){
		if	(ry > b || (ry == b && r+y+rb+yb>0))	return	false;
	}
	if	(rb){
		if	(rb > y || (rb == y && r+b+ry+yb>0))	return	false;
	}
	if	(yb){
		if	(yb > r || (yb == r && y+b+rb+ry>0))	return	false;
	}
	b -= ry;
	y -= rb;
	r -= yb;
	if	(b+y<r || b+r<y || r+y<b)	return	false;
	
	if	(b >= y && b >= r){
		while (b){
			if (y) goY();
			goB();
			if	(r>=b) goR();
		}
	}
	else if	(y >= b && y >= r){
		while (y){
			if (b) goB();
			goY();
			if	(r>=y) goR();
		}
	}
	else{
		while (r){
			if (b) goB();
			goR();
			if	(y>=r) goY();
		}
	}
	while (rb){
		printf("VY");
		rb--;
	}
	while (ry){
		ry--;
		printf("OB");
	}
	while (yb){
		yb--;
		printf("GR");
	}
	return	true;
}


int main(){
	freopen("2.in","r",stdin);
	freopen("2.out","w",stdout);
	scanf("%d",&TT);
	for	(int T=1;T<=TT;++T){
		scanf("%d%d%d%d%d%d%d",&n,&r,&ry,&y,&yb,&b,&rb);
		printf("Case #%d: ",T);
		if	(test())	printf("\n");
		else	printf("IMPOSSIBLE\n");
	}
	return	0;
}

