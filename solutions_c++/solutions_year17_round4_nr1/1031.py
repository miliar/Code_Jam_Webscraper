#include <iostream>
using namespace std;

int q[4];
int c3[4][101][101];
int c4[4][101][101][101];


void testcase(){
	int n, p;
	cin >> n >> p;
	q[0] = q[1] = q[2] = q[3] = 0;
	for(int i=0; i<n; i++){
		int x; cin >> x;
		q[x%p]++;
	}
	
	int ans = q[0];
	if(p == 2){
		ans += (q[1]+1)/2;
		cout << ans << endl;
		return;
	}
	
	if(p == 3){
		ans += c3[0][q[1]][q[2]];
		cout << ans << endl;
		return;
	}
	
	if(p == 4){
		ans += c4[0][q[1]][q[2]][q[3]];
		cout << ans << endl;
		return;
	}
}

int main(){
	for(int x=0; x<=100; x++)
	for(int y=0; y<=100; y++)
	for(int l=0; l<3; l++){
		int r = 0;
		if(x > 0) r = max(r, c3[(l+2)%3][x-1][y] + (l==0 ? 1:0));
		if(y > 0) r = max(r, c3[(l+1)%3][x][y-1] + (l==0 ? 1:0));
		c3[l][x][y] = r;
	}
	
	for(int x=0; x<=100; x++)
	for(int y=0; y<=100; y++)
	for(int z=0; z<=100; z++)
	for(int l=0; l<4; l++){
		int r = 0;
		if(x > 0) r = max(r, c4[(l+3)%4][x-1][y][z] + (l==0 ? 1:0));
		if(y > 0) r = max(r, c4[(l+2)%4][x][y-1][z] + (l==0 ? 1:0));
		if(z > 0) r = max(r, c4[(l+1)%4][x][y][z-1] + (l==0 ? 1:0));
		c4[l][x][y][z] = r;
		//~ cerr << l << ' ' << x << ' ' << y << ' ' << z << " -> " << r << endl;
	}
	
	
	int t; cin >> t;
	for(int i=1; i<=t; i++){
		cout << "Case #" << i << ": ";
		testcase();
	}
	return 0;
}
