#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int t;
	cin>>t;
	string s;
	int k;
	int flag=0;
	for(int jj=0;jj<t;jj++){
	    
	    cin >> s;
	    cin >> k;
	    int count = 0;
	    int ispossible = 1;
	    int len = s.length();
	    for(int i=0;i<len;i++){
	        if(s[i] == '-'){
	            
	            if(i+k>len){
	                    goto label;
	            }
	            count++;
	            for(int j=i;j<i+k;j++){
	                if(s[j] == '-'){
	                    s[j] = '+';
	                }
	                else{
	                    s[j] = '-';
	                }
	            }
	        }
	    }
	    label:flag= 1;
	
	    for(int i=0;i<len;i++){
	        if(s[i] == '-'){
	            ispossible = 0;
	            break;
	        }
	    }
	    if(ispossible){
	        cout<<count<<endl;
	    }
	    else{
	        cout<<"IMPOSSIBLE"<<endl;
	    }
	}
	return 0;
}
