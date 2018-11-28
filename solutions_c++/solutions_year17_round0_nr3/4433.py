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

int mLog2(int mK){
	int ret = -1;
	while(mK>0){
		ret++;
		mK>>=1;
	}
	return ret;
}

int mPow(int mK){
	return 1<<mK;
}

int main(){
	string name = "C-small-2-attempt1";
	string path = "";
	
	ifstream fin((path+name+".in").c_str());
	ofstream fout((path+name+".out").c_str(), ios::app);
	
	int test_case;
	fin>>test_case;
	
	for(int t=1; t<=test_case; t++){
		int mN, mK;
		fin>>mN>>mK;
		
		int mJisu = mLog2(mK);
		int mSize = mPow(mJisu);
		
		int mok = (mN-mSize+1)/mSize;
		int remain = (mN-mSize+1)%mSize;
		
		int mChk = 0;
		if(mK-mSize+1<=remain) mChk = mok + 1;
		else mChk = mok;
		
		if(mChk%2==0) fout<<"Case #"<<t<<": "<<mChk/2<<' '<<mChk/2-1<<'\n';
		else fout<<"Case #"<<t<<": "<<mChk/2<<' '<<mChk/2<<'\n';
	}
	
	fin.close();
	fout.close();
	return 0;
}
