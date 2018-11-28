#include <iostream>
#include <math.h>

int main(){
  int iterations, stalls, people;
  std::cin >> iterations;
  for (int i = 1; i <= iterations; ++i){
    std::cin >> stalls >> people;
    int x, y, level = 0;
    while (people >= int(pow(2, level+1))){
      level += 1;
    }
    int baseLevel = int(pow(2,level));
    stalls -= baseLevel - 1;
    int stallsLeft = stalls % baseLevel;
    stalls /= baseLevel;
    if(people - baseLevel <= stallsLeft-1){
      stalls += 1;
    }
    x = stalls / 2;
    y = stalls - 1 - x;
    std::cout << "Case #" << i << ": " << x << " " << y << std::endl;
  }
}
