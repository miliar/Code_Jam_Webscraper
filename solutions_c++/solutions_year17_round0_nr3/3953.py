#include <algorithm>
#include <iostream>
#include <istream>
#include <iterator>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <streambuf>
#include <string>
#include <vector>

using namespace std;

int main(){
	
	int i, j, t, T, N, K;
	string S;
	int maxLR, minLR;

	cin>>T;
	for(t=1; t<=T; t++){
		cin>>N>>K;

		priority_queue<int> nQueue;
		nQueue.push(N);
		for(i=0; i<K; i++){
			int n = nQueue.top();
			nQueue.pop();

			if(n%2==0){
				maxLR = n/2 - 1;
				minLR = n - n/2;
				
			}else{
				maxLR = (n+1)/2 - 1;
				minLR = n - (n+1)/2;
				
			}

			if(maxLR < minLR){
				int temp = maxLR;
				maxLR = minLR;
				minLR = temp;
			}

			nQueue.push(maxLR);
			nQueue.push(minLR);
			
			//sort(nQueue.begin(), nQueue.begin()+K-i, std::greater<int>());
			
		}

		// Print output
		cout<<"Case #"<<t<<": "<<maxLR<<" "<<minLR<<endl;
		
	}
	
	return 0;
}