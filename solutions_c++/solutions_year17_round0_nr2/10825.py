// Majok Ring

#include <stdlib.h>
#include <iostream>
#include <string>
#include <vector>
#include <sstream>
using namespace std;


int lastTidy(int input)
{

stringstream ss; 
ss << input << endl;
string numString = ss.str();


if(input >= 0 && input <= 9)
    return input;

int size = numString.size();
int numComparisons = 0;

int i = 0;
int j = 1;

int num1;
int num2;

string snum1 = numString.substr(i, 1);
string snum2 = numString.substr(j, 1);

istringstream ( snum1 ) >> num1;
istringstream ( snum2 ) >> num2;


while(num1 <= num2)
{



 snum1 = numString.substr(i, 1);
 snum2 = numString.substr(j, 1);

istringstream ( snum1 ) >> num1;
istringstream ( snum2 ) >> num2;



i++;
j++;
numComparisons++;


    if(numComparisons == (size - 1))
    {
       // cout << "ANSWER: " << input << endl;
        return input;
    }




}




    
    return -1;
}


int main() {

int numCases;
cin >> numCases;

int caseNum = 1;





while(numCases != 0)
{
    int input;
    cin >> input;
    int output = lastTidy(input);

    while(output == -1)
       {
           input--;
           output = lastTidy(input);
          // cout << input << endl;
       }

   cout <<  "Case #"<< caseNum <<": " << output << endl;
    numCases--;
    caseNum++;
}

  return 0;
}