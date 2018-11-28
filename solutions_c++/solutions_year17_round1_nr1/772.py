#include<iostream>
#include<string>
#include<map>
using namespace std;
int main(){
	int TT;
	int r,c;
	cin>>TT;
	string s[100];
	for(int T=1;T<=TT;++T){
	    cin>>r>>c;
	    for(int i=0;i<r;++i)
	        cin>>s[i];
	    for(int i=1;i<r;++i){
	        for(int j=0;j<c;++j){
	            if(s[i][j]=='?'){
	                s[i][j]=s[i-1][j];
	            }
	        }
	    }
	    for(int i=r-2;i>=0;--i){
	        for(int j=0;j<c;++j){
	            if(s[i][j]=='?'){
	                s[i][j]=s[i+1][j];
	            }
	        }
	    }
	    for(int i=1;i<c;++i){
	        if(s[0][i]=='?'){
	            for(int j=0;j<r;++j){
	                s[j][i]=s[j][i-1];
	            }
	        }
	    }
	    for(int i=c-2;i>=0;--i){
	        if(s[0][i]=='?'){
	            for(int j=0;j<r;++j){
	                s[j][i]=s[j][i+1];
	            }
	        }
	    }
	    cout<<"Case #"<<T<<": "<<"\n";
	    for(int i=0;i<r;++i){
	        cout<<s[i]<<"\n";
	    }
	}
	return 0;
}
