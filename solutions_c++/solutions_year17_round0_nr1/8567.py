#include<iostream>
using namespace std;
#include<bits/stdc++.h>
#define f(i,n) for(int z=i; z<n; z++)
#define fe(i,n) for(int z=i; z<=n; z++)
long int k;
string s;

long int countt=0;

bool cake(int first, int last){
    //cout<<s<<" "<<first<<endl;
    if(first>last){
    	return true;
	}
	if(last-first+1<k){
		return false;
	}
	long int i=first,j=last;
    while(s[i]!='-' && i<=j){
    	i++;
	}
/*	while(s[j]!='-' && i<=j){
    	j--;
	}*/
		
     if(i>j){
     	return true;
	 }
	f(i,i+k && j-i+1>=k){
		if(s[z]=='+')
		s[z]='-';
		else if(s[z]=='-')
		s[z]='+';
		
	}
	countt++;
	 while(s[i]!='-' && i<=j){
    	i++;
	}

	cake(i,j);
	
}
int main()
{  int T;
	cin>>T;
   f(0,T){
   	countt=0;
   	string sh;
   	cin>>sh;
   	long int kh;
   	cin>>kh;
   	s=sh;
   	k=kh;
   	long int length=s.length();
   	bool possible=cake(0, length-1);
   	if(possible)
   	cout<<"Case #"<<z+1<<": "<<countt<<"  "<<endl;
   	else
   	cout<<"Case #"<<z+1<<": "<<"IMPOSSIBLE"<<" "<<endl;
   }
	return 0;
}
