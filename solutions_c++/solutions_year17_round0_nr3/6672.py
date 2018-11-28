#include <iostream>
#include <algorithm>
#include <cmath>
#include <vector>

using namespace std;

int indexes[2];
long k;

void findMaxGap(vector<bool> sequence){

	k=0;
	
	long count = 0;
	long maxCount = 0;
	
	indexes[0]=1;
	
	long j=0;
	
	while(sequence[j++] && (j<sequence.size()-1))
		
	
	
	while(j<sequence.size()-1){
		
		count = 0;	
		while(!sequence[j++]) 
			count++;
		
		if(count > maxCount){
			maxCount = count;
			indexes[0] = k;
			indexes[1] = j-1;
			
			//cout<<indexes[0]<<" "<<indexes[1]<<" "<<count<<endl;
		}
		
		k= j-1;
		
	}
	
}

int returnMiddle(int indexOne ,int indexTwo){
	
	long middle;

	if(!(int(indexOne + indexTwo) % 2))
		middle = ceil(float(indexOne + indexTwo)/2.0);
	else 
		middle = ceil(float(indexOne + indexTwo)/2.0) -1;
		
return middle;
}

int main() {

	int t;
	
	cin>>t;
	int testCount=1;
	
	for(int test = 0 ;test <t ;test++){
	
		long N,K;
		cin>>N>>K;
		
		vector<bool> sequence((N+2) ,0);
		
		//Not necessary but just in case
		sequence[0] = true;
		sequence[(N+2)-1] = true;
		
		
		long toLeft = 0;
		long toRight = (N+2)-1;
		
		long middle;
		
		
		while(K--){
		
			findMaxGap(sequence);
			sequence[returnMiddle(indexes[0] ,indexes[1])] = true;		
		}
		
		/*
		for(int i=0 ;i<sequence.size() ;i++)
			cout<<sequence[i]<<" ";
		*/
		
		middle = returnMiddle(indexes[0] ,indexes[1]);
		
		int j=middle-1 ,k =middle+1;
		
		long leftCount = 0,rightCount = 0;
		
		while((!sequence[j]) && j>=0)
			leftCount++ ,j--;
			
		while((!sequence[k]) && k<sequence.size())
			rightCount++ ,k++;
			
		cout<<"Case #"<<testCount++<<": "<<rightCount<<" "<<leftCount<<endl;
	}

return 0;
}
