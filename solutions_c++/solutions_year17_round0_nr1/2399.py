#include <iostream>
#include <string>

int main(){
	int test;
	std::cin>>test;
	for(int t=1;t<=test;++t){
		std::string vec;
		int size;
		std::cin>>vec>>size;
		int count=0;
		for(int i=0;i<=vec.size()-size;++i){
			if(vec[i]=='-'){
				++count;
				for(int j=0;j<size;++j){
					if(vec[j+i]=='-')
						vec[j+i]='+';
					else
						vec[j+i]='-';
				}
			}
		}
		bool bad=false;
		for(int i=vec.size()-size;i<vec.size();++i){
			if(vec[i]=='-')
				bad=true;
		}
		std::cout<<"Case #"<<t<<": ";
		if(bad){
			std::cout<<"IMPOSSIBLE\n";
		}else{
			std::cout<<count<<'\n';
		}

	}

	return 0;
}
