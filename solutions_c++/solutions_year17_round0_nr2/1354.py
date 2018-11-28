#include <bits/stdc++.h>
using namespace std;

#define sd(a) scanf("%d",&a)
#define ss(a) scanf("%s",a)
#define sl(a) scanf("%lld",&a)
#define clr(a) memset(a,0,sizeof(a))
#define debug(a) printf("check%d\n",a)
#define F first
#define S second
#define mp make_pair
#define pb push_back
#define ll long long
#define MAX 100005
#define mod 1000000007

int main() {
	
	int t;
	
	sd(t);
	
	string s;
	
	while(t--){
		cin>>s;
		int a[s.length()];
		
		for(int i=0;i<s.length();i++){
			a[i] = s[i]-'0';
				
		}
		int pos=-1;
		
		for(int i=s.length()-1;i>=1;i--){
			if(s[i]<s[i-1]){
				pos=i;
				break;
			}
		}
		
		if(pos!=-1){
			
			int flag=1;
			
			while(flag){
				flag = 0;
				
				if(!a[0])
					break;
					
				for(int i=s.length()-1;i>=1;i--){
					
					if(a[i]<a[i-1]){
						flag=1;
						a[i-1]--;
						int temp = i;
						
						while(temp!=s.length()){
							a[temp++]=9;
						}
						
						break;
					}
					
				}
			}
			
			if(a[0]){
				pos=0;
			}
			else{
				pos=1;
			}
			
			for(int i=pos;i<s.length();i++)
				cout<<a[i];
			cout<<endl;
			
			
		}
		else{
			cout<<s<<endl;
		}
		
		
	}
	
	
	
	return 0;
}
