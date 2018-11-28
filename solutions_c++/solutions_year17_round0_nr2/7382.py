#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <iomanip>
#include <limits>
#include <map>
#include <math.h>
#include <set>
#include <sstream>
#include <utility>
#include <vector>
#include <queue>
#include <stack>
using namespace std;

long long ctoi(){
	char c;
	while(c=getchar(),(c<'0'||c>'9')&&(c!='-'));
	bool flag=(c=='-');
	if(flag)
		c=getchar();
	long long x=0;
	while(c>='0'&&c<='9'){
		x=x*10+c-48;
		c=getchar();
    }
	return flag?-x:x;
}
		
int main()
{
	freopen("input1.txt","r",stdin);
	freopen("output1.txt","w",stdout);
	long long t=ctoi();
//	printf("cases %lld\n",t);
	for(int tt=1;tt<=t;tt++){
		printf("Case #%d: ",tt);
		long long n = ctoi();
//		printf("number is %lld\n", n);
		long long temp=n;
		int dig=0;
		while(temp){
			dig++;
			temp/=10;
		}
//		printf("digits %d\n",dig);
		int arr[dig];
		for(int i=dig-1;i>=0;i--){
			arr[i]=(int)(n%10);
//			printf("storing %d\t%d\n",(int)(n%10),arr[i]);
			n/=10;
		}
//		for(int i=0;i<dig;i++){
//			printf("%d ",arr[i]);
//		}
//		printf("\n");
		for(int i=dig-1;i>0;i--){
			if(arr[i-1]>arr[i]){
//				printf("for i = %d -> arr[i] %d > arr[i-1] %d",i,arr[i],arr[i-1]);
				for(int j=i;j<dig;j++){
					arr[j]=9;
				}
				arr[i-1]--;
//				for(int i=0;i<dig;i++){
//					printf("%d",arr[i]);
//				}
//				printf("\n");
				continue;
			}
		}
//		printf("\n-----\n");
		for(int i=0;i<dig;i++){
			if(arr[i]!=0)	printf("%d",arr[i]);
		}
		printf("\n");
	}
	return 0;
}
