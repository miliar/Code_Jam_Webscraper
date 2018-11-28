#include <fstream>
#include <iostream>

using namespace std;

// is_tidy returns 1 if x is tidy, and 0 if x is not tidy
int is_tidy(int x) {

   int last_digit;
   int second_to_last_digit;

   while (x >= 10) {
      last_digit = x % 10;
      x = x / 10;
      second_to_last_digit = x % 10;
      if (last_digit < second_to_last_digit) {
         return 0;
      }
   }
   return 1;

}


int determine_largest_tidy(int n) {

   while (n > 10) {

      if (is_tidy(n)) {
         return n;
      }
      else {
         n--;
      }

   }
   return n;

}


int main() {

   ifstream input_file;
   ofstream output_file;

   input_file.open("B-small-attempt0.in.txt");
   output_file.open("output.txt");

   int t;
   int n;
   int largest_tidy;

   if (!input_file.is_open()) {
      cout << "File could not be opened!\n" << endl;
   }
   else {
      input_file >> t;
      for (int a = 1; a <= t; a++) {
         output_file << "Case #" << a << ": ";
         input_file >> n;
         largest_tidy = determine_largest_tidy(n);
         output_file << largest_tidy;
         if (a < t) {
            output_file << endl;
         }
      }   

   }

   input_file.close();
   output_file.close();

   return 0;
}
