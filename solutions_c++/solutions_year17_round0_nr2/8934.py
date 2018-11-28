#include <iostream>
#include <string>
#include <cmath>
#include <vector>
#include <fstream>
using namespace std;

int getEachDigit(long long n) {
  int smaller = 0;
  if(n >= 10) {
    smaller = getEachDigit(n / 10);
    if(smaller == -1) {
      return -1;
    }
  }

  int digit = n % 10;
  if(smaller > digit) {
    return -1;
  }

  return digit;
}

bool checkNumberOrder(long long n) {
  int check = getEachDigit(n);
  if(check == -1) {
    return false;
  }

  return true;
}

int main() {
  ifstream in("B-small.in");
  streambuf *cinbuf = cin.rdbuf();
  cin.rdbuf(in.rdbuf());

  ofstream out("B-small.out");
  streambuf *coutbuf = cout.rdbuf(); //save old buf
  cout.rdbuf(out.rdbuf());

  int t;
  long long num;
  string n;
  bool orderCheck;

  cin >> t;
  for(int i = 1; i <= t; i++) {
    cin >> n;
    num = stoll(n);
    orderCheck = false;
    while(!orderCheck) {
      orderCheck = checkNumberOrder(num);
      if(orderCheck == true)
        break;

      num--;
    }
    if(orderCheck) {
      cout << "Case #" << i << ": " << num << endl;
    }
  }
  return 0;
}
