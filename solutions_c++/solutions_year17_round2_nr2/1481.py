#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cstdio>
#include <set>
using namespace std;

int main() {
	
	int test;
	cin>>test;
	for (int testc = 1; testc<=test; testc++) {
		int n, r, o, y, b, g, v;
		string s = "";
		scanf("%d %d %d %d %d %d %d", &n, &r, &o, &y, &g, &b, &v);
		set<int> scnt;
		if (r>0) scnt.insert(1);
		if (o>0) scnt.insert(2);
		if (y>0) scnt.insert(3);
		if (g>0) scnt.insert(4);
		if (b>0) scnt.insert(5);
		if (v>0) scnt.insert(6);
		if (scnt.size() == 1) {
			printf("Case #%d: IMPOSSIBLE\n", testc);
			continue;
		}
		if (r > n/2 || o > n/2 || y > n/2 || g > n/2 || b > n/2 || v > n/2) {
				printf("Case #%d: IMPOSSIBLE\n", testc);
				continue;
		}
		if (scnt.size() == 2) {
			
			if (g*o>0 || g*v>0 || o*v>0) {
				printf("Case #%d: IMPOSSIBLE\n", testc);
				continue;
			}
			if (r>0) s += "R";
			if (o>0) s += "O";
			if (y>0) s += "Y";
			if (g>0) s += "G";
			if (b>0) s += "B";
			if (v>0) s += "V";
			string xx = s;
			for (int i = 0; i < n/2 - 1; i++) {
				s += xx;
			}
			printf("Case #%d: %s\n", testc, s.c_str());
			continue;
		}
		if ((o>=b && o>0) || (g>=r && g>0) || (v>=y && v>0)) {
			printf("Case #%d: IMPOSSIBLE\n", testc);
			cout<<r<<" "<<o<<" "<<y<<" "<<g<<" "<<b<<" "<<v<<" "<<endl;
			continue;
		}
		string bob = "";
		string rgr = "";
		string yvy = "";
		for (int i = 0; i < o; i++) {
			bob += "BO";
		}
		bob += "B";
		b -= o;
		
		for (int i = 0; i < g; i++) {
			rgr += "RG";
		}
		rgr += "R";
		r -= g;
		
		for (int i = 0; i < v; i++) {
			yvy += "YV";
		}
		yvy += "Y";
		y -= v;
		
		//cout << "after rgr... b=" << b << " r=" << r << " y= " << y << endl;
		
		int a1, a2, a3;
		
		char c1, c2, c3;
		if (r >= y && r >= b) {
			c1 = 'R'; a1 = r;
			if (y >= b) {
				c2 = 'Y'; a2 = y;
				c3 = 'B'; a3 = b;
			}
			else {
				c2 = 'B'; a2 = b;
				c3 = 'Y'; a3 = y;
			}
		}
		else if (y >= r && y >= b) {
			c1 = 'Y'; a1 = y;
			if (r >= b) {
				c2 = 'R'; a2 = r;
				c3 = 'B'; a3 = b;
			}
			else {
				c2 = 'B'; a2 = b;
				c3 = 'R'; a3 = r;
			}
		}
		else {
			c1 = 'B'; a1 = b;
			if (y >= r) {
				c2 = 'Y'; a2 = y;
				c3 = 'R'; a3 = r;
			}
			else {
				c2 = 'R'; a2 = r;
				c3 = 'Y'; a3 = y;
			}
		}
		s = string(a1+a2+a3, ' ');
		
		for (int i = 0; i < a1; i++) {
			s[2*i] = c1;
		}
		//cout<<s<<endl;
		char cur = c2;
		for (int i = 2*a1 - 1; i < n; i++) {
			s[i] = cur;
			if (cur == c2) {
				cur = c3;
				a2--;
			}
			else {
				cur = c2;
				a3--;
			}
		}
		//cout<<s<<endl;
		//cout<<c2<<" "<<a2<<" "<<c3<<" "<<a3<<endl;
		for (int i = 0; i < a1-1; i++) {
			if (a2 > 0) {
				s[2*i+1] = c2;
				a2--;
			}
			else {
				s[2*i+1] = c3;
			}
		}
		//cout << s << " - " <<endl;
		//cout << "| " << bob << " | " << rgr << " | " << yvy << " |" << endl;
		if (bob.length() > 1) {
			s.replace(s.find("B"), 1, bob);
		}
		if (rgr.length() > 1) {
			s.replace(s.find("R"), 1, rgr);
		}
		if (yvy.length() > 1) {
			s.replace(s.find("Y"), 1, yvy);
		}
		
		printf("Case #%d: %s\n", testc, s.c_str());
	}
	return 0;
}

/*
1
6 2 0 2 0 2 0

*/

