#include <iostream>
#include <fstream>
#include <map>
#include <string>
#include <math.h>
#include <iomanip>
using namespace std;
#define ll long long 
/* run this program using the console pauser or add your own getch, system("pause") or input loop */


int main(int argc, char** argv) {
	string hi;
	int number;
	cin >> number;
	double result = 0;
	int cursor = 0;
	string pn;
	char abc[10000];
	char current;
	int k = 0;
	ofstream ofs ("a.txt", ofstream::out);
	int last = 0;
	bool okay = true;
	long long des;
	int houses = 0;
	ll speeds[10000];
	ll start[10000];
	double stop[10000];
	double slowest = 0;
	int farest = 0;
	double pre = 0;
	for (int i = 1; i <=number; i++){
		cin >> des >> houses;
		result = 0;
		slowest = 0;
		farest = 0;
		for (int j =0; j < houses; j++){
			cin >> start[j] >> speeds[j];
			stop[j] = (des-start[j])*1.0/speeds[j]; //finish at time 
			if (slowest<stop[j]){
				slowest = stop[j];
			}
			if (start[j]<start[farest]){
				farest = j;
			}
		}
		
		//further optimize
		//small case
		if (stop[1]<stop[0]){ //farest will not catch the earlier house
			result = des/stop[0];
		}
		else{ //farest will and convert its speed to this
			result = des/stop[1];
		}
		
		//large case		
		result = des/slowest;
		pre = log(result);
		if (pre<0){
			pre = 0;
		}
		else{
			pre = (int)pre + 1;
		}
		cout << pre+6<<endl;
		ofs << "Case #"<<i<<": "<<setprecision(pre+6)<<result<<endl;
	}
	ofs.close();

	return 2;
}
