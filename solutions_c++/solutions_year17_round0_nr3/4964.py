#include<iostream>
#include<inttypes.h>
#include<algorithm>
#include<queue>
#include<vector>

using namespace std;
struct comparator {
 bool operator()(uint64_t i,uint64_t j) {
 return i < j;
 }
};
int main(){
	int t;
	cin>>t;
	for(int g=1;g<=t;g++){
		priority_queue< uint64_t , vector< uint64_t > , comparator > hp;
		cout<<"Case #"<<g<<": ";
		uint64_t n,k,i,temp;
		cin>>n>>k;
		hp.push(n);
		for(i=0;i<k-1;i++){
			temp = hp.top();
			hp.pop();
			if(temp&1){
				hp.push((temp-1)/2);
				hp.push((temp-1)/2);
			}else{
				hp.push(temp/2);
				hp.push((temp-2)/2);
			}
		}
		temp = hp.top();
		if(temp&1){
			cout<<((temp-1)/2)<<" "<<((temp-1)/2);
		}else{
			cout<<((temp)/2)<<" "<<((temp-2)/2);
		}
		cout<<endl;
	}
	return 0;
}
