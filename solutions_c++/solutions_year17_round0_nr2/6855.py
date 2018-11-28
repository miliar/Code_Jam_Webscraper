#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <sstream>
using namespace std;
FILE* Input = fopen("B-large.in","r");
FILE* Output = fopen("B-large.out","w");
bool IsChanged = false;
string cur_num;
template <typename T>
string NumberToString ( T Number ){
	stringstream ss;
	ss << Number;
	return ss.str();
}
unsigned long long StringToNumber(string num){
	char* num_C = new char[num.size()];
	for(int k = 0; k < num.size() ; k++)num_C[k]=num[k];
	return strtoull(num_C,NULL,10);
}
void checker(string msg){
	cout << msg << endl;
}
int ctoi(char c){
	return c - '0';
}
char itoc(int c){
	return c + '0';
}

void downGrade(int idx){
	if(idx == 0)return;

	if(idx > 0){
		int left = ctoi(cur_num[idx-1]);
		int right = ctoi(cur_num[idx]);
		if(left > right){
			IsChanged = true;
			left = left - 1; // it cant be '-1'
			right = 9;
			cur_num[idx-1] = itoc(left);
			cur_num[idx]   = itoc(right);
		}
	

	downGrade(idx-1);
		left = ctoi(cur_num[idx-1]);
		right = ctoi(cur_num[idx]);
		//cout << left << "|" << right << endl;
		if(left > right){
			//cout << "Baaarrr" << endl;
			IsChanged = true;
			left = left + 1; // it cant be '-1'
			right = 9;
			cur_num[idx-1] = itoc(left);
			cur_num[idx]   = itoc(right);
		}
	}
}

int main(){

	int testcase = 1;
	//cin >> testcase;
	//checker("before testcase");
	fscanf(Input,"%d",&testcase);
	//checker("after testcase");
	//cout << testcase << endl;
	
	string* numArr = new string[testcase];
	
	for(int i = 0 ; i < testcase; i++){
		unsigned long long num = 0;
		fscanf(Input,"%llu",&num);
		numArr[i] = NumberToString(num);
	}
	
	for(int i = 0 ; i < testcase; i++){
		cur_num = numArr[i];
		string temp_num = cur_num;
		//cout << cur_num << " -> "; 
		while(true){
			IsChanged = false;
			downGrade(numArr[i].size()-1);
			if(IsChanged == false){
				// no more change
				//cout << "Break!!" << endl;
				break;
			}
			//char* num_C = new char[cur_num.size()];
			//for(int k = 0; k < cur_num.size() ; k++)num_C[k]=cur_num[k];
			//cout << StringToNumber(num_C) << " -> ";
		}
		fprintf(Output,"Case #%d: %llu\n",i+1,StringToNumber(cur_num));
		//cout << StringToNumber(cur_num) << endl;
	}
	fclose(Input);	
	fclose(Output);
	return 0;	
}