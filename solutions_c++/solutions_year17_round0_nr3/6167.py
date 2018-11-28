#include <bits/stdc++.h>
using namespace std;

struct paired{
	long long n1;
	long long n2;
};

struct paired getHalved(long long n){
	struct paired result;
	if(n%2 == 1){
		result.n1 = n/2;
		result.n2 = n/2;
	}
	else{
		result.n1 = n/2;
		result.n2 = result.n1 - 1;
	}
	return result;
}

int main(int argc, char const *argv[])
{
	int t;
	cin>>t;
	for (int i = 0; i < t; ++i)
	{
		long long n,k;
		cin>>n>>k;
		priority_queue<int> q;
		q.push(n);
		for (int j = 0; j < k-1; ++j)
		{
			struct paired result = getHalved(q.top());
			q.pop();
			q.push(result.n1);
			q.push(result.n2);
		}
		struct paired result = getHalved(q.top());
		cout<<"Case #"<<i + 1<<": "<<max(result.n1,result.n2)<<" "<<min(result.n1,result.n2)<<endl;
	}
	return 0;
}