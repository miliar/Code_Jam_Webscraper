#include <bits/stdc++.h>

using namespace std;

int main(){
	int test;
	cin>>test;
	int t=1;
	while(test--){
		int n;
		cin>>n;
		string s="o";
		for(int i=0;i<n;i++)
			s+=".";
		s+="o";
		n=s.size();
		int k;
		cin>>k;
		int L=-1,R=n,P;	
		while(k--){
			L=-1;
			R=n;
			for(int i=0;i<n;i++){
				if(s[i]=='o')
					continue;
				int l=i,r=i;
				for(int j=i+1;j<n;j++)
					if(s[j]!='o')
						r=j;
					else
						break;
				for(int j=i-1;j>=0;j--)
					if(s[j]!='o')
						l=j;
					else
						break;
				l=i-l;
				r=r-i;
				if(min(l,r)>L)
					L=min(l,r),R=max(l,r),P=i;
				else if(min(l,r)==L and max(l,r)>R)
					R=max(l,r),P=i;	
			}
			s[P]='o';
			// cout<<max(L,R)<<" "<<min(L,R)<<" "<<P<<" "<<s<<"\n";
		}
		cout<<"Case #"<<t<<": ";
		t++;
		cout<<max(L,R)<<" "<<min(L,R)<<"\n";
	}
	return 0;
}