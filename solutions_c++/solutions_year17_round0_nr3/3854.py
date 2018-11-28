#include <iostream>
#include <queue>
using namespace std;

int main(){
	priority_queue<long long int> mypq;
	long long int i,j,x,N,k,min1,max1;
	int test,t;
	cin>>test;
	t =1;
	while(test--){
		cin>>N>>k;
		while(!mypq.empty()){
			mypq.pop();
		}
		mypq.push(N);
		for(i = 0;i<k;i++){
			x = mypq.top();
			min1 = (x-1)/2;
			max1 = x/2;
			mypq.pop();
			mypq.push(min1);
			mypq.push(max1);
		}
		cout<<"Case #"<<t++<<": ";
		cout<<max1<<" "<<min1<<endl;
	}
	return 0;
}