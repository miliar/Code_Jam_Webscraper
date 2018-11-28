#include <iostream>
#include <fstream>
#include <set>
#include <queue>
#include <iostream>
#include <memory>
#include <cmath>
#include <bitset>
#include <string>
struct Node {
  std::shared_ptr<Node> parent;
  uint16_t data;
};

//Here we use at 16 bit integer to represent the possible states of the pancakes
//1 represents a +
//0 represents a -

//N is the number of pancakes, K is the size of the fliper 
std::shared_ptr<Node> flipBFS(const unsigned int N, const uint16_t state, const unsigned int K) {
  const uint16_t flipMask = pow(2, K) - 1;
  const uint16_t finalState = pow(2, N) - 1;
  std::set<uint16_t> states;
  std::queue<std::shared_ptr<Node>> toVisit;
  toVisit.push(std::make_shared<Node>(Node{nullptr, state}));
  while(toVisit.empty() == false){
    auto current = toVisit.front();
    toVisit.pop();
    if(current->data == finalState){
      return current;
    }
    for(unsigned int i = 0; i < N - K + 1; i++) {
      uint16_t newState = current->data ^ (flipMask << i);
      if(states.count(newState) == 0) {
        states.insert(newState);
        toVisit.push(std::make_shared<Node>(Node{current, newState}));
      }
    }
  }
  return nullptr;
}

const uint16_t getStateFromString(std::string string) {
  uint16_t result = 0;
  for(auto pancake : string) {
    if(pancake == '+') {
      result = (result << 1) | 1;
    }
    else {
      result = result << 1;
    }
  }
  return result;
}
const std::string findFlips(const unsigned int N, const uint16_t state, const unsigned int K) {
  auto outnode =  flipBFS(N, state, K);
  if(outnode == nullptr) {
    return "IMPOSSIBLE";
  }
  int numflips = 0;
  while(outnode->parent != nullptr) {
    numflips++;
    outnode = outnode->parent;
  }
  return std::to_string(numflips); 
}
int main(int argc, char** argv) {
  std::ifstream input;
  std::ofstream output;
  input.open(argv[1]);
  output.open("pancakes.out");
  int numTests;
  input >> numTests;
  for(int i = 1; i <= numTests; i++){
    std::string initial;
    int K;
    input >> initial >> K;
    uint16_t state =  getStateFromString(initial);
    output << "Case #" << i << ": " << findFlips(initial.length(), state, K) << '\n';  
  }

}
