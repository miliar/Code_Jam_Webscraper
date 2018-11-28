#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <sstream>
using namespace std;

string int_to_str(int num)
{
    stringstream ss;

    ss << num;

    return ss.str();
}

int main(){

	int T;
	ifstream fin("D-large.in");
	ofstream fout("D-large.out");
	fin >> T;

	for(int t = 0; t < T ; t++){
		
		int N, K;
		fin >> N >> K; 

		vector< vector<int> > cross(N), crossInit(N);
		vector< vector<int> > plus(N), plusInit(N);

		for(int i = 0; i < N; i++){
			for(int j = 0; j < N; j++){
				plus[i].push_back(0);
				plusInit[i].push_back(0);
				cross[i].push_back(0);
				crossInit[i].push_back(0);
			}
		}
		

		vector<int> vert(N, 0), hor(N, 0);
		vector<int> diag(2*N-1, 0);
		vector<int> diag2(2*N-1, 0);

		for(int i = 0; i < K; i++){

			int row, col;
			char s;
			fin >> s;
			fin >> row >>col;
			row--; col--;

			if(s == '+' || s == 'o'){
				plus[row][col] = 1;
				plusInit[row][col] = 1;
				diag[row+col] = 1;
				diag2[N-1-(row-col)] = 1;
			}

			if(s == 'x' || s == 'o'){
				cross[row][col] = 1;
				crossInit[row][col] = 1;
				vert[row] = 1;
				hor[col] = 1;
			}
		}
//for(int gh = 0; gh < N; gh++) cout <<t <<": "<< vert[gh] <<endl;
		int j = 0;
		for(int i=0; i < N; i++){

			if(hor[i] == 1) continue;
			while(j < N){
				if(vert[j] == 0) break;
				j++;
			}
			if(j == N) break;
			cross[j][i] = 1;
			vert[j] = 1;
		}


		j=0;
		for(int i = 0; i < N; i++){

			if(diag[i] == 0){
				//first valid empty space in diag2
				int r=0, c=i;
				while(c != -1){
					if(diag2[N-1-(r-c)] == 0){

						plus[r][c] = 1;
						diag[r+c] = 1;
						diag2[N-1-(r-c)] =1;
						break;
					}
					r++;c--;
				}
			}
			if(diag[2*N-2-i] == 0){
				//first valid empty space in diag2
				int r=N-1, c=N-1-i;
				while(c != N){
					if(diag2[N-1-(r-c)] == 0){

						plus[r][c] = 1;
						diag[r+c] = 1;
						diag2[N-1-(r-c)] =1;
						break;
					}
					r--;c++;
				}

			}
		}

		int style = 0, statements = 0;
		string sout = "";
		for(int a = 0; a <  N; a++){
			for(int b = 0; b < N; b++){
				style += plus[a][b];
				style += cross[a][b];
				
				int r = a+1, c = b+1;
				if(plus[a][b] == plusInit[a][b] && cross[a][b] == crossInit[a][b]) continue;
				if(plus[a][b] == 1 && cross[a][b] == 1) {
					sout += "o " + int_to_str(r) +" " + int_to_str(c) + "\n";
					statements++;
				}

				else if(plus[a][b] == 1) {
					sout += "+ " + int_to_str(r) +" " + int_to_str(c) + "\n";
					statements++;
				}

				else if(cross[a][b] == 1) {
					sout += "x " + int_to_str(r) +" " + int_to_str(c) + "\n";
					statements++;
				}
			}

		}
		fout << "Case #" << t+1 << ": " << style << " " << statements << endl;
		fout << sout;

	}

	fin.close();
	fout.close();

	return 0;
}
