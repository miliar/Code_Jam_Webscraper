#include <iostream>

void test(std::string str){
  char max;
  for(int i=0;;i++){
    if(i==str.size()-1){
      std::cout<<str<<std::endl;
      return;
    }
    if(str[i]>str[i+1]){
      max=str[i];
      break;
    }
  }
  for(int j=0;;j++){
    if(str[j]==max){
      if(str[j]>'1'){
	std::cout<<char(str[j]-1);
      }
      for(j++;j<str.size();j++){
	std::cout<<9;
      }
      std::cout<<std::endl;
      return;
    }
    std::cout<<str[j];
  }
}

int main(){
  int T;
  std::cin>>T;
  for(int i=1;i<=T;i++){
    std::string str;
    std::cin>>str;
    std::cout<<"Case #"<<i<<": ";
    test(str);
  }
  return 0;
}
