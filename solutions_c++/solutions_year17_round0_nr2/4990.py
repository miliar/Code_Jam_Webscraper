#include <bits/stdc++.h>
using namespace std;
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("BLarge.out","w",stdout);
	int t;
	cin>>t;
	for(int i=1;i<=t;i++){
		long long n;
		cin>>n;
		stack<int>s;
		long long n1=n;
		int prev=n1%10;
		n1=n1/10;
		int c=1;
		int cur=prev;
		while(n1>0){
			 cur=n1%10;
			if(cur<=prev)
			s.push(prev);
			else{
				cur--;
				s.push(9);
			}
			prev=cur;
			n1=n1/10;
			c++;
		}
		s.push(cur);
		int a[c];
		int j=0;
		while(!s.empty()){
		a[j]=s.top();
		j++;
		s.pop();	
		}
		int flag1=0,flag2=0;
		cout<<"Case #"<<i<<": ";
		for(int k=0;k<c;k++){
		    if(flag1==0&&a[k]>0){
				flag1=1;
				cout<<a[k];
				if(a[k]==9)
				flag2=1;
			}else if(flag1==1&&flag2==0){
				cout<<a[k];
				if(a[k]==9)
				flag2=1;
			}else if(flag1==1&&flag2==1){
				cout<<9;
			}
			
		}
		cout<<endl;
		
	}

	return 0;
}

