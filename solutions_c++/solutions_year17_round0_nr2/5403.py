#include <iostream>
#include <stdio.h>
#include <vector>
using namespace std;

int main() {
	// your code goes here
	int T,check,j;
	int n,i,a;
	std::vector<int> arr;

	scanf("%d", &T);
	for(j=1;j<=T;j++){
	    scanf("%d", &n);

	    for(i=n;i>0;i--){
	        a = i;
	        check = 0;
	        arr.push_back(a%10);
	        a = a/10;
	        while(a>0){
	            arr.push_back(a%10);
	            a = a/10;

	            if(arr.back()>arr.rbegin()[1]){
	                check = 1;
	                break;
	            }
	        }
	        if(check==0){
	            break;
	        }
	    }
	    printf("Case #%d: %d\n",j,i);
	}
	return 0;
}
