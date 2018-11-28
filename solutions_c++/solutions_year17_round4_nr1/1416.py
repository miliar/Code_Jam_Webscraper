#include <iostream>
#include <vector>  
#include <algorithm>
using namespace std; 
 
 
 
void main()  
{  
   int T;
   cin >> T;
   for (int i = 1; i <= T; i++){
	   int N, P;
       cin >> N >> P;
	   
	   vector<int> count(P, 0);
	   
	   for (int j = 1; j <= N; j++){
		   int num;
		   cin >> num;
		   count[num%P]++;
	   }
	   
	   int result = count[0];
	   
	   for (int j = 1; j <= P/2; j++){
		   if (j != P-j){
			   int min_count = min(count[j], count[P-j]);
			   result += min_count;
			   count[j] -= min_count; count[P-j] -= min_count;
		   }
		   else {
			   int min_count = floor(count[j]/2);
			   result += min_count;
			   count[j] -= 2 * min_count;
		   }
	   }

	   if (P > 3){
		   for (int j = 1; j < P; j+=2){
			   int min_count = min(int(floor(count[j]/2)), count[2]);
			   result += min_count;
			   count[j] -= 2 * min_count; count[2] -= min_count;
		   }
	   }
	   
	   for (int j = 1; j < P; j++){
		   result += floor(count[j]/P);
		   count[j] -= P * floor(count[j]/P); 
		   
	   }
	   
	   for (int j = 1; j < P; j++){
		 if (count[j] > 0){
			result ++;
			break;
		 }
	   }
	   
	   cout << "Case #" << i << ": " << result << endl;
   }
}  
