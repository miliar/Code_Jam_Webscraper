#include<iostream>
#include<fstream>
#include<string>
using namespace std;

int main(){
	ifstream fin("in11.txt");
	ofstream fout("out11.txt");
	
	int T;
	string str;
	int size;
	int steps;
	fin>>T;
	
	for(int i=1;i<=T;i++){
		steps = 0;
		fin>>str>>size;
		
		for(int j=0;str[j];j++){
			if(str[j] == '-'){
				if(j+size > str.length()){
					steps = -1;
					break;
				}
				for(int k=0;k<size;k++){
					if(str[k+j] == '+')
						str[k+j] = '-';
					else
						str[k+j] = '+';
				}
				steps++;
			}
		}
		
		
		fout<<"Case #"<<i<<": ";
		if(steps!=-1)
			fout<<steps<<endl;
		else
			fout<<"IMPOSSIBLE"<<endl;			
	}
}
