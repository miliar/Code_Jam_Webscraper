#include<iostream>
#include<math.h>
using namespace std;
long long int findMin(long long int n, long long int k) {
	if(k==1)
		return (n-1)/2;
	return (n-k)/(pow(2,((long long int)(log2(k)+1))));
}

long long int findMax(long long int n, long long int k) {
	if(k==1)
		return n/2;
	if(k%2){
		return findMin(n,k/2) /2;
	}
	else
		return findMax(n,k/2) /2;
}


int main()
{
	long long int n,k;
	int t;
	cin>>t;
for(int i=1; i<=t; ++i)
{
	long long int min, max;
	cin>>n>>k;
	min = findMin(n,k);
	max = findMax(n,k);
	cout<<"Case #"<<i<<": "<<max<<" "<<min<<endl;
}
}


