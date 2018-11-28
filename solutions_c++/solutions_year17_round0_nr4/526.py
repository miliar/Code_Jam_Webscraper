#include "bits/stdc++.h"
using namespace std;
const int dataLen = 4;
struct data{
	int info[dataLen];
	int isize;
	data(){
		for(int e = 0; e < dataLen; e++)
			info[e] = 0;
		isize = 0;
	}
	int happy(int theta){
		if(theta == '.') return 0;
		if(theta == 'x') return 1;
		if(theta == 'o') return 2;
		return 3;
	}
	void insert(int theta){
		theta = happy(theta);
		info[theta]++;
		isize++;
	}
	void erase(int theta){
		theta = happy(theta);
		isize -= info[theta];
		info[theta] = 0;
	}
	int size(){
		return isize;
	}
};
const int maxn = 110;
char grid[maxn][maxn];
char orig[maxn][maxn];
char op[10*maxn*maxn];
int ax[10*maxn*maxn], ay[10*maxn*maxn];
int counter;
int n;
void clean(){
	for(int e = 0; e < maxn; e++)
		for(int f = 0; f < maxn; f++)
			grid[e][f] = orig[e][f] = '.';
}
bool valid(){
	data line[maxn], collum[maxn], diag[2][2*maxn];
	for(int e = 0; e < n; e++)
		for(int f = 0; f < n; f++){
			char cur = grid[e][f];
			line[e].insert(cur);
			collum[f].insert(cur);
			diag[0][e+f].insert(cur);
			diag[1][e-f+n-1].insert(cur);
		}
	for(int e = 0; e < n; e++){
		line[e].erase('+');
		line[e].erase('.');
		if(line[e].size() > 1)
			return false;
	}
	for(int e = 0; e < n; e++){
		collum[e].erase('+');
		collum[e].erase('.');
		if(collum[e].size() > 1)
			return false;
	}
	for(int r = 0; r < 2; r++)
		for(int e = 0; e < 2*n-1; e++){
			diag[r][e].erase('.');
			diag[r][e].erase('x');
			if(diag[r][e].size() > 1)
				return false;
		}
	return true;
}
bool canBe(int x, int y, int theta){
	grid[x][y] = theta;
	if(valid()) return true;
	grid[x][y] = '.';
	return false;
}
int main(){
	int cases; cin >> cases;
	for(int cs = 1; cs <= cases; cs++){
		cout << "Case #" << cs << ": ";
		counter = 0;
		clean();
		cin >> n;
		int edges; cin >> edges;
		if(cs == 77){
		//	fprintf(stderr, "%d %d\n", n, edges);
		}
		while(edges--){
			char type; int x, y;
			cin >> type >> x >> y;
			x--; y--;
			grid[x][y] = orig[x][y] = type;
		}
		bool hasO = false, hasX = false;
		for(int e = 0; e < n; e++) hasO |= grid[0][e] == 'o';
		for(int e = 0; e < n; e++) hasX |= grid[0][e] == 'x';
		if(!hasO && ! hasX){
			grid[0][0] = 'o';
			for(int e = 1; e < n; e++) grid[0][e] = '+', grid[e][e] = 'x';
			for(int e = 1; e < n-1; e++) grid[n-1][e] = '+';
			int ans = 0;
		} else {
			if(hasX){
				for(int e = 0; e < n; e++)
					if(grid[0][e] == 'x')
						grid[0][e] = 'o';
			}
			int ox, oy;
			for(int e = 0; e < n; e++) 
				if(grid[0][e] == 'o')
					ox = 0, oy = e;
			for(int e = 0; e < n; e++)
				if(grid[0][e] != 'o')
					grid[0][e] = '+';
			for(int e = 1; e < n; e++)
				grid[e][e] = 'x';
			if(oy)
				grid[oy][oy] = '.';
			for(int e = 1; e < n-1; e++)
				grid[n-1][e] = '+';
			bool did = false;
			for(int e = 0; e < n && !did; e++)
				for(int f = 0; f < n && !did; f++){
					if(grid[e][f] != '.') continue;
					else if(canBe(e, f, '+')) grid[e][f] = '+', did = true;
					else if(canBe(e, f, 'x')) grid[e][f] = 'x', did = true;
				}
		}
		int ans = 0;
		for(int e = 0; e < n; e++)
			for(int f = 0; f < n; f++)
				if(grid[e][f] != '.'){
					if(grid[e][f] == 'o') ans += 2;
					else ans++;
					if(grid[e][f] != orig[e][f]){
						op[counter] = grid[e][f];
						ax[counter] = e+1;
						ay[counter] = f+1;
						counter++;
					}
				}
	//	fprintf(stderr, "%d %d\n", cs, counter);
		if(ans != 3*n - 2) cerr << "wrong " << n <<  "\n";
		cerr << cs << endl;
		cout << ans << " " << counter << endl;
		for(int e = 0; e < counter; e++)
			cout << op[e] << " " << ax[e] << " " << ay[e] << endl;
	}
	return 0;
}

