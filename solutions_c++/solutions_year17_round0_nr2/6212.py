#include <iostream>
long long n;
std::string str;
long long pos;

int main()
{
	std::cin>>n;
	for(int i=1;i<=n;i++){
		std::cin>>str;
		if(str.size()==1){
			std::cout<<"Case #"<<i<<": "<<str;
			std::cout<<"\n";
			continue;
		}
		for(int j=0;j<str.size()-1;j++){
			if(str[j]>str[j+1]){
				str[j]--;
				for(int k=j+1;k<str.size();k++){
					str[k]='9';
				}
				pos=j;
				break;
			}
		}
		for(int j=pos;j>0;j--){
			if(str[j]<str[j-1]){
				str[j-1]--;
				str[j]='9';
			}
		}
		pos=0;
		std::cout<<"Case #"<<i<<": ";
		while(str[pos]=='0') pos++;
		for(int j=pos;j<str.size();j++){
			std::cout<<str[j];
		}
		std::cout<<"\n";
	}	
	return 0;
}