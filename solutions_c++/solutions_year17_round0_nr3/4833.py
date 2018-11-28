#include <iostream>
#include <queue>
#include <vector>
using namespace std;


int main()
{

	//priority_queue<int> pq;
	int number,i,pos,n,j;
	int t1,t2,t3;
	
	cin>>n;

for(j=1;j<=n;j++)
{
	priority_queue<int> pq;
	cin>>number>>pos;
	pq.push(number);
	
	i=0;
	while(pq.empty()==false)
	{	
		t1=pq.top();
		pq.pop();
		t1-=1;
		t2=t1/2;
		t3=t1-t2;

		i++;
		if(i==pos) break;
		
		if(t2>0) pq.push(t2); 
		if(t3>0) pq.push(t3);
	}

	cout<<"Case #"<<j<< ": "<<t3<<" "<<t2<<endl;
}		

}
