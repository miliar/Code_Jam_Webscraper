#include <bits/stdc++.h>
using namespace std;
int r,c;
string a[30];
int main(){
	long long int t,tc=1,i,j,k,p;
	for(cin>>t;tc<=t;++tc){
		cin>>r>>c;
		for(i=0;i<r;cin>>a[i++]);
		for(i=0;i<r;++i)
			for(j=0;j<c;++j)
				if(a[i][j]!='?'){
					for(k=j-1;k>=0&&a[i][k]=='?';a[i][k--]=a[i][j]);
					for(k=j+1;k<c&&a[i][k]=='?';a[i][k++]=a[i][j]);
				}
	for(i=0;i<r;++i)
		if(a[i][0]=='?'){
			if(i>0)	for(k=0;k<c;a[i][k]=a[i-1][k],++k);
			else for(k=0;k<c;a[i][k]=a[i+1][k],++k);
		}
	for(i=r-1;i>=0;--i)
		if(a[i][0]=='?'){
			if(i<r-1)for(k=0;k<c;a[i][k]=a[i+1][k],++k);
			else for(k=0;k<c;a[i][k]=a[i-1][k],++k);
		}
	cout<<"Case #"<<tc<<":\n";
	for(i=0;i<r;++i,cout<<'\n')
		for(j=0;j<c;cout<<a[i][j++]);
	}
}