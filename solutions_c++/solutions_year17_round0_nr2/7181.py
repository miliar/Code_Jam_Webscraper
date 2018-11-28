#include <iostream>
#include <inttypes.h>
#include <bits/stdc++.h>  // includes cin to read from stdin and cout to write to stdout
using namespace std;  // since cin and cout are both in namespace std, this saves some text

vector<uint64_t> m;

void check(){
	//vector<uint64_t> m;
/*	int i=0;
	while(n>0){
		m.push_back(n%10);
		n=n/10;
	}
	reverse(m.begin(),m.end());
	*/
	int i=0;
	for(int j=0;j<m.size()-1;j++){
		if(m[j]<=m[j+1])
			continue;
		else
			{
				m[j]=m[j]-1;
				for(int k=j+1;k<m.size();k++)
					m[k]=9;
				check();
				break;
			}
	}
	/*cout <<"Case #"<<i++<<": ";
	for(int j=0;j<m.size();j++)
		cout<<m[j];
	cout<<endl;*/
}

int main() {
	
	freopen("B-large.in","r",stdin);
	freopen("output3.out","w",stdout);
  int t;
  int c=0;
  uint64_t n;
  cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
  for(int i=0;i<t;i++)
  {
	cin >> n;
	while(n>0){
		m.push_back(n%10);
		n=n/10;
		c++;
	}
	reverse(m.begin(),m.end());
	check();
	/*for(uint64_t j=n;j>=1;j--){
		cout<<j<<endl;
		if(check(j)){*/
		cout <<"Case #"<<i+1<<": ";
		for(int j=0;j<m.size();j++){
			if(j==0 && m[j]==0)
				continue;
			cout<<m[j];
		}
		cout<<endl;
		for(int x=0;x<c;x++)
			m.pop_back();
		c=0;
	}	
	return 0;	
}
