#include<bits/stdc++.h>
using namespace std;
int test;
int II()
{
int n;
scanf("%d",&n);
return n;
}
int main(){
	ifstream cin("C-small-1-attempt0 (1).in");
	ofstream cout("C-small-1-attempt0 (1).out");
cin>>test;
for(int num=0;num<test;num++){
	int n,k;
	double u;
	cin>>n>>k>>u;
	double v[n];
	priority_queue<double, vector<double>, greater<double> > min_heap;
	for(int i=0;i<n;i++){
	cin>>v[i];
	min_heap.push(v[i]);
	}
	
	while(u>0){
		double temp=min_heap.top();
		double cont=1;
		min_heap.pop();
		while(min_heap.size()>0&&min_heap.top()==temp){
			min_heap.pop();
			cont++;
		}
		
		//cout<<u<<" "<<temp<<" "<<cont<<endl;
		if(min_heap.size()==0){
		temp+=u/cont;
		u=0;
		}
		else{
			if((min_heap.top()-temp)*cont>u){
				temp+=u/cont;
				u=0;
			}
			else{
				
				u-=(min_heap.top()-temp)*cont;
				temp=min_heap.top();
			}
		}
		
		for(int j=0;j<cont;j++)
		min_heap.push(temp);
	}
	double ans=1;
	while(min_heap.size()>0){
		ans*=min_heap.top();
		min_heap.pop();
	}
	cout<<"Case #"<<num+1<<": "<<setprecision(19)<<ans<<endl;
	
	
}
return 0;
}

