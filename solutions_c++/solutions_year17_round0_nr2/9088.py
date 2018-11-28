#include <iostream>
#include <String>

int main(){
  int iterations;
  std::string input;
  std::cin >> iterations;
  for (int i = 1; i <= iterations; ++i){
    bool idenNum = false;
    int idenNumInt = 0;
    std::cin >> input;
    int decreasing = 1;
    if(input.size() != 1){
      while(input[decreasing] >= input[decreasing-1] && decreasing <= input.size()){
        if(input[decreasing] == input[decreasing-1]){
          if(!idenNum){
            idenNumInt = decreasing - 1;
          }
          idenNum = true;
        }
        else{
          idenNum = false;
        }
        decreasing += 1;
      }
      if(decreasing != input.size() && !idenNum){
        input[decreasing] = '9';
        input[decreasing-1] = char(int(input[decreasing-1] - 1));
        decreasing += 1;
      }
      else if(decreasing != input.size()){
        decreasing = idenNum;
        input[decreasing-1] = char(int(input[decreasing-1] - 1));
      }
      while(decreasing <= input.size()){
        input[decreasing] = '9';
        decreasing += 1;
      }
      while(input[0] == '0'){
        input.erase(0, 1);
      }
    }
    std::cout << "Case #" << i << ": " << input << std::endl;
  }
}
