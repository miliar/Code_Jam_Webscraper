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
	ifstream cin("A-large.in");
	ofstream cout("A-large.out");
cin>>n;
for(int z=1;z<=n;z++){
	string a;
	int k,sol=0;
	cin>>a>>k;
	for(int i=0;i<=a.size()-k;i++){
		if(a[i]=='-'){
			sol++;
			for(int j=i;j<i+k;j++){
				if(a[j]=='+')
				a[j]='-';
				else
				a[j]='+';
			}
		}
	}
	bool ok=true;
	for(int i=a.size()-k+1;i<a.size();i++){
		if(a[i]=='-')
		ok=false;
	}
	cout<<"Case #"<<z<<": ";
	if(ok)
	cout<<sol<<endl;
	else 
	cout<<"IMPOSSIBLE"<<endl;
}
return 0;
}

