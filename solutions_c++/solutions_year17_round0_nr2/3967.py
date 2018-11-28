#include <iostream>
#include <string>
#include <fstream>
#include <sstream>
#include <vector>
#include <stdlib.h>

std::vector<std::string> split(const std::string &s, char delimiter);
int ctoi(char c);

int main(){
	using namespace std;

	// 変数定義
	//unsigned long long num;
	int letternum;
	vector<int> numvec;
	int tempnum;
	int count;

	///////////////////////////////////////////////

	// 出力準備
	FILE *outputfile;
	outputfile = fopen("tidy.txt","w");
	if(outputfile==NULL){
		exit(1);
	}

	// 入力開始
	string Inputname = "Input.txt";
	ifstream input;
	input.open(Inputname,ios::in);
	string read_line_buffer;

	// 最初の行の数字を読む（処理回数）
	getline(input, read_line_buffer);
	int itrnum = stoi(read_line_buffer);

	printf("check itrnum : %d\n\n",itrnum);

	for(int i=0; i<itrnum; i++){
		// 同じ処理を連続して行う

		// 初期化
		//num = 0;
		letternum = 0;
		numvec.clear();
		tempnum = 0;
		count = 0;

		getline(input, read_line_buffer);
		//num = stoull(read_line_buffer);
		letternum = read_line_buffer.size();

		printf("start.\n\n");
		//cout << read_line_buffer << endl;

		//printf("Case #%d: num : (%llo)\n", i+1, num);

		for(int j = 0; j < letternum; j++){
			numvec.push_back(ctoi(read_line_buffer[j]));
		}


		for(int j = 1; j < letternum; j++){
			if(numvec[j] < numvec[j-1]){
				// big small
				numvec[j-1] = numvec[j-1] - 1;
				for(int rest = j; rest < letternum; rest++){
					numvec[rest] = 9;
				}
				if(j == 1){
					j = j - 1;
				}
				else{
					j = j - 2;
				}
			}
			
		}

		
		
		
		while(numvec[count] == 0){
			count++;
		}

//		for(int k=count; k<letternum; k++){
//			cout << numvec[k];
//			//printf("aaa");
//		}
//		cout << endl;

		fprintf(outputfile,"Case #%d: ",i+1);
		for(int k=count; k<letternum; k++){
			fprintf(outputfile,"%d",numvec[k]);
		}
		fprintf(outputfile,"\n");


	}
	
	//fclose(outputfile);
	return 0;

}

// split strings to vec<str>
std::vector<std::string> split(const std::string &s, char delimiter){
	std::istringstream stream(s);
	std::string field;
	std::vector<std::string> result;
	while(std::getline(stream, field, delimiter)){
		result.push_back(field);
	}
	return result;
}


int ctoi(char c){
    switch(c){
        case '0': return 0;
        case '1': return 1;
        case '2': return 2;
        case '3': return 3;
        case '4': return 4;
        case '5': return 5;
        case '6': return 6;
        case '7': return 7;
        case '8': return 8;
        case '9': return 9;
        default : return -1;
    }
}