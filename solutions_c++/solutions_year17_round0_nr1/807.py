#include <cstdio>
#include <cstring>
#include <vector>
#include <queue>
#include <string>
#include <algorithm>
#include <iostream>
#include <string>
#include <map>
#include <set>
#include <functional>
#include <iostream>
#define MOD 1000000007LL
using namespace std;
typedef long long ll;
typedef pair<int,int> P;

int t,k;
string str;
int fie[1401];

int main(void){
	scanf("%d",&t);
	for(int i=0;i<t;i++){
		cin >> str;
		int n=str.size();
		scanf("%d",&k);
		for(int j=0;j<n;j++){
			if(str[j]=='+')fie[j]=1;
			else fie[j]=0;
		}
		int cnt=0;
		for(int j=0;j<=n-k;j++){
			if(fie[j]==0){
				for(int l=0;l<k;l++){
					fie[j+l]=1-fie[j+l];
				}
				cnt++;
			}
		}
		bool flag=true;
		for(int j=0;j<n;j++){
			if(fie[j]==0)flag=false;
		}
		if(!flag){
			printf("Case #%d: IMPOSSIBLE\n",i+1);
		}else{
			printf("Case #%d: %d\n",i+1,cnt);
		}
	}
	return 0;
}
