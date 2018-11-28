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

int r,c;
string str[30];
bool flag[31];

void solve(int ta){
	for(int i=0;i<c;i++){
		char g='?';
		flag[i]=false;
		for(int j=0;j<r;j++){
			if(g=='?'){
				if(str[j][i]!='?'){
					g=str[j][i];
					flag[i]=true;
				}
			}else{
				if(str[j][i]=='?'){
					str[j][i]=g;
				}else{
					g=str[j][i];
				}
			}
		}
		g='?';
		for(int j=r-1;j>=0;j--){
			if(g=='?'){
				if(str[j][i]!='?'){
					g=str[j][i];
					flag[i]=true;
				}
			}else{
				if(str[j][i]=='?'){
					str[j][i]=g;
				}else{
					g=str[j][i];
				}
			}
		}
	}
	int pr=-1;
	for(int i=0;i<c;i++){
		if(pr==-1){
			if(flag[i]){
				pr=i;
			}
		}else{
			if(!flag[i]){
				flag[i]=true;
				for(int j=0;j<r;j++){
					str[j][i]=str[j][pr];
				}
			}else{
				pr=i;
			}
		}
	}
	for(int i=c-1;i>=0;i--){
		if(pr==-1){
			if(flag[i]){
				pr=i;
			}
		}else{
			if(!flag[i]){
				flag[i]=true;
				for(int j=0;j<r;j++){
					str[j][i]=str[j][pr];
				}
			}else{
				pr=i;
			}
		}
	}
	printf("Case #%d:\n",ta);
	for(int i=0;i<r;i++){
		cout << str[i] << endl;
	}
}

int main(void){
	int t;
	scanf("%d",&t);
	for(int i=0;i<t;i++){
		scanf("%d%d",&r,&c);
		for(int j=0;j<r;j++){
			cin >> str[j];
		}
		solve(i+1);
	}
	return 0;
}
