#include <fstream>
#include <string>
#include <iostream>

void run(char** cake,int row, int col, std::ofstream& ofile, int caseNum);

int main(int argc, char*argv[]){
	if(argc < 3){
		std::cerr << "Please specify a file input and output name" << std::endl;
		return 1;
	}

	std::ifstream ifile(argv[1]);
	std::ofstream ofile(argv[2]);

	int numOfTestCases;

	ifile >> numOfTestCases;

	std::string s;

	for(int i = 0; i < numOfTestCases; i++){
		int row;
		int col;

		ifile >> row >> col;

		char** cake = new char*[row];
		for(int i2 = 0; i2 < row; i2++){
			cake[i2] = new char[col];
			ifile >> cake[i2];
		}

		run(cake,row,col,ofile,i+1);
	}

	ifile.close();
	ofile.close();
	return 0;
}

void run(char** cake,int row, int col, std::ofstream& ofile, int caseNum){
	ofile << "Case #" << caseNum << ": " << std::endl;
	//**********************************
	//Code Here
	for(int i = 0; i < row; i++){
		for(int i2 = 0; i2 < col; i2++){
			if(cake[i][i2] != '?'){
				for(int i3 = i2 + 1; (i3 < col) && cake[i][i3] == '?'; i3++){
					cake[i][i3] = cake[i][i2];
				}
			}
		}
	}
	for(int i = row - 1; i >= 0; i--){
		for(int i2 = col - 1; i2 >= 0; i2--){
			if(cake[i][i2] != '?'){
				for(int i3 = i2 - 1; (i3 >= 0) && cake[i][i3] == '?'; i3--){
					cake[i][i3] = cake[i][i2];
				}
			}
		}
	}
	for(int i = 0; i < row; i++){
		for(int i2 = 0; i2 < col; i2++){
			if(cake[i][i2] != '?'){
				for(int i3 = i + 1; (i3 < row) && cake[i3][i2] == '?'; i3++){
					cake[i3][i2] = cake[i][i2];
				}
			}
		}
	}
	for(int i = row - 1; i >= 0; i--){
		for(int i2 = col - 1; i2 >= 0; i2--){
			if(cake[i][i2] != '?'){
				for(int i3 = i - 1; (i3 >= 0) && cake[i3][i2] == '?'; i3--){
					cake[i3][i2] = cake[i][i2];
				}
			}
		}
	}



	//**********************************
	for(int i = 0; i < row; i++){
		for(int i2 = 0; i2 < col; i2++){
			ofile << cake[i][i2];
		}
		ofile << std::endl;
	}
	for(int i = 0; i < row; i++){
		delete cake[i];
	}
	delete cake;
	return;
}







































