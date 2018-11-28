#include<iostream>
#include<fstream>
using namespace std;
string str;
int count(int where){
	if(str[where]=='0'){
		str[where]='9';
		count(where-1);
	}
	else str[where]--;
}
int minmax(int where){
	str[where]='9';
	count(where-1);
}
bool check(string str){
	for(int i=0;i<str.size()-1;i++){
		if(str[i]>str[i+1]&&str[i]!='0')return 1;
	}
	return 0;
}
int main(){
	fstream  file,file2 ;
	file.open("B-large.in",ios::in);
	file2.open("out",ios::out);
	int t;
	file>>t;
	//cin>>t;
	for(int f=1;f<=t;f++){ 
		file>>str;
		//cin>>str;
		//cout<<"Case #"<<f<<": ";
		file2<<"Case #"<<f<<": ";
		if(str.size()<2){
			//cout<<str<<endl;
			file2<<str<<endl;
			continue;
		}
		int k=str.size()-1;
		while(check(str)){
			minmax(k);
			k--;
		}
		for(int i=0;i<str.size();i++){
			if(str[i]!='0'){
				//cout<<str[i];
				file2<<str[i];
			}
		}
		//cout<<endl;
		file2<<endl;
	}
}

