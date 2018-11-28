#include <cstdlib>
#include <iostream>
#include <cstring>
#include <fstream>
using namespace std;
int T;
int R,C;
char g[30][30];


int main(){
	fstream in;
	fstream out;
	out.open("output.txt",ios::out);
	in.open("input.txt",ios::in);
	in >> T;
	for(int tc = 1; tc <= T; ++tc){
		in >> R >> C;
		for(int i = 0; i < R; ++i)
			for(int j = 0; j < C; ++j){
				in >> g[i][j];
			}
				
		for(int i = 0; i < C; ++i){
				for(int j = 0; j < R; ++j){
					if(g[j][i] != '?'){
						char w = g[j][i];
						int pos = j-1;
						while(pos >= 0 && g[pos][i] == '?'){
							g[pos][i] = w;
							pos--;
						}
						pos = j+1;
						while(pos < R && g[pos][i] == '?'){
							g[pos][i] = w;
							pos++;
						}
						
					}
				}		
		}
		
		for(int i = 0; i < R; ++i){
				for(int j = 0; j < C; ++j){
					if(g[i][j] != '?'){
						char w = g[i][j];
						int pos = j-1;
						while(pos >= 0 && g[i][pos] == '?'){
							g[i][pos] = w;
							pos--;
						}
						pos = j+1;
						while(pos < C && g[i][pos] == '?'){
							g[i][pos] = w;
							pos++;
						}
					}
				}		
		}
		
		
		out << "Case #" << tc << ":" << endl;
		for(int i = 0; i < R; ++i){
			for(int j = 0; j < C; ++j)
				out << g[i][j];
			out << endl;
		}
		
		
	}
	
}
