#include <iostream>
#include <vector>  
using namespace std; 

void mem(vector<long long int>& ones){
	long long int result = 0;
	for (int i = 0; i <= 18; i++){
		ones.push_back(result);
		result = result * 10 + 1;
	}
}

long long int get_tidy(long long int N, vector<long long int>& ones){
	long long int so_far = 0;
	int digit = floor(log10(N)) + 1;
	while (digit > 0){
		int next_number = 9;
		while (so_far + next_number * ones[digit] > N){
			next_number--;
		}
		so_far += next_number * static_cast<long long int>(pow(10.0, digit-1));
		digit--;
	}
	return so_far;
}
 
void main()  
{  
   int T;
   cin >> T;
   vector<long long int> ones;
   mem(ones);
   for (int i = 1; i <= T; i++){
	   long long int N, result;
	   cin >> N;
	   result = get_tidy(N, ones);
	   cout << "Case #" << i << ": " << result << endl;
   }
}  
