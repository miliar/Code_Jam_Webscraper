#include <bits/stdc++.h>


using namespace std;


int main()
{
	int T;
	cin>>T;
	int t=T;
	while(t--) {
		int n, k;
		cin>>n>>k;

		priority_queue<int> pq;


		int i, temp, l,r;
		if(n%2==0) {
			r=n/2;
				l=r-1;
		}

		else {
			l=r=n/2;

		}

		pq.push(r);
		pq.push(l);
		i=1;

		while(i<k) {
			temp=pq.top();
			pq.pop();
			if(temp%2==0) {
				r=temp/2;
				l=r-1;
			}

			else {
				l=r=temp/2;
			}

			pq.push(r);
			pq.push(l);

			i++;
		}

		
		cout<<"Case #"<<T-t<<": "<<r<<" "<<l<<endl;
	}

	return 0;
}