#include <iostream>
#include <stdio.h>
using namespace std;

int main() {
	// your code goes here
	
	
	int test;
	long long num;
	cin>>test;
	int arr[20];
	
	for(int t=1;t<=test;t++){
	    cin>>num;
	    
	    int ind = 0;
	    while(num>0){
	        arr[ind] = num%10;
	        num = num/10;
	        ind++;
	    }
        int max = arr[ind-1];
        int i = ind -2;
	    for(;i>=0;i--){
	        if(arr[i]>=max)
                max = arr[i];
            else
                break;
            //cout<<arr[i];
	    }
        
        if(i>=0){
            for(int j = i;j>=0;j--)
                arr[j] = 9;
            i++;
            int val = arr[i];
            
            //cout<<val<<endl;
            while(i<ind && arr[i]==val){
                arr[i] = 9;
                i++;
            }
            i--;
            if(val==1){
                ind--;
            }else{
                arr[i] = val-1;
            }
            
                
        }
        i = ind-1;
        cout<<"Case #"<<t<<":"<<" ";
        for(;i>=0;i--)
            cout<<arr[i];
	    cout<<endl;
       
        
        
	}
	return 0;
}
