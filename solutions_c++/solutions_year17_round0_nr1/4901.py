#include<bits/stdc++.h>

using namespace std;

typedef long long int lli;

int f,countp,countm;

lli recur(lli ans,int k,int l,int i,int j,string &s){
	 f=0;
	 countp=0,countm=0;
	 if(i>j)
	return -1;
	if(s[i]=='-'){
		if((i+k-1)>j)
		return -1;
		for(int m=i;m<(i+k);m++){
			if(s[m]=='+')
			s[m]='-';
			else
			if(s[m]=='-')
			s[m]='+';
		}
		f=1;
		ans++;
	}
	if(s[j]=='-'){
		if((j-k+1)<i)
		return -1;
		for(int m=j;m>(j-k);m--){
			if(s[m]=='+')
			s[m]='-';
			else
			
			if(s[m]=='-')
			s[m]='+';
		}
		f=1;
		ans++;
	}
	if(f==1){
		for(int m=0;m<l;m++){
			if(s[m]=='+')
			countp++;
			if(s[m]=='-')
			countm++;
		}
		if(countp==l)
		return ans;
	}
	if(i==j)
	return -1;
	i++;
	j--;
	return recur(ans,k,l,i,j,s);
}

int main(){
	freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
	int t,k,l;
	lli ans;
	string s;
	scanf("%d",&t);
	cin.ignore();
	for(int i=1;i<=t;i++){
		countp=0;countm=0;
		cin>>s;
		l=s.size();
		scanf("%d",&k);
		for(int m=0;m<l;m++){
			if(s[m]=='+')
			countp++;
			if(s[m]=='-')
			countm++;
		}
		if(countp==l)
		ans=0;
		else if(k>=l && countm==l)
		ans=1;
		else if(k>=l && countm!=l)
		ans=-1;
		else
		ans=recur(0,k,l,0,l-1,s);
		
		if(ans!=-1)
		ans=printf("Case #%d: %lli\n",i,ans);
		else
		if(ans==-1)
		printf("Case #%d: IMPOSSIBLE\n",i);
		s.clear();
	}
	return 0;
}
