#include <string>
#include <vector>
#include <limits>
#include <cstring>
#include <iostream>

using namespace std;
    
int main(){
    int t;
    string input;
    cin >> t;
	std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
    for (int i = 0; i < t; i++) {
	   getline (cin, input);
	   for (int j = (int)input.length() - 2; j >= 0; j--) {
		   if (input[j + 1] < input[j]) {
			   input[j]--;
			   input[j + 1] = input[j + 1] + 10;
		   }
	   }
	   for (int j = 0; j < (int)input.length(); j++) {
           if (input[j] > '9') {
			   input[j] = '9';
               input[j+1] = input[j+1] + 10;
           }
	   }
    long long int i_dec = stoll (input,nullptr);
    cout << "Case #" << i+1 << ": " << i_dec << endl;   }
   return 0;
}
