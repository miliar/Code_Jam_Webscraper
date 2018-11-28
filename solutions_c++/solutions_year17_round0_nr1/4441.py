#include<bits/stdc++.h>
using namespace std;

vector<int>a;
int count1=0;

int check(int i,int n){
	if(i==a.size()){
		return 1;
	}

	if(i+n>a.size()&&a[i]==0)
		return -1;

	if(a[i]==0){
		for(int j=i;j<i+n;j++){
			a[j]=(1+a[j])%2;
		}
		int e=i+n;
		for(int j=i;j<i+n;j++){
			if(a[j]==0){
				e=j;
				break;
			}
		}
		count1++;
		return check(e,n);
	}
	
	return check(i+1,n);
}

int main()
{
	int t,n,r;
	string s;
	cin>>t;
	r=t;
	while(t--){
		cin>>s;
		cin>>n;
		a.clear();
		count1=0;

		for(int i=0;i<s.size();i++){

			if(s[i]=='+')
				a.push_back(1);
			else
				a.push_back(0);
		}
		
		if(check(0,n)>=0)
			cout<<"Case #"<<r-t<<": "<<count1<<endl;
		else
			cout<<"Case #"<<r-t<<": IMPOSSIBLE\n";
	}

	return 0;
}