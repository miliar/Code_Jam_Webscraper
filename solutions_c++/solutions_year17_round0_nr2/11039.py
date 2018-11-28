#include <iostream>
#include <string.h>
#include <fstream>

using namespace std;


bool is_tidy(long num){
  if (num < 10){
    return true;
  }

  if (num%10 >= (num/10)%10){
    return is_tidy(num/10);
  }
  else return false;
}


int main(){


  int numtests = 0;
  ifstream testfile;

  testfile.open("input.txt");

  testfile >> numtests;

  long tests [numtests];

  for (int i = 0; i < numtests; i++){
    testfile >> tests[i];
  }

  for(int i = 0; i < numtests; i++){

    while(is_tidy(tests[i]) == false){
      tests[i]--;
    }
    cout << "Case #" << i+1 << ": " << tests[i] << endl;
  }

  testfile.close();

}
