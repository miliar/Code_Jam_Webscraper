#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main() {
	int numCases;
	scanf("%d", &numCases);
	
	long long n;
	
	char arr[1024];
	for (int i = 0 ; i < numCases ; ++i) {
	    scanf("%lld", &n);
	    
	    int arrLen = 0;
	    while(n > 0) {
	        arr[arrLen] = n % 10L;
	        n /= 10L;
	        ++arrLen;
	    }
	    
	    for (int j = arrLen - 1 ; j > 0 ; --j) {
	        if (arr[j] == 0) continue;
	        
	        for (int k = j - 1 ; k >= 0 ; --k) {
	            if (arr[j] > arr[k]) {
	                for (int m = k ; m >= 0 ; --m) {
	                    arr[m] = 9;
	                }
	                --arr[k+1];
	                ++j;
	                break;
	            }
	        }
	    }
	    
	    printf("Case #%d: ", i + 1);
	    int skip = 1;
	    for (int j = arrLen - 1 ; j >= 0 ; --j) {
	        if (skip == 1 && arr[j] == 0) continue;
	        skip = 0;
	        printf("%d", arr[j]);
	    }
	    printf("\n");
	}
	
	
	return 0;
}
