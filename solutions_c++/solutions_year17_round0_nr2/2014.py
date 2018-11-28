#include <iostream>
#include<stdio.h>
#include<string.h>
using namespace std;
char c,arr[20];

int main() {
	// your code goes here
	int t,cs,K,ans;
	cs=0;
	scanf("%d",&t);
	while(t--){
	    cs++;
	    c= getchar();
	    while(c>'9' || c<'0')
	    c= getchar();
	    int len=0;
	    while(c>='0' && c<='9'){
	        arr[len]=c;
	        c= getchar();
            len++;
	    }
	    int j;
	    --len;
	    j=len;
	    while(arr[j]=='0'){
	        arr[j]='9';
	        j--;
	    }
	    if(j!=len)
	    arr[j]=arr[j]-1;
	    for(j=0;j<len;j++){
	        if(arr[j]>arr[j+1]){
	            arr[j]=arr[j]-1;
	            j++;
	            for(;j<=len;j++)
	            arr[j]='9';
	            j=-1;
	        }
	    }
	    j=0;
	    while(arr[j]=='0')
	    j++;
	    printf("Case #%d: ",cs);
	    for(;j<=len;j++){
	        printf("%c",arr[j]);
	    }
	    printf("\n");
	}
	return 0;
}

