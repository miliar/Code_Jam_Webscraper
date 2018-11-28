#include <iostream>
#include <string>
#include <fstream>
#include <sstream>
#include <vector>
#include <stdlib.h>
#include <tuple>
#include <algorithm>
#include <windows.h>
#include<limits>
#include<cstdlib>
#include<algorithm>
#include<functional>
#include<cassert>
#include <map>

std::vector<std::string> split(const std::string &s, char delimiter);
int ctoi(char c);
std::tuple<unsigned long long, unsigned long long> CalcNeighbors(unsigned long long rooms);
void strReplace (std::string& str, const std::string& from, const std::string& to);
void VoidCalcNeighbors(unsigned long long rooms);

	long Ls;
	long Rs;

int main(){
	using namespace std;

	// 変数定義
	long rooms;
	long persons;

	string divide;
	long between;
	string replace;
	long restmax;
	//vector<long> dividevec;
	int array[1000000];
	map<long, int> spacemap;

	//int space;

	std::cout << "QueryPerformanceCounter():\n";
    LARGE_INTEGER freq;
    if( !QueryPerformanceFrequency(&freq) )      // 単位習得
       return 0;
    LARGE_INTEGER start, end;

	if( !QueryPerformanceCounter(&start) );

	///////////////////////////////////////////////

	// 出力準備
	FILE *outputfile;
	outputfile = fopen("bathrooms.txt","w");
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

	for(int i=0; i<itrnum; i++){
		// 同じ処理を連続して行う
		// 初期化
		rooms = 0;
		persons = 0;
		Ls = 0;
		Rs = 0;
		divide.clear();
		replace.clear();
		//dividevec.clear();
		between = 0;
		restmax = 0;
		//space = 0;
		spacemap.clear();

		getline(input, read_line_buffer);
		rooms = stoull(split(read_line_buffer, ' ')[0]);
		persons = stoull(split(read_line_buffer, ' ')[1]);
		//divide = split(read_line_buffer, ' ')[0];
		//between = rooms;


		if(rooms == persons){
			Ls = 0;
			Rs = 0;
		}else{
			restmax = rooms;
			spacemap[rooms] = 1;
			//dividevec.resize(2*persons+1);
			//dividevec[0] = rooms;

			for(int p = 0; p < persons; ++p){
				//std::sort(&dividevec[p], &dividevec[2*p], greater<long>());
				//std::sort(dividevec.begin() + p, dividevec.begin() + 2*p, greater<long>());
				//between = *max_element(&dividevec[p], &dividevec[2*p]);
				//between = dividevec[p];

				for(int sm = restmax; sm; --sm){
					if(spacemap.find(sm) != spacemap.end()){
						between = sm;
						restmax = sm;
						spacemap[sm] = spacemap[sm]-1;
						if(spacemap[sm]==0){
							spacemap.erase(sm);
						}
						break;
					}
				}

				if(between%2 == 0){
					Ls = between / 2 - 1;
					Rs = between / 2;
				}	
				else{
					Ls = (between - 1) / 2;
					Rs = (between-1) / 2;
				}
				
				if( spacemap.find(Ls) != spacemap.end() ) {
				  //  設定されている場合の処理
					spacemap[Ls] = spacemap[Ls] + 1;
				} else {
				  //  設定されていない場合の処理
					spacemap[Ls] = 1;
				}
				if( spacemap.find(Rs) != spacemap.end() ) {
				  //  設定されている場合の処理
					spacemap[Rs] = spacemap[Rs] + 1;
				} else {
				  //  設定されていない場合の処理
					spacemap[Rs] = 1;
				}

				//printf("between : %l");
	
				//printf("%d %d\n\n",i+1, p);
			}
		}

		
		fprintf(outputfile,"Case #%d: %ld %ld\n",i+1, max(Ls, Rs), min(Ls, Rs));
		printf("Case #%d: %ld %ld\n",i+1, max(Ls, Rs), min(Ls, Rs));
		//printf("%d\n",i+1);
	}
	
	fclose(outputfile);
	
	if( !QueryPerformanceCounter(&end) );

	std::cout << "duration = " << (double)(end.QuadPart - start.QuadPart) / freq.QuadPart << "sec.\n";

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

std::tuple<unsigned long long, unsigned long long> CalcNeighbors(unsigned long long rooms){
	unsigned long long Ls;
	unsigned long long Rs;
	if(rooms%2 == 0){
		// even
		// choose rooms / 2 - 1 (from 0)
		Ls = rooms / 2 - 1;
		Rs = rooms / 2;
	}
	else{
		Ls = (rooms - 1) / 2;
		Rs = (rooms-1) / 2;
	}
	return std::forward_as_tuple(Ls, Rs);
}

void VoidCalcNeighbors(unsigned long long rooms){
	if(rooms%2 == 0){
		// even
		// choose rooms / 2 - 1 (from 0)
		Ls = rooms / 2 - 1;
		Rs = rooms / 2;
	}
	else{
		Ls = (rooms - 1) / 2;
		Rs = (rooms-1) / 2;
	}
}

void strReplace (std::string& str, const std::string& from, const std::string& to) {
	str.replace(str.find(from), from.length(), to);
}