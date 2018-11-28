#include <iostream>
#include <fstream>
#include <string.h>

using namespace std;

string delZero(string N){
	for(int i=0;i<N.length();i++){
  		if(N[i]=='0')N=N.erase(0,1);
  		else return N;
	}
	return N;
}

bool check(string N){
	int prev = (int)N[0]-'0';
	int prevI = 0;

	for(int i=1; i<N.length(); i++){
		int ni = (int)N[i]-'0';
		if(ni < prev)return false;
		else{
			prevI = i;
			prev = (int)N[prevI]-'0';
   		}
	}
	return true;
}

string update(string N, int start){
	for(int i=start;i<N.length(); i++)N[i] = '9';
	return N;
}

string tidy(string N){
	int len = N.length();
	int prev = (int)N[0]-'0';
	int prevI = 0;
	while(!check(N)){
		for(int i=1; i<len; i++){
			int ni = (int)N[i]-'0';

			if(ni < prev){
				int temp =(int)N[prevI]-'0';
				N[prevI]= (temp-1)+'0';
				N = update(N,i);
   			}
			else{
				prevI = i;
				prev = (int)N[prevI]-'0';
	   		}
		}
		prev = (int)N[0]-'0';
		prevI = 0;
	}
	return N;
}


int main(){
	ifstream ccin("B-large.in");
	ofstream ccout("large_output.txt");

	int T;
	ccin>>T;
	string N;
	
	for(int i=1; i<=T; i++){
		ccin>>N;
		N = tidy(N);
		N = delZero(N);
		ccout<<"Case #"<<i<<": "<<N<<endl;
	}
	
	
}
