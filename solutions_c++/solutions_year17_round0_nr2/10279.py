#include <cstdio>
#include <iostream>
#include <ctime>
#include <iomanip>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <cstring>
using namespace std;
int T;
int test;
int main() { 
	scanf("%d",&test);
	for(int i=1;i<=test;i++){
		scanf("%d",&T);
		printf("Case #%d: ",i);
		for(int j=T;j>0;j--){
			int m=5;
			int a=11;
			int c=j;
			while(c>0){
				int b=a;
				a=c%10;
				c=c/10;
				if(a>b) break;
				if(c==0){
					printf("%d\n", j);
					m=99;
					break;
				}
			}
			if(m==99) break;
		}
	}

		
		
		
		
		

	return 0;
}	