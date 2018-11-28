#include <bits/stdc++.h>
using namespace std;
string s;
int k;
void flip(int strt,int end){
	for(int i=strt;i<end;i++)
		if(s[i]=='-')
			s[i]='+';
		else
			s[i]='-';
}
int main(){
	ifstream cin("input.txt");
    ofstream cout("output.txt");
	int t,count;
	cin>>t;
	for(int it=1;it<=t;it++){
		cin>>s>>k;
		count=0;
		bool flag=false; //To check if un-flipped pan cake exist beyond reach
		int sz=s.length(); //Size of the string
		for(int i=0;i<=sz-k;i++){
			if(s[i]=='-'){
				count++;
				flip(i,i+k); //Flip k pancake
			}
		}
		for(int i=sz-k+1;i<sz;i++){
			if(s[i]=='-'){
				flag=true;
				break;
			}
		}
		if(flag)
			cout<<"Case #"<<it<<":"<<" IMPOSSIBLE\n";
		else
			cout<<"Case #"<<it<<": "<<count<<endl;
	}
}