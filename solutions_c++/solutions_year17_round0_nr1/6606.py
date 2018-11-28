#include <cmath>
#include <cstdio>
#include <string>
#include <vector>
#include <iostream>
using namespace std;
int main(){
    int t,n,k=1;
    string s;
    freopen("input.in","r",stdin);
    freopen("output3.txt","w",stdout);
    cin>>t;
    int j=1;
    while(t--){
    	int count=0,flag=0;
    cin>>s>>n;

    for(int i=0;i<s.size();i++){
    	if(s[i]=='-'){
            count++;
    		for(int j=0;j<n;j++){
                if(j+i==s.size()){flag=1;break;}
             if(s[i+j]=='-')
             {s[i+j]='+';}
             else
             {s[i+j]='-';}
         	 //if(i+j>s.size()) flag=1;
    		}
    		//count++;
    		//cout<<s<<endl;
    	}
    }
    /*for(int i=s.size()-n+1;i<s.size();i++){
    //cout<<s[i]<<endl;
    if(s[i]=='-')
    flag=1;
    break;
    }*/

    cout<<"Case #"<<k<<": ";
    if (flag==1 ){
    cout<<"IMPOSSIBLE"<<endl;
    }
    else{
    cout<<count<<endl;
    }
    k++;


}
	return 0;
}
