#include<bits/stdc++.h>
using namespace std;
char ch[10000], ans[10000];
bool check(int len){
	for(int i = 1; i <= len; i++){
		if(ans[i] > ch[i])return 0;
		if(ans[i] < ch[i]) return 1;
	}
	return 1;
}
void work(int x, int len){
	if(x > len) return;
	for(char i = '9'; i >= '0'; i--){
		for(int j = x; j <= len; j++)
			ans[j] = i;
		if(check(len)){
			work(x+1, len);
			return;
		}
	}
	puts("ERROR");
}
int main(){
	freopen("B_large.in", "r", stdin);
	freopen("B_large.out", "w", stdout);
	int T;
	cin>>T;
	for(int ii = 1; ii <= T; ii++){
		scanf("%s",ch+1);
		int len = strlen(ch+1);
		work(1, len);
		bool flag = true;
		string str = "";
		for(int i = 1; i <= len; i++){
			if(ans[i] == '0'){
				if(!flag) str += ans[i];
			}else{
				flag = 0;
				str += ans[i];
			}
		}
		printf("Case #%d: ", ii);
		cout<<str<<endl;
	}
}
