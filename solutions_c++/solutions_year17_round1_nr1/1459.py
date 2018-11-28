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

int ctoi(){
	char c;
	while(c=getchar(),(c<'0'||c>'9')&&(c!='-'));
	bool flag=(c=='-');
	if(flag)
		c=getchar();
	int x=0;
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
	int t=ctoi();

	for(int tt=1;tt<=t;tt++){
		printf("Case #%d:\n",tt);
		int r =ctoi();
		int c=ctoi();
		char str[r][c];
		for(int i=0;i<r;i++){
			scanf("%s",str[i]);
		}
//		for(int i=0;i<r;i++){
//			for(int j=0;j<c;j++){
//				cout<<str[i][j];
//			}
//			cout<<endl;
//		}


		for(int i=0;i<r;i++){
			for(int j=1;j<c;j++){
				if(str[i][j]=='?'){
					str[i][j]=str[i][j-1];
				}
			}
			for(int j=c-2;j>=0;j--){
				if(str[i][j]=='?'){
					str[i][j]=str[i][j+1];
				}
			}
		}

		for(int j=0;j<c;j++){
			for(int i=1;i<r;i++){
				if(str[i][j]=='?'){
					str[i][j]=str[i-1][j];
				}
			}
			for(int i=r-2;i>=0;i--){
				if(str[i][j]=='?'){
					str[i][j]=str[i+1][j];
				}
			}
		}

		for(int i=0;i<r;i++){
			for(int j=0;j<c;j++){
				cout<<str[i][j];
			}
			cout<<endl;
		}
	}
	return 0;
}
