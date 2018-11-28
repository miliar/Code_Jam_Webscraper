#include <iostream>
#include <boost/multiprecision/cpp_int.hpp>
#include <fstream>
#include <sstream>
namespace mp = boost::multiprecision;
using namespace std;

bool numberIsTidy(const mp::cpp_int &number){
	stringstream ss;
	ss<<number;
	string str = ss.str();
	char fch = str[0];
	int i = 0;
	while(i<str.size()){
		char ch = str[i];
		if(fch>ch){
			return false;
		}
		fch = str[i];
		i++;
	}
	
	return true;
}


bool numberIsTidy2(const mp::cpp_int &number){
	stringstream ss;
	ss<<number;
	string str = ss.str();
	string minorTidyStr = "";
	for(int i=0;i<str.size()-1;i++) { 
		minorTidyStr+='9';
	}
	mp::cpp_int minorTidy (minorTidyStr);
	
	char fch = str[0];
	int i = 0;
	while(i<str.size()){
		char ch = str[i];
		if(fch>ch){
			return false;
		}
		fch = str[i];
		i++;
	}
	
	return true;
}


bool numberIsTidyStr(const string &str){
	char fch = str[0];
	int i = 0;
	while(i<str.size()){
		char ch = str[i];
		if(fch>ch){
			return false;
		}
		fch = str[i];
		i++;
	}
	
	return true;
}


void take(string &str, int pos){
	if(pos<0) return;
//	cout<<"Taking from "<<pos<<endl;
	if(str[pos]!='0'){
		str[pos] = str[pos]-1;
	}else{
		str[pos]='9';
		for(int j = pos; j<str.size(); j++){
			str[j] = '9';
		}
		take(str, pos-1);
	}
}

string findTidy(const mp::cpp_int &number){
	stringstream ss;
	ss<<number;
	string str = ss.str();
	while(!numberIsTidyStr(str)){
		for(int i=str.size()-1;i>0;i--) { 
			
			if(str[i]<str[i-1]){
//				cout<<"Transforming: "<<str<< "   =>   ";
				for(int j = i; j<str.size(); j++){
					str[j] = '9';
				}
				
				take(str, i-1);
				
//				cout<<str<<endl;
			}
			
		}
		
		while(str[0] == '0'){
			str.erase(0, 1);
		}
	}
	
	return str;
}

int main(int argc, char *argv[]) {
	if(argc < 2){
		cerr<<"ERROR: No input file."<<endl;
		return -1;
	}
	ifstream input(argv[1]);
	if(!input.is_open()){
		cerr<<"ERROR: File \""<<argv[1]<<"\" not found."<<endl;
		return -1;
	}
	
	int N;
	input>>N;
	for(int i = 0; i<N; i++){
		mp::cpp_int n;
		
		input>>n;
		cout<<"Case #"<<i+1<<": "<<findTidy(n)<<endl;
		
	}
	return 0;
}

