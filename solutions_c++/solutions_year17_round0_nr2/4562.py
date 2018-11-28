#include<bits/stdc++.h>
using namespace std;
int n;
int II()
{
int n;
scanf("%d",&n);
return n;
}
int main(){
	ifstream cin("B-large.in");
	ofstream cout("B-large.out");
cin>>n;
for(int z=1;z<=n;z++){
	string a;
	cin>>a;
	for(int i=0;i<a.size()-1;i++){
		if(a[i]>a[i+1]){
			a[i]--;
			for(int j=i+1;j<a.size();j++)
			a[j]='9';
			i=-1;
		}
	}
	bool ok=false;
	cout<<"Case #"<<z<<": ";
	for(int i=0;i<a.size();i++){
		if(a[i]!='0')
		ok=true;
		
		if(ok)
		cout<<a[i];
	}
	cout<<endl;
}
return 0;
}

