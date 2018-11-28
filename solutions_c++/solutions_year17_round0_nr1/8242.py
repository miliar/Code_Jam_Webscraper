#include<iostream>
#include<cstdio>
using namespace std;
char flipp(char ch){
	if (ch=='+') return '-';
	return '+';
}
int main(){
    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);
	int T;
	cin>>T;
	for (int t=1;t<=T;t++){
		string s;
		int n,cnt=0;
		cin>>s>>n;
		int num=(int)s.size();
		for (int i=0;i+n-1<num;i++){
			if (s[i]=='-'){
				cnt++;
				for (int j=i;j<i+n;j++)
				s[j]=flipp(s[j]);
			}
		}
		cerr<<s<<endl;;
		bool flag=true;
		for (int i=0;i<num;i++) if (s[i]=='-') flag=false;
		cout<<"Case #"<<t<<": ";
		if (flag) cout<<cnt<<endl;
		else cout<<"IMPOSSIBLE"<<endl;
	}
}
