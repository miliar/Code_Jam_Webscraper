#include <iostream>
#include <string>
#include <iomanip>
#include <algorithm>

using namespace std;

void qwe(string &q, int p, string c){
	string a, b;
	string tmp = "";
	tmp += c;
	a = q.substr(0, p);
	b = q.substr(p, q.length() - p);
	q = a + tmp + b;
}

int main(){
	int T;
	cin >> T;
	for (int K = 1; K <= T; K++){
		int n, r, o, y, g, b, v;
		cin >> n >> r >> o >> y >> g >> b >> v;
		
		r -= g;
		b -= o;
		y -= v;
		
		if (r < 0 || b < 0 || y < 0){
			cout << "Case #" << K << ": ";
			cout << "IMPOSSIBLE" << endl;
			continue;
		}
		
		if (r == 0 && g){
			if (o || y || b || v){
				cout << "Case #" << K << ": ";
				cout << "IMPOSSIBLE" << endl;
				continue;
			}
			cout << "Case #" << K << ": ";
			for (int i = 0; i < g; i++) cout << "GR";
			cout << endl;
			continue;
		}
		if (b == 0 && o){
			if (r || y || g || v){
				cout << "Case #" << K << ": ";
				cout << "IMPOSSIBLE" << endl;
				continue;
			}
			cout << "Case #" << K << ": ";
			for (int i = 0; i < o; i++) cout << "OB";
			cout << endl;
			continue;
		}
		if (y == 0 && v){
			if (r || o || g || b){
				cout << "Case #" << K << ": ";
				cout << "IMPOSSIBLE" << endl;
				continue;
			}
			cout << "Case #" << K << ": ";
			for (int i = 0; i < v; i++) cout << "VY";
			cout << endl;
			continue;
		}
		
		string q[1005];
		for (int i = 0; i < 1005; i++) q[i] = "";
		char p[3];
		int pp[3];
		if (r >= y && r >= b){
			p[0] = 'R';
			pp[0] = r;
			if (y >= b){
				p[1] = 'Y';
				pp[1] = y;
				p[2] = 'B';
				pp[2] = b;
			} else {
				p[2] = 'Y';
				pp[2] = y;
				p[1] = 'B';
				pp[1] = b;
			}
		} else if (y >= r && y >= b){
			p[0] = 'Y';
			pp[0] = y;
			if (r <= b){
				p[1] = 'R';
				pp[1] = r;
				p[2] = 'B';
				pp[2] = b;
			} else {
				p[2] = 'R';
				pp[2] = r;
				p[1] = 'B';
				pp[1] = b;
			}
		} else {
			p[0] = 'B';
			pp[0] = b;
			if (r >= y){
				p[1] = 'R';
				pp[1] = r;
				p[2] = 'Y';
				pp[2] = y;
			} else {
				p[2] = 'R';
				pp[2] = r;
				p[1] = 'Y';
				pp[1] = y;
			}
		}
		if (pp[1] + pp[2] < pp[0]){
			cout << "Case #" << K << ": ";
			cout << "IMPOSSIBLE" << endl;
			continue;
		}
		for (int i = 0; i < pp[0]; i++) q[i] = p[0];
		for (int i = 0; i < pp[1]; i++) q[i] += p[1];
		for (int i = 0; i < pp[2]; i++) q[pp[0] - 1 - i] += p[2];
		
		string ans = "";
		for (int i = 0; i < pp[0]; i++) ans += q[i];
		
		int pos = ans.find('R');
		if (g && pos != string::npos){
			string tmp = "";
			for (int i = 0; i < g; i++) tmp += "RG";
			qwe(ans, pos, tmp);
		}
		pos = ans.find('B');
		if (o && pos != string::npos){
			string tmp = "";
			for (int i = 0; i < o; i++) tmp += "BO";
			qwe(ans, pos, tmp);
		}
		pos = ans.find('Y');
		if (v && pos != string::npos){
			string tmp = "";
			for (int i = 0; i < v; i++) tmp += "YV";
			qwe(ans, pos, tmp);
		}
		
		cout << "Case #" << K << ": ";
		cout << ans;
		cout << endl;
	}
	
	return 0;
}
