#include<bits/stdc++.h>
using namespace std;

int a[100];

void gen(int a[],int l,int r,int len){
	int i;
	if(l==r){
		i=0;
		while(a[i]==0){
			i++;
		}
		for(;i<len;i++){
			cout<<a[i];
		}
		cout<<endl;
		return;
	}
	else{
	i=l;
	while(i<=r-1){
		if(a[i]>a[i+1])
		break;
		i++;
	}
	if(i!=r){
	for(int j=i+1;j<=r;j++)
		a[j]=9;
	a[i]--;
	gen(a,l,i,len);
	}
	else gen(a,0,0,len);
	}
}

int main(){
	int t,i;
	cin>>t;
	int c=1;
	while(t>0){
		string s;
		cin>>s;
		for(i=0;i<s.length();i++){
			a[i]=s[i]-'0';
		}
		cout<<"Case #"<<c<<": ";
		gen(a,0,s.length()-1,s.length());
		c++;
		t--;
	}
}
