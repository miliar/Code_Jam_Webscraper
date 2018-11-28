#include <iostream>
#include <algorithm>
#include <string>
#include <cstring>
#include <vector>
#include <set>
#include <cstdio>
#include <cmath>
#include <limits>
#include <fstream>

using namespace std;

int main(){
	string name = "A-large";
	string path = "";
	
	ifstream fin((path+name+".in").c_str());
	ofstream fout((path+name+".out").c_str(), ios::app);
	
	int test_case;
	fin>>test_case;
	
	for(int t=1; t<=test_case; t++){
		string mS;
		int mK;
		fin>>mS>>mK;
		
		int cnt=0;
		for(int i=0; i<mS.size(); i++){
			if(mS[i]=='-'){
				if(i+mK<=mS.size()){
					for(int j=0; j<mK; j++){
						if(mS[i+j]=='-') mS[i+j]='+';
						else mS[i+j]='-';
					}
					cnt++;
				}else{
					cnt=-1;
					break;
				}
			}
		}
		
		if(cnt==-1) fout<<"Case #"<<t<<": IMPOSSIBLE"<<'\n';
		else fout<<"Case #"<<t<<": "<<cnt<<'\n';
	}
	
	fin.close();
	fout.close();
	return 0;
}
