#include <iostream> 
#include <string>
#include <fstream>
#include <vector>
#include <set>
#include <algorithm>
#include <map>

using namespace std;

int N, M;

int main() {
	ifstream fin("in.txt");
	ofstream fout("out.txt");

	int T;
	fin >> T;
	for (int caseNo = 1; caseNo <= T; caseNo++) {
		cout << caseNo << endl;
		fin >> N >> M;
		vector<vector<char>> given(N, vector<char>(N, '.'));
		vector<vector<bool>> rook_game(N, vector<bool>(N, 0));
		vector<vector<bool>> bishop_game(N, vector<bool>(N, 0));
		for (int i = 0; i < M; i++) {
			char c; int R, C;
			fin >> c >> R >> C;
			given[R - 1][C - 1] = c;
			if (c == 'x' || c == 'o') {
				rook_game[R - 1][C - 1] = 1;
			}
			if (c == 'y' || c == 'o') {
				bishop_game[R - 1][C - 1] = 1;
			}
		}

		//solve rook game
		vector<bool> row_taken(N, 0);
		vector<bool> col_taken(N, 0);	
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				if (rook_game[i][j]) {
					row_taken[i]=1;
					col_taken[j]=1;
				}
			}
		}
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				if (!row_taken[i] && !col_taken[j]) {
					rook_game[i][j] = 1;
					row_taken[i] = 1;
					col_taken[j] = 1;
				}
			}
		}
		/*for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				cout << rook_game[i][j];
			}cout << endl;
		}cout << endl;*/

		//solve bishop game (greedy approach)
		vector<bool> sum_taken(2 * N - 1, 0);//sum=0 to 2N-2
		vector<bool> diff_taken(2 * N - 1, 0);//diff=-(N-1) to (N-1), diff+(N-1)=0 to 2N-2
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				if (bishop_game[i][j]) {
					sum_taken[i+j] = 1;
					diff_taken[i-j+N-1] = 1;
				}
			}
		}
		
		for (int d = 0;d<=N/2; d++) {
			for (int i = 0; i < N; i++) {
				for (int j = 0; j < N; j++) {
					if (min(min(min(i, j), N - 1 - i), N - 1 - j) == d) {
						if (!sum_taken[i + j] && !diff_taken[i - j + N - 1]) {
							bishop_game[i][j] = 1;
							sum_taken[i + j] = 1;
							diff_taken[i - j + N - 1] = 1;
						}
					}
				}
			}
		}

		/*for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				cout << bishop_game[i][j];
			}cout << endl;
		}cout << endl;*/

		//now compile to give answer
		string t = "";
		int y = 0;//style points
		int z = 0;//num changes
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				if (given[i][j] == '.') {
					if (rook_game[i][j] && bishop_game[i][j]) {
						t += "o " + to_string(i+1) + " " + to_string(j+1) + "\n";
						y += 2;
						z++;
					}
					if (!rook_game[i][j] && bishop_game[i][j]) {
						t += "+ " + to_string(i + 1) + " " + to_string(j + 1) + "\n";
						y += 1;
						z++;
					}
					if (rook_game[i][j] && !bishop_game[i][j]) {
						t += "x " + to_string(i + 1) + " " + to_string(j + 1) + "\n";
						y += 1;
						z++;
					}
				}
				if (given[i][j] == 'x') {
					if (bishop_game[i][j]) {
						t += "o " + to_string(i + 1) + " " + to_string(j + 1) + "\n";
						y += 2;
						z++;
					}
					else
						y++;
				}
				if (given[i][j] == '+') {
					if (rook_game[i][j]) {
						t += "o " + to_string(i + 1) + " " + to_string(j + 1) + "\n";
						y += 2;
						z++;
					}
					else
						y++;
				}
				if (given[i][j] == 'o') {
					y+=2;
				}
			}
		}

		fout << "Case #" << caseNo << ": " << y << " " << z << endl;
		fout << t;
		//cout << "Case #" << caseNo << ": " << y << " " << z << endl;
		//cout << t;
	}

}