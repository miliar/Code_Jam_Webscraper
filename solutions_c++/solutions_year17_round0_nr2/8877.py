/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/* 
 * File:   main.cpp
 * Author: sally090230
 *
 * Created on April 7, 2017, 8:48 PM
 */

#include <cstdlib>
#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <algorithm>    // std::reverse
#include <vector>
using namespace std;  // since cin and cout are both in namespace std, this saves some text
void tidy_numbers(long bound_number, int case_number);

int main() {
  int t;
  long bound_number;
  cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
  for (int i = 0; i < t; ++i) {
    cin >> bound_number;  // read n and then m.
    tidy_numbers(bound_number,i);
  }
}

void tidy_numbers(long bound_number, int case_number){
    vector<int> digits;
    while (bound_number > 0){
        int digit = bound_number%10;
        bound_number /= 10;
        digits.push_back(digit);
    }
    
    if(digits.size()==1){
        cout << "Case #" << case_number+1 << ": " << digits.front()<< endl;
        return;
    }else{
        reverse(digits.begin(),digits.end());
        
        //go through from last digit
        for(int i = digits.size()-1; i >= 1; --i){
            //if number after is smaller than before, then change later number to 9, before number to current -1, and make anything after that to be 0
            
            if(digits[i-1] > digits[i]){
                digits[i-1]--;
                for(int j = i; j < digits.size();j++)
                    digits[j] = 9;
            }
        }
        
        
        //cut 0 from front
        if(digits.front() == 0)
            digits.erase(digits.begin());
        
        cout << "Case #" << case_number+1 << ": ";
        for(int i = 0; i < digits.size(); i++){
            cout<<digits[i];
        }
        cout<<endl;
    }
}