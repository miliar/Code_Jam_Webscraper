#include <bits/stdc++.h>
using namespace std;

bool verify(string s)
{
	for(int i=0;i<s.length();++i){
		char ch=s[i];
		if(ch=='-'){
			return false;
		}
	}
	return true;
}
int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
    int t;
    cin>>t;
    int tc=1;
    while(t--){
    	string s;
    	int k;
    	cin>>s>>k;
    	int minc=0;
    	int length=s.length();
    	for(int i=0;i<length-k+1;++i){
    		if(s[i]=='-'){
				for(int j=i;j<i+k;++j){
					if(s[j]=='-'){
						s[j]='+';
					}else{
						s[j]='-';
					}
				}
				minc++;
			}
		}
		
		
    	cout<<"Case #"<<tc++<<": ";
    	if(!verify(s)){
			cout<<"IMPOSSIBLE\n";
		}else{
			cout<<minc<<"\n";
		}
    	
	}
    return 0;
}

