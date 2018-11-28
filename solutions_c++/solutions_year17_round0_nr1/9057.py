#include <iostream>
#include <string>
using namespace std;

char flip(char c){
    if(c=='-'){ return '+';}
    else if(c=='+'){ return '-';}
}
int testCase(string s,int k){
    int count=0;
    int testCount=0;
    for(int j=0; j<s.length()-k; j++){
        if(s[j]=='-'){
            count++;
            for(int l=0; l<k; l++){
                s[j+l]=flip(s[j+l]);
            }
        }
    }
    for(int x=s.length()-k; x<s.length(); x++){
        if(s[x]=='-'){testCount++;}
    }
    if(testCount==k){return (count+1);}
    else if(testCount==0){return count;}
    else{return -1;}
}
int main() {
	int t;
	string s;
	int k;
	int output;
	cin >> t;
	for(int i=1; i<=t; i++){
	    cin >> s;
	    cin >> k;
	    output=testCase(s,k);
	    if(output==-1){
	        cout << "Case #" << i << ": IMPOSSIBLE" <<"\n";
	    }
	    else{
	        cout << "Case #" << i << ": " << output <<"\n";
	    }
	}
	return 0;
}