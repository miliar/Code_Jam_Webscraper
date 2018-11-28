#include <iostream>
#include <fstream>
#include <string>
#include <stdlib.h>
#include <cstdlib>

#include <vector>


using namespace std;


void parseNumber(unsigned long long int nummer, int iteration); //Prototype

int main() {

  //Get the data
  int t = 0;//Number of testcases


  //Get the data
  cin >> t;
  //cout << "The number of test cases is "<< t << endl;

  //Each of the testcases
  for(int zz = 0; zz < t; zz++) {
    //Get the string
    string number;
    cin >> number;
    //cout << "The string number is " << number << endl;
    unsigned long long int nummer = stoull(number);
    //cout << "The integer is " << nummer << endl;
    //Analyze the number 
    parseNumber(nummer,zz);
    number.clear();
  }
}


void parseNumber(unsigned long long int nummer, int iteration) {
  
  while(true) {
    //Test condition for a tidy number  
    string number = to_string(nummer);
    //See if it complies with tidy property 
    bool isTidy = true;//Better be optimistic =)
    unsigned long long int currentIt = 0;
    int digit0 = 0;
    int digit1 = 0;
    for(int i = 0; i < number.size()-1; i++) {
      currentIt = i;
      digit0 = int(number[i]-'0');
      digit1 = int(number[i+1]-'0');
      //Tidyness check
      if(digit0 > digit1) {
        isTidy = false;
        break;
      }
    } 
    if(isTidy == true) {
      cout << "Case #"<<iteration+1<<": "<<nummer<< endl;
      return;
    }
    //nummer--;
    currentIt++;
    string pending = number.substr(currentIt,number.size()-currentIt); 
    unsigned long long int decrease = stoull(pending)+1;   
    //cout << "The value of decrease is " << decrease << endl;
    nummer -= decrease; 
  }
}

