#include <bits/stdc++.h>
using namespace std;
int main(){
	int n;
	cin>>n;
	for(int t=1;t<=n;t++){
		long long int e=0;
		cin>>e;
		for(int j=0;j<20;j++){
			int h[100];
			int r=e%10;
			int count=0;
			while(e!=0){
				e=e/10;
				h[count++]=r;
				r=e%10;
			}
			int f = 22;
			for(int i=1;i<count;i++)
				if(h[i-1]<h[i])
				{
					f = i;
				}
			if(f<count){
				h[f] = h[f]-1;
				for(int i=0;i<f;i++)
					h[i]=9;
			}
			long long int u = 0;
			int q=0;
			for(int i=count-1;i>=0;i--)
			{
				if(h[i]!=0)
				{
					q=i;
					break;
				}
			}
			long long int r2=0;
			for(int i=q;i>=0;i--){
				r2=r2*10+h[i];
			}
			e = r2;
		}
		cout<<"Case #"<<t<<": ";
		cout<<e;
		cout<<'\n';
	}
	return 0;
}
