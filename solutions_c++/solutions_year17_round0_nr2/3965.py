#include <iostream>
#include <fstream>
#include <map>
#include <string>
#include <math.h>
using namespace std;
/* run this program using the console pauser or add your own getch, system("pause") or input loop */

int main(int argc, char** argv) {
	string hi;
	int number;
	cin >> number;
	int result = 0;
	int cursor = 0;
	int k = 0;
	string pn;
	char abc[10000];
	char current;
	string tmp = "";
	ofstream ofs ("b.txt", ofstream::out);
	int last = 0;
	bool borrow = false;
	for (int i = 1; i <=number; i++){
		cin >> pn;
		hi = "";
		borrow = false;
		
		for (int s = pn.length()-1; s >=0;s--){
			current = pn.at(s);
			cursor = current - '0';
			if (borrow ==true){
				cursor--;
				borrow = false;
			}
			if (s==0){
				if (cursor>0){
					tmp = char(cursor+48);
					hi = string(tmp)+hi;
				}
			}
			else{ //s>0
				k = pn.at(s-1) - '0';
				if (k>cursor || cursor==0){
					borrow = true;
					tmp = hi;
					hi = "9";
					for (int j = 0; j <tmp.length(); j++){
						hi += "9";
					}
				}
				else{
					tmp = char(cursor+48);
					hi = string(tmp)+hi;
				}
			}
		}
		ofs << "Case #"<<i<<": "<<hi<<endl;
	}
	ofs.close();
	return 0;
}
