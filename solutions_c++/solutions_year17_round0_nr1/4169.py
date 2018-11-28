#include <stdio.h>
#include <assert.h>
#include <iostream>     // std::cout
#include <algorithm>    // std::binary_search, std::sort
#include <vector>       // std::vector
#include <list>       // std::list
#include <string>

// int main(){
//   FILE *fr, *fw;
//   int N, K, i;
//   fr = fopen("A-small-attempt1.in", "r");
//   fw = fopen("output.txt", "w");
//   assert(1 == fscanf(fr, "%d", &N));
//   for(i=0; i<N; i++){
//       char current(100,' ');
//       fscanf(fr, "%s %d", &current[0], &K);
//       bool side = true; // true => not negated
//       int flip = 0;
//       int side_change = -K-1;
//       std::cout << "/* message */"<< current << "length: "<<current.length()<<" K "<< K << '\n';
//       for(int j = 0; j<current.length()-K+1;++j){
//         if(side_change + K >= j) side = true;
//         if(current[j] == '-' && side){
//           flip++;
//           side = !side;
//           side_change = j;
//         }else if(current[j] == '+' && !side){
//           flip++;
//           side = !side;
//           side_change = j;
//         }
//       }
//       bool impossible = false;
//       for(int j = current.length()-K+1; j<current.length();++j){
//         if(side_change + K >= j) side = !side;
//         if(current[j] == '-' && side){
//           impossible = true;
//         }else if(current[j] == '+' && !side){
//           impossible = true;
//         }
//       }
//       fprintf(fw, "Case #%d: ",i+1);
//       if(impossible)fprintf(fw, "IMPOSSIBLE\n");
//       else fprintf(fw, "%d\n",flip);
//
//   }
//
//   fclose(fr);
//   fclose(fw);
//   return 0;
//
// }


#include <iostream>  // includes cin to read from stdin and cout to write to stdout
using namespace std;  // since cin and cout are both in namespace std, this saves some text
int main() {
  int t, k;
  string current;
  cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
  for (int i = 1; i <= t; ++i) {
    cin >> current >> k;  // read n and then m.

    bool side = true; // true => not negated
    int flip = 0;
    int side_change = -k-1;
    std::cerr << "/* message */"<< current << "length: "<<current.length()<<" k "<< k << '\n';
    for(int j = 0; j<current.length()-k+1;++j){
      if(current[j] == '-'){
        flip++;
        for(int l = j;l<j+k;++l){
          if(current[l] == '-')current[l]='+';
          else current[l]='-';
        }
      }
    }
    bool impossible = false;
    for(int j = current.length()-k+1; j<current.length();++j){
      if(current[j] == '-'){
        impossible = true;
      }
    }
    // impossible = false;

    cout << "Case #" << i << ": ";
    if(impossible) cout << "IMPOSSIBLE" << endl;
    else cout<< flip << endl;

    // cout knows that n + m and n * m are ints, and prints them accordingly.
    // It also knows "Case #", ": ", and " " are strings and that endl ends the line.
  }
  return 0;
}
