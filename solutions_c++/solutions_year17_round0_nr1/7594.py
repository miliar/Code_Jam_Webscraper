#include<iostream>
#include<stdlib.h>

using namespace std;

int main(){
    int tests;
    cin >> tests;
    int cases=1;
    int k,l,count;
    string s;
    bool fl=false;
    while(tests--){

	cin >> s >> k;
	
	l = s.length();
	fl = false;
	count = 0;

	for(int i=0;i<l;i++){
	
		if(s[i]=='+')
			continue;

		if(i+k-1<l){

		    for(int j=0;j<k;j++){

				if(s[i+j]=='+')
			   	 s[i+j]='-';
				
				else
			    		s[i+j]='+';
		    }
		    count++;
		}
		else{
		    fl = true;
			 break;
		}
	    
	}
	if(!fl){
	    cout <<"Case #"<<cases<<": "<<count<<endl;
	}
	else {
	    cout <<"Case #"<<cases<<": IMPOSSIBLE"<<endl;
	}
	cases++;
    }
    return 0;
}
