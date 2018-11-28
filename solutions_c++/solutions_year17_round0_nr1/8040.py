#include <iostream>
#include <vector>  
using namespace std; 
 
void main()  
{  
   int T;
   cin >> T;
   for (int i = 1; i <= T; i++){
	   vector<char> pancakes;
	   char c;
	   int K;
	   while ((c = getchar()) != ' ')
		   pancakes.push_back(c);
	   cin >> K;
	   int start = 0;
	   int count = 0;
	   while (start <= pancakes.size() - K){
		   if (pancakes[start] == '-'){
			   count++;
			   for (int j = start; j < start + K; j++){
				   if (pancakes[j] == '+')
					   pancakes[j] = '-';
				   else 
					   pancakes[j] = '+';
			   }
		   }
		   start++;
	   }
	   bool impossible = false;
	   for (int j = start; j < pancakes.size(); j++){
		   if (pancakes[j] == '-')
			   impossible = true;
	   }
	   if (impossible)
		   cout << "Case #" << i << ": IMPOSSIBLE" << endl;
	   else
		   cout << "Case #" << i << ": " << count << endl;
   }
}  
