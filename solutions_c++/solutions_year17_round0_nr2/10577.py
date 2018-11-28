#include <iostream>
#include <cstring>
#include <cmath>
#include <array>
using namespace std;
int tmp [100];
char ii[100];
int tstcases, tmpnum;
void convertintarr(){
    int tmpnum1 = tmpnum;
	for (int i = strlen(ii)- 1; i >= 0; i--) {
        tmp[i] = tmpnum1 % 10;
        tmpnum1 /= 10;
    }
}
void convertarrint(){
	for(int i=0;i<strlen(ii);i++){
		tmpnum += tmp[i] * pow(10,(strlen(ii)- i- 1));
	}
}
void subtract(){
    --tmpnum;
    convertintarr();
}
void translate(){
	for(int i=0;i<strlen(ii);i++){
		tmp[i] = ii[i]-'0';
	}
}
bool check(){
	for(int i=0;i<(strlen(ii)-1);i++){
		if(tmp[i]>tmp[i + 1]){
			return false;
		}
	}
	return true;
}
int main(){
	cin >> tstcases;
	for(int i=0;i<tstcases;i++){
		cin >> ii;
		translate();
		convertarrint();
		while(!check()){
			subtract();
		}
		cout << "Case #" << i + 1 << ": " << tmpnum << endl;
		tmpnum = 0;
	}
}