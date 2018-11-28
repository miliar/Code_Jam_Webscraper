#include <iostream>
#include <cmath>

using namespace std;

unsigned long long getTidyNumber(unsigned long long K) {
  unsigned long long upperLimit = 1;
  int numDigits = 0;
  int ii = 0;
  while (((unsigned long long) (K/pow(10,ii))) >= 10) {
    ++ii;
    upperLimit = upperLimit * 10 + 1;
  }
  unsigned long long pivot = ((unsigned long long) (K/pow(10,ii))) * upperLimit;
  
  if (K < pivot) {
    unsigned long long value = ((unsigned long long) (K/pow(10,ii)))*pow(10,ii);
    value -= 1ULL;
    return value;
  } else if (K == pivot) {
    return pivot;
  }
  return ((unsigned long long) (K/pow(10,ii)))*pow(10,ii) + getTidyNumber(K-((unsigned long long) (K/pow(10,ii)))*pow(10,ii));
}

int main(int argc, char* argv[]) 
{
  int t;
  cin >> t;
  for (int i = 1; i <= t; ++i) {
    unsigned long long K;
    cin >> K;
    cout << "Case #" << i << ": " << getTidyNumber(K) << endl;
  }
  return 0;
}
