#include<iostream>
#include<string>
#include<cstdio>
#include<cstring>
#include<vector>
#include<math.h>
#include<map>
#include<queue> 
#include<algorithm>
using namespace std;
const int inf = 0x3f3f3f3f;
struct node {
	int cost;
	string s;
	node (){}
	node (string s_,int cost_){
		s=s_;
		cost=cost_;
	}
};
string s;
int num;
bool judge(string s){
	for (int i=0;i<s.length();i++){
		if (s[i]=='-') return false;
	}
	return true;
}

int main ()
{
	
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int t;
	cin>>t; 
	int cnt=1;
	while (t--){
		cin>>s>>num;
		int ans=0;
		for (int i=s.length()-1;i>=num-1;i--){
			if (s[i]=='+')continue;
			ans++;
			for (int j=i;j>i-num;j--){
				if (s[j]=='+')s[j]='-';
				else s[j]='+';
			}
			//cout<<s<<endl;
		}
		int flag=1;
		for (int i=0;i<s.length();i++){
			if(s[i]=='-'){
				flag=0;
				break;
			} 
		}
		if (flag){ 
			cout<<"Case #"<<cnt++<<": "<<ans<<endl;
		}
		else cout<<"Case #"<<cnt++<<": IMPOSSIBLE"<<endl;
	}	
	return 0;
}
