#include <iostream>
#include <string>
#include <stdio.h>
using namespace std;

int main() {
	// your code goes here
	int t,k,l,count,m,x,check;
	string str;

	scanf("%d",&t);

	for(int i=1;i<=t;i++){
	    cin >> str >> k;
	    l = str.size();

	    string cmp_str(l,'+');

	    count = 0;
	    check = 0;

	    while(cmp_str.compare(str) != 0){
	        for(m=0;m<l;m++){
	            if(str[m] == '-'){
	                if(m>(l-k)){
	                    printf("Case #%d: IMPOSSIBLE\n",i);
	                    check = 1;
	                    goto impossible;
	                }

	                for(x=m;x<m+k;x++){
	                    str[x] = str[x] == '-' ? '+' : '-';
	                }
	                count++;

	            }
	        }

	    }
	    impossible:
	    if(check == 0){
	        printf("Case #%d: %d\n",i,count);
	    }
	}

	return 0;
}
