#include<iostream>
#include <fstream>
#include<queue>
using namespace std;


int main(){
	ofstream myfile;
  	myfile.open ("C-small-2.out");
	int t;
	cin>>t;
	for(int i=1;i<=t;i++){
		priority_queue<int> q;
		int n,k;
		cin>>n>>k;
		q.push(n);
		int j= 0;
		int x,y;
		while(j!=k){
			int u = q.top();
			q.pop();
			
			if(u%2==0){
				x = u/2;
				y = x-1;
			}
			else{
				x = u/2;
				y = x;
			}
			q.push(x);
			q.push(y);
			j++;
		}
		myfile<<"Case #"<<i<<": "<<x<<" "<<y<<endl;
		//cout<<"Case #"<<i<<": "<<x<<" "<<y<<endl;

	
		
	}
	
	
}

