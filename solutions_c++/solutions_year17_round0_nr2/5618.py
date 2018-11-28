#include <iostream>
#include <string>

using namespace std;

int main() {

   int i=1, T;
   string line;

   cin >> T;
   cin.ignore();

   while (getline(cin, line)) {
      cout << "Case #" << i << ": ";
      if (line.length() != 1) {
         for (int j=line.length()-1; j>0; j--) {
            if (line[j] == '0') {
               long long num = stoll(line.substr(0, j + 1)) - 1;
               line = to_string(num) + string(line.length() - j - 1, '9');
            } else if (line[j] < line[j-1]) {
               long long num = stoll(line.substr(0, j)) - 1;
               line = to_string(num) + string(line.length() - j, '9');
            }
         }
      }

      cout << line << endl;
      i++;
   }

   return 0;
}