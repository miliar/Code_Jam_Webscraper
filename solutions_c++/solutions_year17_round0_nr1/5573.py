#include<iostream>
#include<string.h>
#include<fstream>
using namespace std;


int main(){
	ofstream fout;
	ifstream fin;
	fout.open("out.txt");
	fin.open("in.in");
	
	char pan[1000] = "";
	int k,t;
	fin>>t;
	for(int a = 1; a <= t;a++){
		bool o = false;
		fin>>pan;
		fin>>k;
		int cnt = 0;
		//cout<<pan;
		int l = strlen(pan);
		for(int i = 0;i < l;i++){
			if(pan[i] == '-'){
				cnt++;
				for(int j = 0;j < k;j++){
					if(i+(k-1) < l && pan[i+j] == '+' ){
						pan[i+j] = '-';
					}
					else{
						if(i+(k-1) < l)
							pan[i+j] = '+';
					}	
				}
			}
		}
		
		for(int i = 1;i <= k;i++){
			if(pan[l-i] != '+'){
				fout<<"Case #"<<a<<": IMPOSSIBLE"<<endl;
				cout<<"Case #"<<a<<": IMPOSSIBLE"<<endl;
				o = true;
				break;
			}
		}
		if(!o){
			fout<<"Case #"<<a<<": "<<cnt<<endl;
			cout<<"Case #"<<a<<": "<<cnt<<endl;
		}
	}
	return 0;
}
