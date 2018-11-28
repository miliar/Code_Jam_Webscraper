#include <bits/stdc++.h>
using namespace std;
typedef double ld;
typedef long long ll;
typedef unsigned int uint;
typedef unsigned long long ull;
typedef pair<int,int>ii;
const int MAXN=1111;
const int INF=0x7f7f7f7f;
int cases;

bool check(const string&s){
    auto a=s[0];
    for(int i=1;i<s.length();i++){
    	if(s[i]<a) return false;
        a=s[i];
    }
    return true;
}


int main() {
	
	int x;
	string str,tmp;
	while(~scanf("%d",&cases)) {
		for(int ca=1;ca<=cases;ca++){
			cin>>str;
			printf("Case #%d: ",ca);
			tmp=str;
			while(!check(tmp)) {
				tmp.clear();
				int pos=str.length();
				for(int i=str.length()-1;i>0;i--){
					if(str[i]<str[i-1]) pos=i-1;
				}	    
				if(str[pos]-1=='0'){
					for(int i=0;i<str.length()-1;i++){
						tmp.push_back('9');
					}
				}else{
					
					tmp=str.substr(0,pos+1);
                    tmp[pos]--;
					for(int i=pos+1;i<str.length();i++){
						tmp.push_back('9');
					}
				}
				str=tmp;
			}
			cout<<str<<'\n';
		}
	}
}
