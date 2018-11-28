#include<iostream>
#include<queue>
#include<cmath>
using namespace std;
int main ()
{
	
	int t,k,n,temp;
	cin >> t;
	
	for (int i=0;i<t;i++)
	{	priority_queue<int> prio_queu;
		cin >> n >> k;
		prio_queu.push(n);
		for (int j=1;j<k;j++)
			{temp=prio_queu.top();
			prio_queu.pop();
			prio_queu.push(ceil((temp-1)/2.0));
			prio_queu.push(floor((temp-1)/2.0));
		}
		cout << "Case #"<<i+1 <<": "<< ceil((prio_queu.top()-1)/2.0)<<" "<<floor((prio_queu.top()-1)/2.0)<<endl;
	}
	
	
	return 0;
	
	}
