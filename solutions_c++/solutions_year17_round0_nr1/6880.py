#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <string>
#define H '+'
#define B '-'
using namespace std;
FILE* Input = fopen("A-large.in","r");
FILE* Output = fopen("A-large.out","w");
void checker(string msg){
	cout << msg << endl;
}
char flip(char c){if(c == H){return B;}else{return H;}}

int solve(string cake,int size){
	bool finish = false;
	int idx = 0;
	int flipCount = 0;
	while(!finish){
		if(cake[idx]==B){
			if(idx + size > cake.size()){
				return -1;
			}else{
				// Pan Cake Flip
				flipCount++;
				for(int i = 0 ; i < size;i++){
					cake[i+idx] = flip(cake[i+idx]);
				}	
			}
		}
		idx++;
		if(idx == cake.size()){
			finish = true;
		}
	}

	//cout << "Cake : " << cake << " and Count : " << flipCount << endl;
	return flipCount;
}
int main(){

	int testcase = 0;
	//cin >> testcase;
	//checker("before testcase");
	fscanf(Input,"%d",&testcase);
	//checker("after testcase");
	//cout << testcase << endl;
	int* sizeArr = new int[testcase];
	string* cakeArr = new string[testcase];
	for(int i = 0 ; i < testcase; i++){
		//cin >> cakeArr[i] >> sizeArr[i];
		char cake[1000];
		fscanf(Input,"%s %d",cake,&sizeArr[i]);
		cakeArr[i] = cake;
		//cout << i << endl;
	}
	//for(int i = 0 ; i < testcase; i++){
	//	cout << cakeArr[i] <<" " << sizeArr[i] << endl;
	//}
	for(int i = 0 ; i < testcase; i++){
		//checker("before solve");
		int result = solve(cakeArr[i],sizeArr[i]);
		//checker("after solve");
		if(result >= 0){
			//cout << "Case #" << i+1 << ": " << result << endl;
			fprintf(Output,"Case #%d: %d\n",i+1,result);
		}else{
			//cout << "Case #" << i+1 << ": IMPOSSIBLE" << endl;
			fprintf(Output,"Case #%d: IMPOSSIBLE\n",i+1);
		}
	}
	fclose(Input);	
	fclose(Output);
	return 0;	
}