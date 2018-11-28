#include<iostream>
using namespace std;
int n;
int k;
int ans;
bool flag;
string str;

int main(){
	cin>>n;
	for(int i=1;i<=n;i++){
		ans=0;
		cin>>str;
		cin>>k;
		flag=false;
		for(int j=0;j<str.size();j++){
			if(str[j]=='-'){
				if(j+k-1<str.size()){
					for(int q=j;q<j+k;q++){
						if(str[q]=='-') str[q]='+';
						else str[q]='-';
					}
					ans++;
				}
				else{
					cout<<"Case #"<<i<<": IMPOSSIBLE"<<"\n";
					flag=true;
					break;
				}
			}
		}
		if(!flag) cout<<"Case #"<<i<<": "<<ans<<"\n";
	}
	return 0;	
}