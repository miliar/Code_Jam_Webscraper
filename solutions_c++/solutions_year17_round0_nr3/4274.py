#include <iostream> 
#include <fstream> 
#include <cstdlib> 
#include <cmath> 
#include <queue> 
#include <cstring> 
#include <algorithm> 
using namespace std; 

int main(){
	int T; 
	cin >> T; 
	for (int test = 1; test <= T; test++){
		int N,K; 
		cin >> N >> K; 
		priority_queue<int> pq;  
		if (K == 1){
			cout << "Case #" << test << ": "; 
			if (N%2 == 0){
				cout << (N-1)-(N-1)/2 << " " << (N-1)/2 << endl; 
			}else if (N%2 == 1){
				cout << (N-1)/2 << " " << (N-1)/2 << endl; 
			}
		}else{
			if(N%2 == 0){
				pq.push((N-1)-(N-1)/2);  
				pq.push((N-1)/2); 
			}else if (N%2 == 1){	
				pq.push((N-1)/2); 
				pq.push((N-1)/2);  
			}
			for (int i = 2; i <= K; i++){
				int val = pq.top(); pq.pop();  
				if (i == K){
					if (val%2 == 0){
						cout << "Case #" << test << ": " << ((val-1)-(val-1)/2) << " " << ((val-1)/2) << endl; 
					}else if (val%2 == 1){
						cout << "Case #" << test << ": " << ((val-1)/2) << " " << ((val-1)/2) << endl; 
					}
					continue;  
				}	
				if (val%2 == 0){
					pq.push((val-1)-(val-1)/2);  
					pq.push((val-1)/2);  
				}else if (val%2 == 1){
					pq.push((val-1)/2);  
					pq.push((val-1)/2); 
				}
			}
		}
	}
	return 0;  
}