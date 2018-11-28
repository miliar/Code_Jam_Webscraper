#include <iostream>
#include <fstream>
#include <string.h>
#include <cstdlib>
#include <stdio.h>
#include <string>

#include <vector>


using namespace std;


void parsePancake(string pancakes, int zz, int k); //Prototype

int main() {

  //Get the data
  int t = 0;//Number of testcases
  int k = 0;//Size of the pancake flipper


  //Get the data
  cin >> t;
  //cout << "The number of test cases is "<< t << endl;

  //Each of the testcases
  for(int zz = 0; zz < t; zz++) {

    bool readPanck = true;
    //Get the pancake
    string panck;
    cin >> panck;
    //cout << "The pancake array is " << panck << endl;
    cin >> k;
    //cout << "The size of k is " << k << endl;
    //Call the function to parse the pancake array
    parsePancake(panck, zz, k);
    //Go to next iteration
    panck.clear();
  }
}


void parsePancake(string pancake, int iteration, int k) {
  int i = 0;
  int numFlips = 0;
  while(true) {
    if(i == pancake.size()-1 && pancake[i] == '+') {
      cout << "Case #"<< iteration+1 <<": "<< numFlips << endl;
      return;
    }
    else if(pancake[i] == '-' && pancake.size()-i < k) {
      cout << "Case #"<< iteration+1 <<": IMPOSSIBLE" << endl;
      return;
    }
    //No ending condition

    //cout << "The value of i is " << i << endl;
    if(pancake[i] == '-') {//We must flip
      int counter = i;
      for(int pp=0; pp < k; pp++) {
        //cout << "The character is " << pancake[counter] << endl;
        switch(pancake[counter]) {
          case '+':
              pancake[counter] = '-';
            break;
          case '-':
              pancake[counter] = '+';
            break;
          default:
              cout << "Something really bad happened =( "<< endl;
              return;
            break;  
        }
        counter++;
      }  
      numFlips++;  
    }
    i++; 
  }
}

