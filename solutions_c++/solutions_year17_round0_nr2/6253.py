#include <iostream>
#include <cstring>
using namespace std;

/* run this program using the console pauser or add your own getch, system("pause") or input loop */

int main() {
	int t;
	cin>>t;
	for (int k=1;k<=t;k++){
		string n;
		cin>>n;
		int flag=1;
		while (flag==1){
			flag=0; 
			for (int i=0,m=n.length();i<m-1;i++){
			if (n[i]>n[i+1]) {
				n[i]=n[i]-1;
				for (int j=i+1;j<m;j++) n[j]='9';
				flag=1;
			}	
		}
		}
		cout<<"Case #"<<k<<": ";
		if (n[0]=='0') {
			for (int i=1,m=n.length();i<m;i++) 
			cout<<n[i];
		cout<<endl;
		}
		else cout<<n<<endl;
		//cout<<"Case #"<<k<<": "<<kq<<endl;
	}
	return 0;
}
