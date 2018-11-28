#include <iostream>
#include <algorithm>
#include <cmath>
#include <stdio.h>
#include <stdlib.h>
#include <vector>
#include <queue>
#include <stack>
using namespace std;

#define ll long long


int t;
int k;
int f;
int ans;
string s;

int main(){
	freopen("A-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	cin>>t;
	for(int i=1;i<=t;i++){
		cout<<"Case #"<<i<<": ";
		f = 0;
		ans =  0;
		cin>>s>>k;
		for(int j=0;j<s.size()-k+1;j++){
			if(s[j]=='-'){
				ans += 1;
				for(int p=j;p<j+k;p++){
					if(s[p]=='-') s[p] = '+';
					else s[p] = '-';
				}
			}
		}
		for(int i=0;i<s.size();i++){
			if(s[i]=='-'){
				f = 1;
				break;
			}
		}
		if(f==0) cout<<ans<<endl;
		else cout<<"IMPOSSIBLE\n";
	}
	return 0;
}