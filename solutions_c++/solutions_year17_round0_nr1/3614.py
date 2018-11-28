//#define LOCAL
#include<iostream>
using namespace std; 
int main()
{
	#ifdef LOCAL
	freopen("A-large.in.txt","r",stdin);
	freopen("A-large.out","w",stdout);
	#endif
	int t;
	cin>>t;
	for(int i=0;i<t;i++)
	{
		char pancakes[1001];
		int k;
		cin>>pancakes>>k;
		int start = -1;
		int downCount = 0, flipCount = 0, iter = 0, length=0;
		while (pancakes[iter]){
			if(pancakes[iter]=='-'){
				if(start==-1)start=iter;//intialize start position
				downCount++;//count blank num
			}
			iter++;
		}
		length=iter;
		cout<<"Case #"<<i+1<<": ";
		if(downCount%2==1 && k%2==0){
			cout<<"IMPOSSIBLE"<<endl;
			continue;
		}
		while(downCount!=0 && start<=length-k){
			//flip
			int oldstart=start;
			iter=start;
			while(iter<oldstart+k){
				if(pancakes[iter]=='-'){
					pancakes[iter]='+';
					downCount--;
				}
				else{
					pancakes[iter]='-';
					downCount++;
					if(start==oldstart)start=iter;//update start to first -
				}
				iter++;
			}
			flipCount++;
			//find start if all +
			while(start==oldstart){
				if(pancakes[iter]=='-') start=iter;
				iter++;
			}
		}
		if(downCount==0){
			cout<<flipCount<<endl;
		}
		else if(start>length-k){
			cout<<"IMPOSSIBLE"<<endl;
		}		
	}
	return 0;
}
