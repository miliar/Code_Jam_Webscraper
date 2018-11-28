#include <iostream>
#include<math.h>

using namespace std;

int main() {
	// your code goes here
	
	int t;
	cin>>t;
	
	for(int a =0; a < t; a++)
	{
		long long n;
		cin>>n;
	
		int x = log10(n)+1;
	
		int arr[x];
	
	
		for(int i =0 ; i < x; i++)
		{
		
			arr[i] = n%10;
			n=n/10;
	
		}
	
		for(int i =0; i < x-1; i++)
		{
			if(arr[i+1] > arr[i]){
				
				arr[i+1] -= 1;
				for(int j = 0; j < i+1; j++)
				{
					arr[j] = 9;
				}	
			}
		}
	
		long long m = 0;
		int z =1;
	
		for(int i = 0; i < x; i++)
		{
			m += arr[i]*z;
			z*=10;
		}
	
		cout<<"Case #"<<a+1<<": "<<m<<endl;
	}
	
	return 0;
}