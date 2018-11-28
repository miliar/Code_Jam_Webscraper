#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <climits>
#include <cstring>
#include <string>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <vector>
#include <list>
using namespace std;
int T=0;
string N;
int a[20];
int main(){
	//freopen("B-small-attempt0.in","r",stdin);  
	freopen("B-large.in","r",stdin);  
	//freopen("out0.txt","w",stdout); 
	freopen("out0-large.txt","w",stdout); 
	scanf("%d",&T);
	
	for(int i=1; i<=T; i++){

		cin>>N;
		for(int b=0; b<20; b++){
			a[b] = 0;
		}
		int j=0;
		while(N[j]!='\0'){
			j++;
		}
		for(int b=0; b<j; b++){
			a[b] = N[j-1-b] - '0';
			//printf("a[%d]=%d\n",b,a[b]);
		}

		int k = j-1;
		while(k>=1){
			if(a[k]<=a[k-1]){
				k--;
				continue;
			}else{
				break;
			}
		}
		k--;
		//printf("k=%d\n",k);
		if(k!=-1){
			for(int b=k-1; b>=0; b--){
				a[b] = 9;
			}
			for(int b=k; b<j-1; b++){
				while(a[b+1]>a[b]){
					a[b+1]--;
					a[b] = 9;
				}
			}
		}

		
		printf("Case #%d: ", i);
		int sign = 0;
		for(int b=19; b>=0; b--){
			if(a[b]==0 && sign==0)
				continue;
			else
				sign = 1;
			printf("%d",a[b]);
		}
		printf("\n");
	}

	return 0;
}