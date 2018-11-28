#include <cstdlib>
#include <iostream>
#include <cstring>
#include <algorithm>
#include <fstream>
using namespace std;
int T;
int N,R,O,Y,G,B,V;
char color[3];
int q[3];
int o[3];
bool mycompare(int x, int y){
	return q[x] > q[y];
}
int main(){
	fstream in;
	fstream out;
	out.open("output.txt",ios::out);
	in.open("input.txt",ios::in);
	in >> T;
	int N;
	color[0] = 'R';
	color[1] = 'Y';
	color[2] = 'B';

	for(int tc = 1; tc <= T; ++tc){
		in >> N >> R >> O >> Y >> G >> B >> V;
		q[0] = R;
		q[1] = Y;
		q[2] = B;
		for(int i = 0; i < 3; ++i)
			o[i] = i;
		sort(o,o+3,mycompare);
		int x = o[0];
		int y = o[1];
		int z = o[2];
		if( q[x] > q[y] + q[z] ){
			out << "Case #" << tc << ": IMPOSSIBLE" << endl;
		}else{
			string ans = "";
			for(int i = 0; i < q[x]; ++i){
				ans+= color[x];
				if( i < q[y] ) ans+= color[y];
				if(q[x] -1 - i < q[z]) ans+=color[z];
			}
			out << "Case #" << tc << ": " << ans << endl;
		}
	}
	
}
