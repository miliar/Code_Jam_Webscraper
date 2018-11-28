#include <iostream>
#include <fstream>
#include <string>
#include <set>
#include <vector>

using namespace std;

//#define ifs cin
//#define ofs cout
ifstream ifs("D-small-attempt1.in");ofstream ofs("1.out");
//ifstream ifs("C-small-2-attempt0.in");ofstream ofs("2.out");
//ifstream ifs("C-large.in");ofstream ofs("3.out");

struct solver{
	vector<int> field[2];
	int size;

	solver(int n){
		size = n;
		field[0].resize(n*n);
		field[1].resize(n*n);
		for(int i = 0;i < n*n;i++){
			field[0][i] = 1; field[1][i] = 1;
		}
	}

	void opten(int x,int y){
		for(int i = 0;i < size;i++){
			if(i != x){
				field[0][y*size+i] = 0;
			}
		}
		for(int i = 0;i < size;i++){
			if(i != y){
				field[0][i*size+x] = 0;
			}
		}
	}

	void opcross(int x,int y){
		for(int i = 0;i < size;i++){
			if(i != y && 0 <= x+y-i && x+y-i < size){
				field[1][i*size+x+y-i] = 0;
			}
		}
		for(int i = 0;i < size;i++){
			if(i != y && 0 <= x-y+i && x-y+i < size){
				field[1][i*size+x-y+i] = 0;
			}
		}
	}

	void add(int c,int y,int x){
		switch(c){
		case 0:
			opten(x,y);
			break;
		case 1:
			opcross(x,y);
			break;
		}
		field[c][y*size+x] = 2;
	}

};
void solve(int time){
	int n,m;
	ifs >> n >> m;
	int ans = 0,ansm = 0;
	solver sv(n);
	for(int i = 0;i < m;i++){
		char c;
		int x,y;
		ifs >> c >> x >> y;
		x--;y--;
		switch(c){
		case 'o':
			sv.add(0,x,y);
			sv.add(1,x,y);
			ans += 2;
			break;
		case 'x':
			sv.add(0,x,y);
			ans++;
			break;
		case '+':
			sv.add(1,x,y);
			ans++;
			break;
		}
	}
	set<int> sp;
	for(int i = 0;i < 2;i++){
		for(int j = 0;j < n*n;j++){
			if(j < n || j >= n*(n-1) || j%n == 0 || j%n == n-1)
			if(sv.field[i][j] == 1){
				sv.add(i,j/n,j%n);
				sp.insert(j);
				ans++;
			}
		}
		for(int j = 0;j < n*n;j++){
			if(!(j < n || j >= n*(n-1) || j%n == 0 || j%n == n-1))
			if(sv.field[i][j] == 1){
				sv.add(i,j/n,j%n);
				sp.insert(j);
				ans++;
			}
		}
	}
	ofs << "Case #" << time << ": " << ans << ' ' << sp.size() << endl;
	for(set<int>::iterator itr = sp.begin(); itr != sp.end(); ++itr) {
		if(sv.field[0][*itr]){
			if(sv.field[1][*itr]){
				ofs << "o " << *itr/n+1 << " " << *itr%n+1 << endl;
			}
			else{
				ofs << "x " << *itr/n+1 << " " << *itr%n+1 << endl;
			}
		}else if(sv.field[1][*itr]){
			ofs << "+ " << *itr/n+1 << " " << *itr%n+1 << endl;
		}
	}
}

int main() {
	int t;
	ifs >> t;
	cout << "start" << endl;
	for(int i = 1;i <= t;i++){
		solve(i);
	}
	cout << "fin" << endl;
	return 0;
}
