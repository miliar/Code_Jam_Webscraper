#include <iostream>
using namespace std;

int main(){
	int Te;
	cin>>Te;
	for(int te=1;te<=Te;te++){
		string s;
		cin>>s;
		int k;
		cin>>k;
		int n=s.size();
		int ans=0;
		for(int i=0;i<=n-k;i++){
			if(s[i]=='-'){
				ans++;
				for(int j=i;j<i+k;j++){
					if(s[j]=='-'){
						s[j]='+';
					}
					else{
						s[j]='-';
					}
				}
			}
		}
		for(int i=0;i<n;i++){
			if(s[i]=='-'){
				ans=-1;
				break;
			}
		}
		cout<<"Case #"<<te<<": ";
		if(ans!=-1){
			cout<<ans<<endl;
		}
		else{
			cout<<"IMPOSSIBLE\n";
		}
	}
	return 0;
}