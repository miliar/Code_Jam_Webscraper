#include <iostream>
#include <stdio.h>
#include <queue>
#include <string.h>
#include <fstream>

using namespace std;

int n;
string arr;
bool possible;

void makeWord(string s, int r, int y, int b){
	//cout << s.size() << " " << s << endl;
	if( s.size() == n ){
		if( s[0] != s[s.size() -1]){
			arr = s;
			possible = true;	
		}
		return;
	}

	if( s.size() == 0 ){
		if( r > 0 && !possible ) makeWord(s+'R', r-1, y, b);
		if( y > 0 && !possible ) makeWord(s+'Y', r, y-1, b);
		if( b > 0 && !possible ) makeWord(s+'B', r, y, b-1);

		return;
	}

	char l;
	l = s[s.size() - 1];

	if( l == 'R' && !possible ){
		if( y > b && y > 0 && !possible ) makeWord(s+'Y', r, y-1, b);
		else if( b > 0 && !possible) makeWord(s+'B', r, y, b-1);
	}else if( l == 'Y' && !possible ){
		if( b > r && b > 0  && !possible ) makeWord(s+'B', r, y, b-1);
		else if( r > 0 && !possible) makeWord(s+'R', r-1, y, b);
	}else if( l == 'B' && !possible ){
		if( r > y && r > 0 && !possible) makeWord(s+'R', r-1, y, b);
		else if( y > 0 && !possible) makeWord(s+'Y', r, y-1, b);
	}
}

int main() {
	ios_base::sync_with_stdio(false);cin.tie(NULL);

    ifstream cin("bs3.in");
    ofstream cout("b.out");

	int TC, t, r, o, y, g, b, v;
	string s;

	cin >> TC;
	t = 1;

	
	while( t <= TC ){
		
		cin >> n >> r >> o >> y >> g >> b >> v;

		arr = "";
		possible = false;

		cout << "Case #" << t << ": ";
		if( y + b >= r && b + r >= y && y + r >= b ){
			possible = false;
			makeWord("", r, y, b);
			cout << arr << "\n";
		}else{
			cout << "IMPOSSIBLE\n";
		}

		
		t++;
	}
	
	return 0;
}