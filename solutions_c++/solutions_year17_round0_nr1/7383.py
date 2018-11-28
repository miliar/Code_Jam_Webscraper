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
	for(int tt=1;tt<=t;tt++){
		printf("Case #%d: ",tt);
		char str[1000];
		scanf("%s",str);
		int k = ctoi();
		int len=strlen(str);
		int count=0;
		bool check=true;
		for(int i=0;i<=len-k;i++){
			if(i==len-k){
				bool one=false;
				bool all=true;
				for(int j=i;j<len;j++){
					if(str[j]=='+'){
						one=true;
					}
					if(str[j]=='-'){
						all=false;
					}
				}
				if(!all && one){
					printf("IMPOSSIBLE\n");
					check=false;
				}else if(!all){
					count++;
				}
			}else{
				if(str[i]=='-'){
					count++;
					for(int j=i;j<i+k;j++){
						if(str[j]=='+'){
							str[j]='-';
						}else{
							str[j]='+';
						}
					}
				}
			}
		}
		if(check){
			printf("%d\n",count);
		}
	}
	return 0;
}
