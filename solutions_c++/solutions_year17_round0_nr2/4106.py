#include<iostream>
#include<string>
#include<cstdio>
#include<cstring>
#include<vector>
#include<math.h>
#include<map>
#include<queue> 
#include<algorithm>
#include<sstream> 
using namespace std;
const int inf = 0x3f3f3f3f;
long long n;
string s;
int judge[128];
int main ()
{
	int t;
	freopen("B-small-attempt11.in","r",stdin);
	freopen("B-small-attempt11.out","w",stdout);
	cin>>t;
	int cnt=1;
	while (t--){
		cin>>s;
		//cout<<s<<" ";
		int flag=1;
		int place;
		for (int i=1;i<s.length();i++){
			if (s[i]<s[i-1]){
				flag=0;
				place=i-1;
				break;
			}
		}
		if (flag){
			cout<<"Case #"<<cnt++<<": "<<s<<endl;
			continue;
		}
		//cout<<place<<endl; 
		memset(judge,0,sizeof (judge));
		char m=s[0];
		for (int i=place;i>=0;i--){
			if (i==place){
				s[i]-=1;
			}
			else if(s[i]>s[i+1]){
				s[i]-=1;
				s[i+1]='9';
			}
		}
		for (int i=place+1;i<s.length();i++){
			s[i]='9';
		}
		
		cout<<"Case #"<<cnt++<<": ";
		flag=1;
		for (int i=0;i<s.length();i++){
			if (flag&&s[i]=='0')continue;
			flag=0;
			cout<<s[i];
		}
		//cout<<" "<<s;
		cout<<endl;
	} 
	return 0;
}
