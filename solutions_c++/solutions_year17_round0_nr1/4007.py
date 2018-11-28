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
	string pn;
	char abc[10000];
	char current;
	int k = 0;
	ofstream ofs ("a.txt", ofstream::out);
	int last = 0;
	bool okay = true;
	for (int i = 1; i <=number; i++){
		cin >> pn;
		cin >> k; //flip count, k at least 2
		last = pn.length()-k; 
		result = 0;
		okay = true;
		for (int s = 0; s <= last;s++){
			current = pn.at(s);
			if (current=='-'){
				for (int t = s; t<s+k; t++){
					pn.at(t) = (pn.at(t)=='-')?'+':'-';
				}
				result++;
			}
		}
		for (int lll = last+1; lll<pn.length();lll++){
			if (pn.at(lll)=='-'){
				okay = false;
				break;
			}
		}
		if (okay){
			ofs << "Case #"<<i<<": "<<result<<endl;
		}
		else{
			ofs << "Case #"<<i<<": IMPOSSIBLE"<<endl;
		}
	}
	ofs.close();
	return 0;
}
