#include <iostream>
#include <cmath>
#include <string.h>
using namespace std;

int length;
char** m;
int ptr=0;

bool all_face_up(char* s){
	char* temp = s;
	while (*temp != 0){
		if (*temp != '+') {return false;}
		temp++;
	}
	//cout<< "check"<<endl;
	return true;
}

int flip(char* s, int index, int k,int acc){
	int len = (int) strlen(s);
	if (index+k <= len){
		for (int i = index;i <index+k;i++){
			switch(s[i]){
				case '+':
				s[i] = '-';
				break;
				case '-':
				s[i] = '+';
				break;
			}
		}
		acc++;
		return acc;
	} else {
		return -1;
	}

}

int pancake(char* s , int k){
	int acc = 0;
	int len = (int) strlen(s);
	for (int i=0; i< len;i++){
		if (s[i] == '-')
			acc = flip(s,i,k,acc);
		if (acc == -1)
			return -1;
	}
	return acc;
}

int main(){
	int t;
	char b[2];
	char* a = b;
	int k;
	cin >> t;
	for (int i =0;i<t;i++){
		cin >> a >> k;
		int result = pancake(a, k);
		if (result != -1){
			cout <<"Case #" << i+1 << ": " << result;
			cout << endl;
		}
		else {
			string c = "IMPOSSIBLE";
			cout <<"Case #" << i+1 << ": " << c;
			cout << endl;
		}
	}
	return 0;
}


