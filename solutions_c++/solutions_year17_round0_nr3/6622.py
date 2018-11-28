#include<bits/stdc++.h>
long long int arr[1000000];
int main(){
	freopen( "input.txt", "r", stdin );
	freopen( "output.txt", "w", stdout );
	int t,check=0;
std::cin>>t;
int l=t;

while(l--){
	for(int i=0;i<1000000;i++)
		arr[i]=0;
	check++;
	long long int n,k,q=1,w=0;
	std::cin>>n>>k;
	long long int x=k;
	arr[0]=n;
	while(k--){
		sort(arr+w,arr+q,std::greater<long long>());
		long long a1=arr[w]/2;
		arr[q++]=a1;
		if(arr[w]%2==0)
			arr[q++]=a1-1;
		else
			arr[q++]=a1;
		w++;
	}
	int y=t-l;
	std::cout<<"Case #"<<y<<": "<<arr[q-2]<<" "<<arr[q-1]<<"\n";
}
}
