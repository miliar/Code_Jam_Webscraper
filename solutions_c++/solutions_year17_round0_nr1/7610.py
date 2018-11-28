#include <bits/stdc++.h>
using namespace std;
int main(){
	int n;
	cin>>n;
	for(int t=1;t<=n;t++)
	{
		string s;
		cin>>s;
		int y;
		cin>>y;
		int l=s.length();
		int test=0;
		int k=0;
		for(int i=0;i<l;i++)
		{
			if(s[i]=='-'){
				k++;
				int r=i;
				if(r+y>l){
					test=1;
					break;
				}
				for(int j=r;j<r+y;j++)
				{
					if(s[j]=='+')
					{
							s[j]='-';
					}
					else
						s[j]='+';
				}
			}
		}
		cout<<"Case #"<<t<<": ";
		if(test==1)
			cout<<"IMPOSSIBLE\n";
		else
			cout<<k<<'\n';

	}
	return 0;
}
