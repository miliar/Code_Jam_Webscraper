#include<bits/stdc++.h>
using namespace std;

string s;
int k;

#define MAX 1005

int main() {
	
	freopen("input.in","r",stdin);
	freopen("output.txt","w",stdout);
	
	cin.sync_with_stdio(false);
	cout.sync_with_stdio(false);
	
	int t;
	cin>>t;
	
	for(int tst = 1;tst<=t;tst++) {
		
		cin>>s>>k;
		
		int steps = 0;
		
		for(int i = 0;i<s.size()-k+1;i++) {
			
			if(s[i] == '+')
				continue;
			
			steps++;
			for(int j = i;j<i+k;j++)
			{
				if(s[j] == '+')
					s[j] = '-';
				else
					s[j] = '+';
			}
		}
		
		
		bool flag = 0;
		
		for(int i = 0;i<s.size();i++)
		{
			if(s[i] == '-') {
				flag = 1;
				break;
			}
		}
	
		if(flag)
			cout<<"Case #"<<tst<<": IMPOSSIBLE"<<endl;
		else {
			cout<<"Case #"<<tst<<": "<<steps<<endl;
		}
	}
	
	return 0;
}
