#include <iostream>
#include <vector>

int main(){
	int t;
	std::cin>>t;
	for(int test=1;test<t+1;++test){
		long number;
		std::cin>>number;
		int curr=10;
		std::vector<long> num;
		while(number>0){
			long temp=number%curr;
			num.push_back(temp);
			number/=curr;
		}
		
		for(int i=1;i<num.size();++i){
			if(num[i-1]<num[i]){
				num[i]--;
				int temp=i-1;
				while(temp>=0){
					num[temp]=9;
					--temp;
				}
			}
		}

		while(num.back()==0){
			num.pop_back();
		}
		std::cout<<"Case #"<<test<<": ";
		for(int i=num.size()-1;i>-1;--i){
			std::cout<<num[i];
		}
		std::cout<<'\n';

	}
	return 0;
}

