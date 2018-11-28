#include <iostream>
#include <string>
#include <fstream>
#include <sstream>
#include <vector>

std::vector<std::string> split(const std::string &s, char delimiter);
void FlipPancake(std::string& pancakestate, int flipstart, int flipnum);

int main(){
	using namespace std;

	// 変数定義
	std::vector<std::string> datavec_str;
	string state;
	int flipsize;
	string goal;
	int count;
	int currentminus;

	///////////////////////////////////////////////

	// 出力準備
	FILE *outputfile;
	outputfile = fopen("flipper.txt","w");
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
		datavec_str.clear();
		state.clear();
		flipsize = 0;
		read_line_buffer.clear();
		goal.clear();
		count = 0;
		currentminus = 0;

		getline(input, read_line_buffer);
		datavec_str = split(read_line_buffer, ' ');
		state = datavec_str[0];
		flipsize = stoi(datavec_str[1]);		
		for(int addnum =0; addnum<state.size(); addnum++){
			goal.push_back('+');
		}

		printf("Case #%d: state :( %s ), flipsizes : %d, GOAL : ( %s )\n", i+1, state.c_str(), flipsize, goal.c_str());
		
		while(1){
		//printf("check state : %s\n", state.c_str());
			if(state == goal){
				printf("FLIP FINISHED.\n");
				break;
			}
			else{
				for(int s=0; s<state.size(); s++){
					if(state[s]=='+'){
						if(s == state.size() - 1){
							currentminus = state.size();
						}
						//OK.
					}
					else{
						//NG.
						currentminus = s;
						//printf("check currentminus : %d\n", currentminus);
						break;
					}
				}
				//printf("check %d\n", currentminus);
				if(currentminus > state.size() - flipsize){
					// OUT
					count = -1;
					break;
				}
				else{
					// FLIP
					//printf("[bef]check state: %s\n", state.c_str());
					FlipPancake(state, currentminus, flipsize);
					//printf("[aft]check state: %s\n\n", state.c_str());
					//printf("FLIP DONE, %d\n", count);
					count++;
				}
			}
		}
		
		if(count >= 0){
			fprintf(outputfile,"Case #%d: %d\n", i+1, count);	
		}
		else{
			fprintf(outputfile,"Case #%d: %s\n", i+1, "IMPOSSIBLE");
		}

	}
	
	fclose(outputfile);
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

void FlipPancake(std::string& pancakestate, int flipstart, int flipnum){
	for(int flipitr=0; flipitr<flipnum; flipitr++){
		if(pancakestate[flipstart+flipitr] == '+'){
			//printf("check flip + to -  %d / %d \n",flipitr+1, flipnum);
			//printf("[bef]check state: %s\n", pancakestate.c_str());
			pancakestate[flipstart+flipitr] = '-';
			//printf("[aft]check state: %s\n\n", pancakestate.c_str());
		}
		else if(pancakestate[flipstart+flipitr] == '-'){
			//printf("check flip - to +  %d / %d \n",flipitr+1, flipnum);
			//printf("[bef]check state: %s\n", pancakestate.c_str());
			pancakestate[flipstart+flipitr] = '+';
			//printf("[aft]check state: %s\n\n", pancakestate.c_str());
		}
		else{
			printf("ERROR: invalid input. (FlipPancake)\n");
		}
	}
}