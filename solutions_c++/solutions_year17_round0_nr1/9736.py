#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#define MIN(x,y) (x)<(y)?(x):(y)
#define INF 999999999
using namespace std;

int flip;
ofstream fout;
ifstream fin;

int recur(string in,int now,int tried,int pluscot){
	if( now >= in.size()) return INF;
	if( pluscot == in.size()){
		return 0; 
	}
	
	string temp = in;
	int pcot = pluscot;
	int mn = INF;
	int tmn = INF, cmn = INF;
	int st,dest;

	for(int i=0;i<flip+1;i++){
		st = ( (now + i) - (flip-1) );
		dest = st + ( flip -1 );
		if( st < 0 || dest >= in.size()) continue;
		if( i == flip ) { 
			cmn = recur(temp,now+1,tried,pcot);
			break;
		}
		for(int j=st;j<=dest;j++){
			if(temp[j] == '+'){
				temp[j] = '-'; 
				pcot --;
			}
			else{
				temp[j] = '+';
				pcot ++;
			}
		}
		tmn = recur(temp,now+1,tried+1,pcot);
		mn = MIN(tmn,mn);
		temp = in;
		pcot = pluscot;

	}
	if( cmn != INF && cmn < mn ) return cmn;
	else if( mn != INF) return mn+1;
	else return INF;
}
int main(){
	fin.open("input.txt");
	fout.open("output.txt");
	string input; int test;
	fin >> test;
	
	for(int z=1;z<=test;z++){

		fin >> input;
		fin >> flip;
		int c=0;
		for(int i=0;i<input.size();i++) 
			if( input[i] == '+') c++;
		int t = recur(input,0,0,c);
		fout << "Case #" << z << ": " ;
		if( t == INF) fout << "IMPOSSIBLE" << endl;
		else fout << t << endl;
	}

	fin.close();
	fout.close();
	return 0;
}