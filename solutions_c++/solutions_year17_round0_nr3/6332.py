#include <iostream>
#include <map>  
using namespace std; 
 
void solve(long long int N, long long int K){
	map<long long int, long long int> intervals;
	intervals[N] = 1;
	   
	long long int left, right;
	for (int i = 0; i < K; i++){
	   long long int largest = intervals.rbegin()->first;
	   intervals[largest]--;
	   if (intervals[largest] == 0)
		   intervals.erase(largest);
	   left = floor((largest-1)/2);
	   right = largest - 1 - left;
	   map<long long int, long long int>::iterator it_left = intervals.find(left);
	   if (it_left == intervals.end())
		   intervals[left] = 1;
	   else
		   it_left->second++;
	   map<long long int, long long int>::iterator it_right = intervals.find(right);
	   if (it_right == intervals.end())
		   intervals[right] = 1;
	   else 
		   it_right->second++;
	}
	cout << "Case #" << i << ": " << right << " " << left << endl;
}
 
void main()  
{  
   int T;
   cin >> T;
   for (int i = 1; i <= T; i++){
	   long long int N, K;
	   cin >> N >> K;
	   solve(N, K);
   }
}  
