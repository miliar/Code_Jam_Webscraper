#include<iostream>
#include<fstream>
using namespace std;
bool finished(string s){
	int i;
	int len=s.length();
	for (i=0;i<len;i++){
		if (s[i]=='-') return false;
	}
	return true;
}
int main(){
	ifstream in("Q1.in");
	ofstream out("Q1.out");
	int n,i,j,k,lf,len,ans;
	string s;
	in>>n;
	bool flag;
	for (i=1;i<=n;i++){
		in>>s;
		in>>lf;
		len=s.length();
		ans=0; 
		out<<"Case #"<<i<<": ";
		flag=false; 
		for (j=0;j<len-lf+1;j++){
			if (finished(s)) {
				out<<ans<<endl;
				flag=true;
				break;
			}
			if (s[j]=='+') continue;
			for (k=j;k<j+lf;k++) {
				if (s[k]=='-') s[k]='+'; else s[k]='-';
			}
			ans++;
		}
		if (flag==false) {
			if (finished(s)) {out<<ans<<endl;} 
			else {out<<"IMPOSSIBLE"<<endl;}
		} 
	}
}
