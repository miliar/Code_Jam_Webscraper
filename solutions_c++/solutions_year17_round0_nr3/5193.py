#include <iostream>
#include <string>
#include <vector>
#include <cmath>

int divideAndConquer(const long long int &val, std::vector<long long int> &outVals){
	int ret = val&1;
	for(int i=0;i<4;++i){
		outVals[i]=0;
	}

	if(ret){
		outVals[0]=2;
		outVals[1]=val>>1;
	}else{
		outVals[0]=outVals[2]=1;
		outVals[1]=val>>1;
		outVals[3]=outVals[1]-1;
	}

	return ret;
}

void broom(){
	long long int n,k;
	std::cin>>n>>k;
	long long int openIntervals[64][4];
	std::vector<long long int> tmp(4);
	for(int i=0; i<64;++i){
		for(int j=0;j<4;++j){
			openIntervals[i][j]=0;
		}
	}
	openIntervals[0][0] = 1;
	openIntervals[0][1] = n;
	long long int seated = 0;
	int level=0;
	for(level=0;level<63&&seated<k;++level){
		seated <<=1;
		seated |= 1;
		divideAndConquer(openIntervals[level][1],tmp);
		openIntervals[level+1][0]=openIntervals[level][0]*tmp[0];
		openIntervals[level+1][1]=tmp[1];
		openIntervals[level+1][2]=openIntervals[level][0]*tmp[2];
		openIntervals[level+1][3]=tmp[3];

		if(divideAndConquer(openIntervals[level][3],tmp)){
			if(tmp[1]==openIntervals[level+1][1]){
				openIntervals[level+1][0]+=openIntervals[level][2]*tmp[0];
			}else{
				openIntervals[level+1][2]+=openIntervals[level][2]*tmp[0];
			}
		}else if(openIntervals[level][3]!=0){
			openIntervals[level+1][0]+=tmp[0]*openIntervals[level][2];
			openIntervals[level+1][1]=tmp[1];
			openIntervals[level+1][2]+=tmp[2]*openIntervals[level][2];
			openIntervals[level+1][3]=tmp[3];
		}
	}//end seating
	--level;
	int offset = k - (seated>>1);

	if(offset <= openIntervals[level][0]){
		offset = 1;
	}else{
		offset = 3;
	}

	if(divideAndConquer(openIntervals[level][offset],tmp)){
		std::cout<<tmp[1]<<' '<<tmp[1];
	}else{
		std::cout<<tmp[1]<<' '<<tmp[3];
	}

}

int contest(){
	int runs;
	std::cin>>runs;
	for(int i = 0; i<runs; ++i){
		std::cout<<"Case #"<<i+1<<": ";
		broom();

		std::cout<<'\n';
	}

	return 0;
}

int main(){
	contest();
	return 0;
}