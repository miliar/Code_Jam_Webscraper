#include <iostream>
#include <string>
#include <algorithm>
#include <vector>


int findSpot(std::vector<char> stalls);
std::vector<char> populate(std::vector<char> stalls, int numPeople);
int calcLS(std::vector<char> stalls, int spot);
int calcRS(std::vector<char> stalls, int spot);


int main()
{
  int n;
  std::cin >> n;

  for (int i=1; i<=n; ++i) {
    int numStalls, numPeople;
    std::cin >> numStalls >> numPeople;
    std::vector<char> stalls;
    
    for (int i = 0; i < numStalls; ++i)  stalls.push_back('.');
    stalls = populate(stalls, numPeople);
    int finalSpot = findSpot(stalls);
    stalls[finalSpot] = 'o';
    int LS = calcLS(stalls, finalSpot);
    int RS = calcRS(stalls, finalSpot);
    
    std::cout << "Case #" << i << ": " << std::max(LS, RS) << " " << std::min(LS, RS) << std::endl;
    // std::cout << stalls.size() << std::endl;
  }

  // std::vector<char> stalls;
  // for (int i = 0; i < 4; ++i)  stalls.push_back('.');
  // for (int i = 1; i < 2; ++i) {
  //   int spot = findSpot(stalls);
  //   // std::cout << spot << std::endl;
  //   stalls[spot] = 'o';
  //   for (int j = 0; j < stalls.size(); ++j) {
  //     std::cout << stalls[j] << " ";
  //   }
  //   std::cout << std::endl;
  // }
  // int finalSpot = findSpot(stalls);
  // int LS = calcLS(stalls, finalSpot);
  // int RS = calcRS(stalls, finalSpot);
  // std::cout << finalSpot << " " << LS << " " << RS << std::endl;


}


std::vector<char> populate(std::vector<char> stalls, int numPeople) {
  for (int i = 1; i < numPeople; ++i) {
    int spot = findSpot(stalls);
    stalls[spot] = 'o';
  }
  return stalls;
}

int findSpot(std::vector<char> stalls) {
  int count = 0;
  int longestCount = 0;
  int start = 0;
  int longestStart = 0;
  for (int i = 0; i < stalls.size(); i++) {
    if (stalls[i] == '.') count++; 
    else {
      if (count > longestCount) {
        longestCount = count;
        longestStart = start;
      }
      count = 0;
      start = i+1;
    }
    if (count > longestCount) {
        longestCount = count;
        longestStart = start;
      }
  }
  return (longestStart + ((longestCount - 1)/2));
}

int calcLS(std::vector<char> stalls, int spot) {
  int count = 0;
  int iterator = spot - 1;
  if(iterator == 0 && stalls[0] == '.'){
    count++;
    iterator--;
  }
  while (iterator >= 0 && stalls[iterator] == '.') {
      count++;
      iterator--;
  }
  return count;
}

int calcRS(std::vector<char> stalls, int spot) {
  int count = 0;
  int iterator = spot + 1;
  if(iterator == (stalls.size()-1) && stalls[stalls.size()-1] == '.') {
    count++;
    iterator++;
  }
  while (iterator < stalls.size() && stalls[iterator] == '.') {
      count++;
      iterator++;
  }
  return count;
}

