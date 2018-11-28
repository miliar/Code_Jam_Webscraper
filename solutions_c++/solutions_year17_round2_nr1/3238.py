#include <iostream>
#include <queue>
using namespace std;
int main()
{
	int f;
	cin>>f;
	for(int i=1;i<=f;i++)
	{
		long int totaldis, horsenum ; 
		cin>>totaldis>>horsenum;
		priority_queue<double> pq;
		while(horsenum--){
			long int kpos, speedhorse;
			cin>>kpos>>speedhorse;
			pq.push((double)(totaldis - kpos)/speedhorse);
		}
		//Case #1: 101.000000
		cout<<"Case #"<<i<<": "<<fixed<<totaldis/pq.top()<<endl;
	}
}