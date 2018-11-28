#include <iostream>
#include <fstream>
#include <map>
#include <string>
#include <math.h>
#include <queue>
using namespace std;
/* run this program using the console pauser or add your own getch, system("pause") or input loop */

int main(int argc, char** argv) {
	string hi;
	int number;
	cin >> number;
	int result = 0;
	long long cursor = 0;
	long long k = 0;
	int last = 0;
	string pn;
	char abc[10000];
	long long current;
	string tmp = "";
	ofstream ofs ("c.txt", ofstream::out);
	bool borrow = false;
	priority_queue<long long> first;
	long long l = 0;
	long long r = 0;
	for (int i = 1; i <=number; i++){
		cin >> cursor; //N - space
		cin >> k; //K - ppl
		while (!first.empty()){
			first.pop();
		}
		first.push(cursor);
		while (k>0){
			current = first.top();
			//cout << current<<endl;
			first.pop();
			l = (current-1) /2;
			r = current - l - 1;
			if (current == 1){
				l = 0;
				r = 0;
			}
			if (k==0){
				break;
			}
			else{
				if (current>1){
					if (r>l){
						if (r>0){
							first.push(r);
						}
						if (l>0){
							first.push(l);
						}
					}
					else{
						if (l>0){
							first.push(l);
						}
						if (r>0){
							first.push(r);
						}
					}
				}
			}
			k--;
		}
		ofs << "Case #"<<i<<": "<<r<<" "<<l<<endl;
		//cout <<endl<< "Case #"<<i<<": "<<r<<" "<<l<<endl;
	}
	ofs.close();
	return 0;
}
