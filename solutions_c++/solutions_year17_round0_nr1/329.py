#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int main(){
	cout<<"launching function main"<<endl;
	ifstream file("A-large.in");
	ofstream outputfile("myoutput.txt");
	int T, K, pos;
	string s;
	file>>T;
	int nmoves;
	bool *sign, global, read, solved;
	for(int t=0;t<T;t++){
		//read input
		file>>s>>K;
		//solve
		sign=new bool[K];
		pos=0; nmoves=0;
		global=false;
		for(int i=0; i<K; i++)
			sign[i]=true;
		for(int i=0; i<s.length(); i++){
			switch(s[i]){
				case '+':
					read=true;
					break;
				case '-':
					read=false;
					break;
				default:
					cout<<"could not read pancake"<<endl;
			}
			if(read^(sign[i%K]^global)){
				nmoves++;
				global=!global;
				sign[i%K]=!global;
			}else
				sign[i%K]=!global;
		}
		solved=true;
		for(int i=0; i<K; i++){
			solved=solved && (global^sign[i]);
		}
		//write output
		if(solved)
			outputfile<<"Case #"<<(t+1)<<": "<<nmoves<<endl;
		else
			outputfile<<"Case #"<<(t+1)<<": "<<"IMPOSSIBLE"<<endl;
	}
	file.close();
	outputfile.close();
}

