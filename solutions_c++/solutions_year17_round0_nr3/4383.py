#include <bits/stdc++.h>
using namespace std;

int main()
{
	freopen("C-small-2-attempt0.in","r",stdin);
	freopen("out.txt","w",stdout);
	int test,tc=1;
	cin >> test;
	while(test--) {
		long long int n,k;
		cin >> n >> k;
		priority_queue<long long int> q;
		q.push(n);
		for (int i=1;i<k;i++) {
			long long int temp = q.top();
			q.pop();
			if(temp/2 != 0) {
				q.push(temp/2);
			}
			long long int temp1 = temp-1-temp/2;
			if(temp1!=0) q.push(temp1);
		}
		long long int temp = q.top();
		printf("Case #%d: ",tc++);
		long long int maxx=max(temp/2,temp-temp/2-1);
		long long int minn = min(temp/2,temp-temp/2-1);
		cout << maxx << " " << minn << endl;
	}
	
}
