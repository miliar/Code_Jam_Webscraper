#include <iostream>
#include <vector>

void solve(std::string str,int K){
  std::vector<int> flip;
  flip.resize(str.length()+1);
  int ac=0;
  int cnt=0;
  for(int i=0;i<str.length();i++){
    ac^=flip[i];
    //std::cout<<"I="<<i<<"\tstr[i]="<<str[i]<<"\tflip[i]="<<flip[i]<<"\tac="<<ac<<std::endl;
    if((str[i]=='-')^ac){
      if(i+K>str.length()){
	std::cout<<"Impossible"<<std::endl;
	return;
      }
      flip[i+K]^=1;
      ac^=1;
      cnt++;
    }
  }
  std::cout<<cnt<<std::endl;
}

int main(){
  int T;
  std::cin>>T;
  for(int i=1;i<=T;i++){
    std::string str;
    int K;
    std::cin>>str>>K;
    std::cout<<"Case #"<<i<<": ";
    solve(str,K);
  }
  return 0;
}
