#include <iostream>
#include <fstream>
#include <vector>
#include <string>
using namespace std;

void check(vector< vector<char> >& matrix, int i, int j) {
	if(matrix[i][j] != 'n') return;
	int n = matrix.size()-1;
	bool flag1 = true, flag2 = true;
	for(int k=1; k<=n; k++) {
		if(k != j && (matrix[i][k] == 'o' || matrix[i][k] == 'x')) {
			flag1 = false;
			break;
		}
		if(k != i && (matrix[k][j] == 'o' || matrix[k][j] == 'x')) {
			flag1 = false;
			break;
		}		
	}
	for(int a=1; a<=n; a++) {
		if(a != i) {
			int b = a + j - i;
			if(b>=1 && b<=n && (matrix[a][b] == 'o' || matrix[a][b] == '+')) {
				flag2 = false;
				break;
			}
		} 
	}
	if(flag2) {
		for(int a=1; a<=n; a++) {
			if(a != i) {
				int b = i + j - a;
				if(b>=1 && b<=n && (matrix[a][b] == 'o' || matrix[a][b] == '+')) {
					flag2 = false;
					break;
				}
			} 
		}
	}	
	if(flag2) {
		matrix[i][j] = '+';
		return;		
	}	
	if(flag1) {
		matrix[i][j] = 'x';
		return;		
	}												
}

void check2(vector< vector<char> >& matrix, int i, int j) {
	if(matrix[i][j] == 'o') {
		return;
	}	
	int n = matrix.size()-1;
	bool flag1 = true, flag2 = true;
	for(int k=1; k<=n; k++) {
		if(k != j && (matrix[i][k] == 'o' || matrix[i][k] == 'x')) {
			flag1 = false;
			break;
		}
		if(k != i && (matrix[k][j] == 'o' || matrix[k][j] == 'x')) {
			flag1 = false;
			break;
		}		
	}
	for(int a=1; a<=n; a++) {
		if(a != i) {
			int b = a + j - i;
			if(b>=1 && b<=n && (matrix[a][b] == 'o' || matrix[a][b] == '+')) {
				flag2 = false;
				break;
			}
		} 
	}
	if(flag2) {
		for(int a=1; a<=n; a++) {
			if(a != i) {
				int b = i + j - a;
				if(b>=1 && b<=n && (matrix[a][b] == 'o' || matrix[a][b] == '+')) {
					flag2 = false;
					break;
				}
			} 
		}
	}	
	if(flag1 && flag2) {
		matrix[i][j] = 'o';
		return;		
	}			
}

int main() {
	ifstream file("D-small-attempt4.in");
	ofstream out("output.txt");
	int N;
	file >> N;
	for(int a=0; a<N; a++) {
		int n, L;
		file >> n >> L;
		vector< vector<char> > matrix(n+1 ,vector<char>(n+1, 'n'));
		int point = 0;
		vector<string> records;	
		for(int b=0; b<L; b++) {
			int i, j;
			char m;
			file >> m >> i >> j;
			matrix[i][j] = m;
		}
		vector< vector<char> > original = matrix;
		/*
		for(int i=2; i<=n; i++) {
			for(int j=1; j<=n; j++) {
				check(matrix, i, j);
			}
		}
		for(int i=2; i<=n; i++) {
			for(int j=1; j<=n; j++) {
				check2(matrix, i, j);
			}
		}	
		*/
		for(int k=1; k<=(n*n+1)/2; k++) {
			int i = (k-1)%n + 1;
			int j = (k-1)/n + 1;
			check(matrix, i, j);
			i = (n*n - k)%n + 1;
			j = (n*n - k)/n + 1;			
			check(matrix, i, j);			
		}	

		for(int k=1; k<=(n*n+1)/2; k++) {
			int i = (k-1)%n + 1;
			int j = (k-1)/n + 1;
			check2(matrix, i, j);
			i = (n*n - k)%n + 1;
			j = (n*n - k)/n + 1;			
			check2(matrix, i, j);			
		}			

		for(int i=1; i<=n; i++) {
			for(int j=1; j<=n; j++) {
				if(matrix[i][j] == 'o') {
					point += 2;
				}
				else if(matrix[i][j] == 'x' || matrix[i][j] == '+') {
					point++;
				}
				if(matrix[i][j] != original[i][j]) {
					string str(1, matrix[i][j]);
					str += " " + to_string(i) + " " + to_string(j);
					records.push_back(str);
				}
			}
		}			
		out << "Case #" << a+1 << ": " << point << " " << records.size() << endl;
		for(int i=0; i<records.size(); i++) {
			out << records[i] << endl;
		}
	}
}