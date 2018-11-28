#include <iostream>
#include <math.h>

#define MAX_LENGTH 1000

using namespace std;

int main()
{
   int i, j, n_cases, possible;
   int flip_sum, flip_size, total_flips, flipped[MAX_LENGTH];
   string data;
   
   cin >> n_cases;
   cin.ignore();
   for (i=0; i<n_cases; i++) {
       getline(cin, data, ' ');
       cin >> flip_size;
       cin.ignore();
       
       flipped[0] = (data[0]=='-');
       flip_sum = flipped[0];
       total_flips = flipped[0];

       for (j=1; j<data.length()-flip_size+1; j++) {
           flipped[j] = (flip_sum + (data[j]=='-')) %2;
           total_flips += flipped[j];
           
           flip_sum += flipped[j];
           if (j>=flip_size-1) {
                flip_sum -=  flipped[j-flip_size+1];
           }
       }
       
       possible = 1;
       for (j=data.length()-flip_size+1; j<data.length(); j++) {
           possible *= !((flip_sum + (data[j]=='-'))%2);
           if (j>=flip_size-1) {
                flip_sum -=  flipped[j-flip_size+1];
           }
       }
       
       cout << "Case #" << i+1 << ": ";
       if (possible) {
           cout << total_flips;
       } else {
           cout << "IMPOSSIBLE";
       }
       
       if (i < n_cases-1) {
           cout << endl;
       }
   }
   return 0;
}