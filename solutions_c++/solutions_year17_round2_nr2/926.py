#include <iostream>
#include <fstream>
#include <string>
#include <set>
#include <vector>
#include <algorithm>

using namespace std;

//#define ifs cin
//#define ofs cout
//ifstream ifs("B-small-attempt2.in");ofstream ofs("1.out");
ifstream ifs("B-large.in");ofstream ofs("2.out");
//ifstream ifs("C-large.in");ofstream ofs("3.out");

void solve(int time){
	int n;
	int r,o,y,g,b,v;
	ifs >> n >> r >> o >> y >> g >> b >> v;
	string ans = "";
	if(r+g == n){
		if(r == g){
			for(int i = 0;i < n/2;i++){
				ans = ans + "RG";
			}
		}
		else ans = "IMPOSSIBLE";
	}
	else if(y+v == n){
		if(y == v){
			for(int i = 0;i < n/2;i++){
				ans = ans + "YV";
			}
		}
		else ans = "IMPOSSIBLE";
	}
	else if(o+b == n){
		if(o == b){
			for(int i = 0;i < n/2;i++){
				ans = ans + "OB";
			}
		}
		else ans = "IMPOSSIBLE";
	}
	else if(g > r-1 && g > 0) ans = "IMPOSSIBLE";
	else if(v > y-1 && v > 0) ans = "IMPOSSIBLE";
	else if(o > b-1 && o > 0) ans = "IMPOSSIBLE";
	else{
		string gr = "",vy = "",ob = "";
		if(r > 0){
			gr = "R";
			for(int i = 0;i < g;i++){
				gr = gr + "GR";
			}
			r -= g;
		}
		if(y > 0){
			vy = "Y";
			for(int i = 0;i < v;i++){
				vy = vy + "VY";
			}
			y -= v;
		}
		if(b > 0){
			ob = "B";
			for(int i = 0;i < o;i++){
				ob = ob + "OB";
			}
			b -= o;
		}
		if(r > y+b) ans = "IMPOSSIBLE";
		else if(y > r+b) ans = "IMPOSSIBLE";
		else if(b > y+r) ans = "IMPOSSIBLE";
		else if(r == 0 && y == 0 && b == 0) ans = gr + vy + ob;
		else{
			string sub = "";
			int sur = 0;
			if(r >= y && r >= b){
				sur = y+b-r;
				for(int i = 0;i < sur;i++){
					sub = sub + "RYB";
				}
				y -= sur;
				b -= sur;
				for(int i = 0;i < y;i++){
					sub = sub + "RY";
				}
				for(int i = 0;i < b;i++){
					sub = sub + "RB";
				}
			}
			else if(y >= r && y >= b){
				sur = r+b-y;
				for(int i = 0;i < sur;i++){
					sub = sub + "YRB";
				}
				r -= sur;
				b -= sur;
				for(int i = 0;i < r;i++){
					sub = sub + "YR";
				}
				for(int i = 0;i < b;i++){
					sub = sub + "YB";
				}
			}
			else if(b >= r && b >= y){
				sur = y+r-b;
				for(int i = 0;i < sur;i++){
					sub = sub + "BYR";
				}
				y -= sur;
				r -= sur;
				for(int i = 0;i < y;i++){
					sub = sub + "BY";
				}
				for(int i = 0;i < r;i++){
					sub = sub + "BR";
				}
			}
			for(int i = 0;i < sub.length();i++){
				if(sub[i] == 'R'){
					sub.replace(i,1,gr);
					break;
				}
			}
			for(int i = 0;i < sub.length();i++){
				if(sub[i] == 'Y'){
					sub.replace(i,1,vy);
					break;
				}
			}
			for(int i = 0;i < sub.length();i++){
				if(sub[i] == 'B'){
					sub.replace(i,1,ob);
					break;
				}
			}
			ans = sub;
		}
	}
	ofs << "Case #" << time << ": " << ans << endl;
	//printf("Case #%d: %9f\n",time,d/maxi);
}

int main() {
	int t;
	ifs >> t;
	//cout << "start" << endl;
	for(int i = 1;i <= t;i++){
		solve(i);
	}
	//cout << "fin" << endl;
	return 0;
}
