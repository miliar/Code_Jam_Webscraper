#include <iostream>
#include <vector>
#include <fstream>


using namespace std;


int detect_left(vector<vector<char> > & matrix, int x, int y){
	int left = y;
	if (left == 0)
		return 0;
	while (matrix[x][left] == matrix[x][y] || matrix[x][left] == '?'){
		if (left == 0)
			return 0;
		left--;
	}
	return left+1;
}

int detect_right(vector<vector<char > > & matrix, int x, int y){
	int right = y;
	if (right >= matrix[0].size()-1)
		return matrix[0].size()-1;
	while (matrix[x][right] == matrix[x][y] || matrix[x][right] == '?'){
		if (right >= matrix[0].size()-1)
			return matrix[0].size()-1;
		right++;
	}
	return right-1;
}

bool detect_empty(vector<char> & row){
	for (auto chr : row){
		if (chr != '?')
			return false;
	}
	return true;
}

int detect_down(vector<vector<char > > & matrix, int x, int y){
	int down = x + 1;

	if (down > matrix.size()-1){
		return matrix.size()-1;
	}

	if (down == matrix.size()-1){
		if (!detect_empty(matrix[down])){
			return x;
		}
		else {
			return matrix.size()-1;
		}
	}

	if (!detect_empty(matrix[down])){
		return x;
	}
	while (detect_empty(matrix[down])){
		down ++;
		if (down >= matrix.size()-1){
			if (detect_empty(matrix[down]))
				return matrix.size()-1;
			else 
				return down-1;
		}
	}
	return down-1;
}

int detect_up(vector<vector<char > > & matrix, int x, int y){
	int up = x -1;

	if (up <0){
		return 0;
	}

	if (up == 0){
		if (!detect_empty(matrix[up])){
			return x;
		}
		else {
			return 0;
		}
	}

	if (!detect_empty(matrix[up])){
		return x;
	}
	while (detect_empty(matrix[up])){
		up --;
		if (up <= 0){
			if (detect_empty(matrix[up]))
				return 0;
			else 
				return up +1;
		}
	}
	return up+1;
}

void fill(vector<vector<char > > & matrix, vector<vector<char > > & ret, int x, int y){
	int left = detect_left(matrix, x, y);
	int right = detect_right(matrix, x, y);
	int up = detect_up(matrix,x,y);
	int down = detect_down(matrix, x, y);

	for (int i=up; i<=down; i++){
		for (int j=left; j<=right; j++){
			ret[i][j] = matrix[x][y];
		}
	}
} 


vector<vector<char> > fill_matrix(vector<vector<char> > & matrix){
	vector<vector<char> > ret;
	for (auto row: matrix){
		vector<char> the_row;
		for (auto chr: row){
			the_row.push_back('?');
		}
		ret.push_back(the_row);
	}


	for (int i=0; i<matrix.size(); i++){
		for (int j=0; j<matrix[i].size(); j++){
			if (matrix[i][j] != '?'){
				fill(matrix, ret, i, j);
			}
		}
	}

	return ret;
}

void print_matrix(vector<vector<char> > & matrix){
	for (auto row : matrix){
		for (auto chr : row){
			cout<<chr;
		}
		cout<<endl;
	}
	cout<<endl;
}

void out_matrix(vector<vector<char> > & matrix, ofstream & outfile){
	for (auto row : matrix){
		for (auto chr : row){
			outfile<<chr;
		}
		outfile<<endl;
	}
}



int main(){

	// vector<vector<char> > matrix;
	// vector<char> one;
	// one.push_back('G');
	// one.push_back('?');
	// one.push_back('?');
	// vector<char> two;
	// two.push_back('?');
	// two.push_back('C');
	// two.push_back('?');
	// vector<char> three;
	// three.push_back('?');
	// three.push_back('?');
	// three.push_back('J');
	// matrix.push_back(one);
	// matrix.push_back(two);
	// matrix.push_back(three);

	// cout<<(detect_left(matrix, 1,1))<<endl;
	// cout<<(detect_right(matrix, 1,1))<<endl;
	// cout<<(detect_down(matrix,1,1))<<endl;

	// fill_matrix(matrix);
	// print_matrix(matrix);

	ifstream infile;
	infile.open("A-small-attempt2.in");

	int numLines;
	infile>>numLines;

	ofstream outfile;
	outfile.open("A-small-attempt2.out");

	for (int i=0; i<numLines; i++){
		int row;
		int col;
		infile>>row;
		infile>>col;
		vector<vector<char> > matrix;
		for (int a = 0; a<row; a++){
			vector<char> row;
			for (int b=0; b<col; b++){
				char temp;
				infile>>temp;
				if (temp != '\n')
					row.push_back(temp);

			}
			matrix.push_back(row);
		}
		auto ret = fill_matrix(matrix);
		print_matrix(ret);
		outfile<<"Case #"<<(i+1)<<":"<<endl;

		out_matrix(ret, outfile);
	}

	infile.close();
	outfile.close();


	return 0;
}