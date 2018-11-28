#include <sstream>
#include <string>

#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

char decrement(char c){
	return (c-1);
}

int main(){
	cout<<"launching function main"<<endl;
	ifstream file("B-large.in");
	ofstream outputfile("myoutput.txt");
	int T, lower, pos;
	string s;
	file>>T;
	for(int t=0;t<T;t++){
		//read input
		file>>s;
		//solve
		lower=0; pos=0;
		while(pos<(s.length()-1)){
			if(s[pos]<=s[pos+1]){
				if(s[pos]!=s[pos+1])
					lower=(pos+1);
				pos++;
			}else{
				pos=(s.length());
			}
		}
		if(pos==(s.length()-1))
			lower=(pos+1);
		//write output
		outputfile<<"Case #"<<(t+1)<<": ";
		for(int i=0; i<lower; i++)
			outputfile<<s[i];
		if(lower != s.length()){
			if(!(lower==0 && (s[0]=='1'))){
				outputfile<<(decrement(s[lower]));
			}
		}
		for(int i=(lower+1); i<s.length(); i++)
			outputfile<<'9';
		outputfile<<endl;
	}
	file.close();
	outputfile.close();
}

