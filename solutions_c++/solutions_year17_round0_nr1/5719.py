#include <iostream>
#include <stdlib.h>
#include <math.h>
#include <string>

using namespace std;

int main(){
	int i,j,k,l;
	string str;
	int K, T;
	int *a;
	cin>>T;
	for(l = 0 ; l < T ; l++){
		cout<<"Case #"<<l+1<<": ";
		cin>>str>>K;
		int N = str.length();
		a = new int[str.length()];
		for(i = 0 ; i < str.length() ; i++)
		{
			if(str[i] == '+')
				a[i] = 1;
			else
				a[i] = 0;
		}
		
		int count = 0;
		for(i = 0 ; i <= N - K ; i++){
			if(a[i] == 1)
				continue;
			count++;
			for(j = 0 ; j < K ; j++)
				a[i+j] = (a[i+j] + 1)%2;
			
		}
		
		for(i = 0 ; i < N ; i++){
			if(a[i] == 0)
				break;
		}
		if(i != N)
			cout<<"IMPOSSIBLE"<<"\n";
		else{
			cout<<count<<"\n";
		}		 
		delete[] a;
	}
	return 0;	
}
