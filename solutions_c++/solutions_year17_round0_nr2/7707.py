#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int t;
	cin>>t;
	string s;
	for(int uu=0;uu<t;uu++){
	    cin>>s;
	    //checking for tidy no.
	    int len = s.length();
	    int alreadyTidy = 1;
	    int index = -1;
	    for(int i=0;i<len-1;i++){
	        if(s[i]>s[i+1]){
	            alreadyTidy = 0;
	     //       index = i;
	            
	        }
	    }
	    
	    if(alreadyTidy == 0){
	        char c;
	        for(int i=0;i<len-1;i++){
	            if(s[i]>s[i+1]){
	               index = i;
	               c = s[i];
	               break;
	            }
	        }
	        while((c == s[index]) && index >= 0){
	            index-- ;
	        }
	        index++;
	        if(s[index]!='0')
	            s[index] = s[index] - 1;
	        else
	            s[index] = '9';
	        for(int j=index+1;j<len;j++){
	            s[j] = '9';
	        }
	        if(s[0] == '0' && len > 1){
	            cout<<"Case #"<<(uu+1)<<": "+s.substr(1,len-1)<<endl;
	        }
	        else
	            cout<<"Case #"<<(uu+1)<<": "+s<<endl;
	    }
	    else{
	        cout<<"Case #"<<(uu+1)<<": "+s<<endl;
	    }
	}
	
	return 0;
}
