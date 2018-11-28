#include<iostream>
#include <bits/stdc++.h>

using namespace std;
string  s;
char give(char c){
	if(c == '+')
	    return '-';
	if(c == '-')
		return '+';    
}
int flip(int start , int end){
	for(;start <= end;start++){
		s[start] = give(s[start]);

	}            
}
int main(){
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

	int count = 0;
	int size;
	int t;
	cin>>t;
	for( int j = 0;j < t;j++)
	{
	
	cin>>s;
	cin>>size;
	count = 0;
	int i = 0;
	int flag =1;
	for ( ; i <=  s.length() - size  ;i++){
		   if(s[i] != '+')
		   {
			    flip(i,i+size-1);
//				cout<<s<<endl;
				count++;
			}
	}
	for(;i < s.length() ;i++){
		if(s[i] != '+'){
			flag = 0;
		}
	}
	if(flag != 0)
	   cout<<"Case #"<<j+1<<": "<<count<<endl;
	else 
	   cout<<"Case #"<<j+1<<": "<<"IMPOSSIBLE"<<endl;

    }
	return 0;
}
