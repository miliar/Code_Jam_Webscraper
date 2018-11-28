#include<bits/stdc++.h>
#include<vector>

using namespace std;

long long int change(int*arr, int i, int n){
	for(int j=n-1;j>=0;j--){
		if(j==i){
			arr[j] = (arr[j]-1)%10;
			break;
		}
		else if(j>i){
			arr[j] = 9;
		}
	}
}

int numDigits(long long int n)
{
    int digits = 0;
    while (n) {
        n /= 10;
        digits++;
    }
    return digits;
}

long long int tidyNum(long long int n){
	int i = 0;
	int arr[20];
	int d = numDigits(n);
	for(int i=d-1;i>=0;i--){
		arr[i]=n%10;
		n=n/10;
	}
	
//	for(int i=0;i<d;i++){
//		cout<<arr[i]<<" ";
//	}
//	cout<<endl;
	
	for(int i=d-1;i>0;i--){
		if(arr[i]<arr[i-1]){
			change(arr,i-1,d);
		}
	}
	int flag = 0;
	for(int i=0;i<d;i++){
		if(arr[i]!=0){
			flag=1;
		}
		if(flag==1)
		cout<<arr[i];
	}
	cout<<endl;
	
}

int main(){
	freopen("input_file2.in","r",stdin);
	freopen("output_file2.out","w",stdout);
	int t;
	cin>>t;
	for(int i=1;i<=t;i++){
		long long int n;
		cin>>n;
		cout<<"Case #"<<i<<": ";
		tidyNum(n);
	}
}
