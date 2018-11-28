#include <iostream>
#include <string>
using namespace std;
int main() {
	int t;
	cin>>t;
	for(int c=1;c<=t;c++) {
		string a;
		cin>>a;
		int k;
		cin>>k;
		int ans=0;
		for(int j=0;j<a.size();j++) {
			if(a[j]=='+')
				continue;
			else {
				int l=j;
				if(l+k-1>=a.size())
				{
					ans = -1;
					break;
				}
				int cnt=0;
				while(cnt!=k) {
					if(a[l]=='-')
						a[l]='+';
					else
						a[l]='-';
					cnt++;l++;
				}
				ans++;
			}	
		}
		for(int i=0;i<a.size();i++)
		{
			if(a[i]=='-'){
				ans=-1;
				break;
			}
		}
		cout<<"Case #"<<c<<": ";
		if(ans==-1)
			cout<<"IMPOSSIBLE";
		else
			cout<<ans;
		cout<<endl;
	}
	return 0;
}
