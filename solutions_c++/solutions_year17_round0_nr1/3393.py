#include<iostream>
#include<string>
using namespace std;

int main(){
	int T,k;
	string s;
	cin>>T;
	int ans;
	bool flag;
	for (int dummy=0;dummy<T;dummy++) {
		cin>>s>>k;
		ans=0;
		flag = true;
		int i;
		for (i=0;i<=s.length()-k;i++) {
			if (s[i]=='-') {
				ans++;
				for (int j=0;j<k;j++) {
					if(s[i+j]=='+') {
						s[i+j]='-';
					}
					else {
						s[i+j]='+';
					}
				}
			}
		}
		for (; i<s.length(); i++) {
			if (s[i]=='-') {
				cout<<"Case #"<<dummy+1<<": IMPOSSIBLE"<<endl;
				flag = false;
				break;
			}
		}
		if (flag==true) {
			cout<<"Case #"<<dummy+1<<": "<<ans<<endl;
		}
	}
	return 0;
}
