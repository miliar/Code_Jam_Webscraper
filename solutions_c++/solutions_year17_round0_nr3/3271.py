#include <iostream>
#include <queue>
#include <vector>

using namespace std;

int main(){
   int nTestCases, currTest = 1, max, min, n, k;
   int alreadyIn, maxEmpty;
   priority_queue<int> emptyStalls;

   cin >> nTestCases;
   while(currTest <= nTestCases){
      cin >> n >> k;
      emptyStalls.push(n);
      alreadyIn = 0;

      while(alreadyIn < k){
         alreadyIn++;
         maxEmpty = emptyStalls.top();
         emptyStalls.pop();
         // Even case
         if(maxEmpty%2 == 0){
            max = maxEmpty/2;
            min = max - 1;
         }
         // Odd case
         else {
            max = min = (maxEmpty - 1)/2;
         }
         emptyStalls.push(max);
         emptyStalls.push(min);
      }

      cout << "Case #" << currTest++ << ": "
           << max << " " << min << endl;

      emptyStalls = priority_queue<int>();
   }

   return 0;
}