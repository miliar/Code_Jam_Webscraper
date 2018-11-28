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
	string name = "B-large";
	string path = "";
	
	ifstream fin((path+name+".in").c_str());
	ofstream fout((path+name+".out").c_str(), ios::app);
	
	int test_case;
	fin>>test_case;
	
	for(int t=1; t<=test_case; t++){
		long long mN;
		fin>>mN;
		
		vector<int> mV;
		while(mN>0){
			mV.push_back(mN%10);
			mN/=10;
		}
		
		if(mV.size()==1) fout<<"Case #"<<t<<": "<<mV[0]<<'\n';
		else{
			for(int i=0; i<mV.size()-1; i++){
				if(mV[i]<mV[i+1]){
					for(int j=i; j>=0; j--){
						mV[j]=9;
					}
					mV[i+1]--;
				}
			}
			
			fout<<"Case #"<<t<<": ";
			for(int i=mV.size()-1; i>=0; i--){
				if(i==mV.size()-1 && mV[i]==0) continue;
				else fout<<mV[i];
			}
			fout<<'\n';
		}
	}
	
	fin.close();
	fout.close();
	return 0;
}
