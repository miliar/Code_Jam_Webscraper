#include <iostream>
#include <string>
#include <vector>

void tidynum(){
	std::string num;
	int size;
	std::cin>>num;
	size=num.size();

	for(int i=size-1;i>0;--i){
		bool test=false;
		for(int j=i-1;j>-1&&!test;--j){
			if(num[i]<num[j]){
				test=true;
			}
		}

		if(test)
		{
			num[i]='9';
			int k=i-1;
			while(k>0&&num[k]=='0'){
				num[k]='9';
				--k;
			}

			
			--(num[k]);
			

			for(int j=i;j<size;++j)
			{
				num[j]='9';
			}

			i=k+1;
		}
	}

	int offset=0;
	while(offset<size&&num[offset]=='0'){
		++offset;
	}

	num=num.substr(offset,size-offset);
	std::cout<<num;
}

int contest(){
	int runs;
	std::cin>>runs;
	for(int i = 0; i<runs; ++i){
		std::cout<<"Case #"<<i+1<<": ";
		tidynum();
		
		std::cout<<'\n';
	}

	return 0;
}

int main(){
	contest();
	return 0;
}