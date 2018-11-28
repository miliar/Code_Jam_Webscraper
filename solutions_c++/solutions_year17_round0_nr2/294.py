#include <iostream>
#include <string>

int T;

int main(){
	std::cin>>T;
	
	for(int i=0;i<T;i++){
		std::string digits;
		std::cin>>digits;
		int L=digits.length();
		
		std::cout<<"Case #"<<i+1<<": ";
		
		char last='0';
		int idx=0;
		bool good=true;
		
		for(int j=0;j<L;j++){
			if(digits[j]>last){
				last=digits[j];
				idx=j;
			}else if(digits[j]<last){
				good=false;
				break;
			}
		}
		if(good)
			idx=L;
		
		for(int j=0;j<L;j++){
			if(j<idx)
				std::cout<<digits[j];
			else if(j==idx){
				if(!(j==0 && digits[j]=='1'))
					std::cout<<char(digits[j]-1);
			}else
				std::cout<<'9';
		}
		
		std::cout<<'\n';

	}
	return 0;
}