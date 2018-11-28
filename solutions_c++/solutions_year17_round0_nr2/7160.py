#include <iostream>
using namespace std;

long long int makeNumber(long long int arr[],long long int len){
	long long int result=0;
		for(int i=0;i<len;i++){
			result = result*10 + arr[i];
		}
	return result;
}

int main() {
	// your code goes here
	long long int t,n;
	cin>>t;
	
	long long int arr[20];
	for(int test=1;test<=t;test++){
		cin>>n;
		long long int len=0;
		long long int i=0;
		//cout<<"ayush "<<n<<endl;
		while(n>0){
			arr[i]=n%10;
			n=n/10;
			i++;
			len++;
		}
		
		i=0;
		long long int j=len-1,temp;
		while(i<=j){
			temp=arr[i];
			arr[i]=arr[j];
			arr[j]=temp;
			i++;
			j--;
		}
		//	cout<<"actuall Num : "<<makeNumber(arr,len)<<endl;
		bool good=false;
		while(!good){
			good=true;
			for(int i=0;i<len-1;i++){
				if(arr[i]>arr[i+1]){
					good=false;
					arr[i]=arr[i]-1;
					for(int j=i+1;j<len;j++)
						arr[j]=9;
				}
			}	
		//	cout<<makeNumber(arr,len)<<endl;
		}
		long long int result=makeNumber(arr,len);
	
	
		cout<<"Case #"<<test<<": "<<result<<endl;
	}
	
	
	return 0;
}