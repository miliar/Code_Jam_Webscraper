#include<iostream>
#include<iomanip>

double solve(){
  double Distance, number;
  double remaining, speed, min = -1;
  std::cin >> Distance >> number;
  for(int i = 0; i < number; i++){
    double buff;
    std::cin >> remaining >> speed;
    buff = (Distance - remaining) / speed;
    if(buff > min || min == -1)
      min = buff;
  }
  return (Distance / min);
}

int main(){
  int T;
  std::cin >> T;

  for(int i = 1; i <= T; i++){
    std::cout << std::fixed;
    std::cout << std::setprecision(10);
    std::cout << "Case #" << i << ": " << solve() << std::endl;
  }
  return 0;
}
