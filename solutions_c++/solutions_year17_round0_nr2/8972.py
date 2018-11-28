#include <iostream> 
#include <fstream>
#include <map>
#include <sstream>
#include <cmath>

using namespace std; 

bool areSorted(unsigned long long int n)
{
    // Note that digits are traversed from last to first
    int next_digit = n%10;
    n = n/10;
    while (n)
    {
        int digit = n%10;
        if (digit > next_digit)
            return false;
        next_digit = digit;
        n = n/10;
    }
 
    return true;
}

int main() { 
  unsigned long long int n;
  string s="";
  
  ifstream inFile("input.in");
  ofstream outFile("output.out");
  
  if(inFile.is_open()){
    getline(inFile,s);
    while(getline(inFile,s)){
      istringstream f(s);
      f >> n;
      unsigned long long int len = s.size()-1;
      
      //iterate through digits
      for(int i = len-1; i >= 0; i--){
        if(areSorted(n)) break;
        if(n%(unsigned long long int)pow(10,len-i-1) == 0){
          n = n - (unsigned long long int) pow(10,len-i-1);
        }
        while(n% (unsigned long)pow(10,len-i) < n%(unsigned long)pow(10,len-i+1)/10 || n%(unsigned long)pow(10,len-i+1)/10 ==0){
          n -= (unsigned long long int) pow(10,(len-i-1));
        }
      }
      cout << n << endl;

    }
  }
  inFile.close();
  outFile.close();
} 


