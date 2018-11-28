#include <iostream>
#include <algorithm>
#include <cmath>
#include <vector>
#include <string>
#include <cstdio>
#include <map>
#include <cstdlib>
#include <cstring>
#include <fstream>
#include <set>

#define FOR(i,a,b) for(int (i)=(a);(i)<(b);++(i))
#define FORC(it,cont) for(__typeof(cont.begin()) it=(cont).begin(); it!=(cont).end();++(it))
#define VI vector<int>
#define VS vector<string>
#define pb push_back

using namespace std;

VI colors;

string construct(int r, int y, int b) {
	if (r + y + b == 0 ) return "";
	string sol = "";
	if ( r >= y && r >= b ) {
		while(r) {
			if( y + b > r) { sol += "RYB"; --r; --y; --b; }
			else if ( y > 0 ) { sol += "RY"; --r; --y; }
			else if ( b > 0 ) { sol += "RB"; --r; --b; }
		}
		return sol;		
	}
	else if ( y >= r && y >= b ) {
		while(y) {
			if( r + b > y) { sol += "YRB"; --r; --y; --b; }
			else if ( r > 0 ) { sol += "YR"; --r; --y; }
			else if ( b > 0 ) { sol += "YB"; --y; --b; }
		}
		return sol;		
	}
	else {
		while(b) {
			if( y + r > b) { sol += "BRY"; --r; --y; --b; }
			else if ( y > 0 ) { sol += "BY"; --b; --y; }
			else if ( r > 0 ) { sol += "BR"; --r; --b; }
		}
		return sol;		
	}
	return sol;
}

string add(string s, int o, int g, int v) {
	//cout << s << " " << o << " " <<  g << " " << v << endl;
	if( o > 0 ) {
		int pos = s.find('B');
		string tmp;
		while( o > 0 ) { tmp += "BO"; --o; }
		s = s.substr(0,pos) + tmp + s.substr(pos);
	}
	
	if( g > 0 ) {
		int pos = s.find('R');
		string tmp;
		while( g > 0 ) { tmp += "RG"; --g; }
		s = s.substr(0,pos) + tmp + s.substr(pos);
	}
	
	if( v > 0 ) {
		int pos = s.find('Y');
		string tmp;
		while( v > 0 ) { tmp += "YV"; --v; }
		s = s.substr(0,pos) + tmp + s.substr(pos);
	}
	return s;
}

string construct2(int o, int g, int v) {
	string sol;
	while( o > 0 ) { sol += "BO"; -- o;} 
	while( g > 0 ) { sol += "RG"; --g; }
	while( v > 0 ) { sol += "YV"; --v; }
	return sol;
}

int main()
	{
	int T,N;
	//ifstream fcin("in.txt",ios::in);
	//ifstream fcin("B-small-attempt1.in",ios::in);
	ifstream fcin("B-large.in",ios::in);
	FILE* fout;
	fout = fopen("out.txt","w");
	fcin >> T;
	FOR(tc,0,T)
		{
		int res = 0;
		
		fcin >> N;
		colors.clear();
		colors.resize(6);
		FOR(i,0,6) fcin >> colors[i];
		
		VI tmp = colors;
		bool ok = 1;
		int usedup = 0; 
		
		for(int i=1;i < 6; i+=2)
			if(tmp[i] > 0) {
				tmp[(i+3)%6] -= tmp[i];
				tmp[i] = 0;
				if(tmp[(i+3)%6]==0) ++usedup;
			}
			
		FOR(i,0,6) if(tmp[i]<0) ok = 0;
		//cout << tc << " " << usedup << endl;
		if( usedup > 1 ) ok = 0;
		FOR(i,0,6) if( usedup == 1 && tmp[i] > 0 ) ok = 0;
		int sum = 0;
		int mx = 0;
		FOR(i,0,6) { sum += tmp[i]; mx = max(mx,tmp[i]); }
		if( mx > sum - mx )  ok = 0;
		
		
		if( ok ) {
			fprintf(fout,"Case #%d: ",tc+1);
			int r = tmp[0];
			int y = tmp[2];
			int b = tmp[4];
			string s = construct(r,y,b);
			int o = colors[1];
			int g = colors[3];
			int v = colors[5];
			if( usedup == 0 ) s = add(s,o,g,v);
			else s = construct2(o,g,v);
			fprintf(fout,"%s\n",s.c_str());
		}	
		else
			fprintf(fout,"Case #%d: IMPOSSIBLE\n",tc+1);
		}
	fcin.close();
	return 0;
	}
