#include <bits/stdc++.h>
using namespace std;

int n, k, T;

int main()
{
	cin>>T;

for(int t = 1; t <= T; t++) 
{
	priority_queue<int> pq;

	cin>>n>>k;

	pq.push(n);

	for(int i=0;i<k-1;i++)
    {
        	int next = pq.top();

        	pq.pop();

            if(next%2!=0)
            {
                pq.push(next/2);
                pq.push(next/2);
            }
            if(next%2==0)
            {
                pq.push(next/2);
                pq.push(next/2 - 1);                  
            }
       }

        int resp = pq.top();

        cout<<"Case #"<<t<<": ";

        if(resp%2!=0)
        {
            cout<<resp/2<<" "<<resp/2<<"\n";
        }
        else
        {
            cout<<resp/2<<" "<<resp/2 - 1<<"\n";
        }
    }
}