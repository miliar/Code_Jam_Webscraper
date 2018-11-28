#include <iostream>
#include <string>
#include <vector>


int pflip(){
	std::string pancakeString;
	std::cin>>pancakeString;
	int k;
	std::cin>>k;
	int size = pancakeString.size();
	int flippable = size-k+1;
	int flips=0;

	if(k<=size){
		for(int i=0;i<flippable;++i){
			if(pancakeString[i] == '-')
			{
				for(int j=0;j<k;++j)
				{
					if(pancakeString[i+j] == '-'){
						pancakeString[i+j] = '+';
					}else{
						pancakeString[i+j]='-';
					}
				}
				++flips;
			}
		}
	}

	for(int i = (flippable>0)?flippable:0;i<size;++i){
		if(pancakeString[i] == '-')
			return -1;
	}
	
	return flips;
}

int contest(){
	int runs;
	int val;
	std::cin>>runs;
	for(int i = 0; i<runs; ++i){
		std::cout<<"Case #"<<i+1<<": ";
		val = pflip();
		if(val < 0){
			std::cout<<"IMPOSSIBLE";
		}
		else
			std::cout<<val;

		std::cout<<'\n';
	}

	return 0;
}

int main(){
	contest();
	return 0;
}