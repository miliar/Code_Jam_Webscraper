#include <iostream>
#include <math.h>
#include <string> 

using namespace std;

int CharToDigit(char input) {
    return int(input - '0');
}

int main()
{
   int i, j, n_cases, left_index, new_val;
   string input, new_value;
   string extra="999999999999999999"; // MAX_DIGITS * '9'
   
   cin >> n_cases;
   cin.ignore();
   

   for (i=0; i<n_cases; i++) {
       
       getline(cin,input);
       
       left_index = input.length();
       new_val = CharToDigit(input[input.length()-1]);
       //cout << new_rightval;
       
       for (j=input.length()-2; j>=0; j--) {
           if (CharToDigit(input[j]) > new_val) {
               new_val = max(0, CharToDigit(input[j])-1);
               left_index = j;
           } else {
               new_val = CharToDigit(input[j]);
           }
       }
       
       new_value="";
       if (input.length() == 1) {
           new_value = input;
       }
       
       if (left_index == 0 && CharToDigit(input[left_index]) > 1) {
           new_val = CharToDigit(input[left_index]-1);
           new_value += char(new_val + '0');
       } 
       
       if (left_index > 0 && input.length() > 1) {
           new_value.append(input,0,left_index);
               if (left_index != input.length()) {
               new_val = CharToDigit(input[left_index]-1);
               if (new_val < 0) {
                   new_value += "9";
               } else {
                   new_value += char(new_val + '0');
               } 
           }
       }
       new_value.append(extra,0,max(0,int(input.length()-left_index-1)));

       cout << "Case #" << i+1 << ": " << new_value;
       
       if (i < n_cases-1) {
          cout << endl;
       }
   }
   return 0;
}