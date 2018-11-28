#include <fstream>
#include <iostream>

using namespace std;

typedef struct {
   int min;
   int max;
} MinMax;


void update_closest_farthest(int *lefts, int *rights, int *closest, int *farthest, int n) {

   for (int a = 0; a < n; a++) {
      if (lefts[a] < rights[a]) {
         closest[a] = lefts[a];
         farthest[a] = rights[a];
      }
      else {
         closest[a] = rights[a];
         farthest[a] = lefts[a];
      }
   }
}


MinMax get_last_min_max(int n, int k) {

   int * people;
   int * lefts;
   int * rights;
   int * closest_neighbor;
   int * farthest_neighbor;
   MinMax final_min_max;
   final_min_max.min = 0;
   final_min_max.max = 0;
   int current_pos;

   //early exit cases 
   if (n == k) {
      return final_min_max;
   }

   //if early exit cases don't apply, run this
   people = new int[n];
   lefts = new int[n];
   rights = new int[n];
   closest_neighbor = new int[n];
   farthest_neighbor = new int[n];

   //fill in initial people 
   for (int i = 0; i < n; i++) {
      people[i] = 0;
   }

   //fill in initial Ls
   for (int a = 0; a < n; a++) {
      lefts[a] = a;
   }

   //fill in initial Rs
   for (int b = 0; b < n; b++) {
      rights[n - (1+b)] = b;
   } 

   int num_left_spaces = 0;
   int num_right_spaces = 0;

   //update L and R for each person who enters up until kth person
   for (int c = 0; c < k; c++) {
      update_closest_farthest(lefts, rights, closest_neighbor, farthest_neighbor, n);
      //find farthest closest neighbor
      //find first empty stall
      for (int i = 0; i < n; i++) {
         if (people[i] != 1) {
            current_pos = i;
            break;
         }
      }
      for (int d = current_pos+1; d < n; d++) {
         //don't include stalls that already have someone 
         if (people[d] == 1) {
            continue;
         }
         else if (closest_neighbor[d] > closest_neighbor[current_pos]) {
            current_pos = d;
         }
         else if (closest_neighbor[d] == closest_neighbor[current_pos]) {
            if (farthest_neighbor[d] > farthest_neighbor[current_pos]) {
               current_pos = d;
            }
         }
      } // end for loop through each element in n array
      people[current_pos] = 1;
      //update R array
      num_left_spaces = 0;
      for (int e = 1; e <= current_pos; e++) {
         if (people[current_pos - e] == 1) {
            break;
         }
         rights[current_pos - e] = e - 1;
         num_left_spaces++;
      }
      //update L array
      num_right_spaces = 0;
      for (int f = 1; f <= ((n - 1) - current_pos); f++) {
         if (people[current_pos + f] == 1) {
            break;
         }
         lefts[current_pos + f] = f - 1;
         num_right_spaces++;
      }
   } // end each placement of k people
   // kth person was at current_pos
   if (num_left_spaces > num_right_spaces) {
      final_min_max.max = num_left_spaces;
      final_min_max.min = num_right_spaces;
   }
   else {
      final_min_max.min = num_left_spaces;
      final_min_max.max = num_right_spaces;
   }

   delete [] lefts;
   delete [] rights;
   delete [] people;
   delete [] closest_neighbor;
   delete [] farthest_neighbor;

   return final_min_max;

}


int main() {

   ifstream input_file;
   ofstream output_file;

   int t;
   int n;
   int k;
   MinMax current_min_max;

   input_file.open("C-small-1-attempt1.in.txt");
   output_file.open("output-2.txt");

   if (!input_file.is_open()) {
      cout << "File could not be opened!\n" << endl;
   }
   else {
      input_file >> t;
      for (int a = 1; a <= t; a++) {
         input_file >> n >> k;
         output_file << "Case #" << a << ": ";
         current_min_max = get_last_min_max(n, k);
         output_file << current_min_max.max << " ";
         output_file << current_min_max.min;
         if (a < t) {
            output_file << endl;
         }
      }
   }

   input_file.close();
   output_file.close();

   return 0;
}
