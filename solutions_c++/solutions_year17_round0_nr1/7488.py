#include<iostream>
#include<algorithm>
#include<vector>
#include<set>
#include<stdlib.h>
#include<queue>
#include<math.h>

using namespace std;

int main(){
    int t;
    cin >> t;
    int cases=1;
    while(t--){
	string s;
	int k;
	cin >> s >> k;
	int l = s.length();
	bool fl = 0;
	int count = 0;

	for(int i=0;i<l;i++){
	
	    if(s[i]=='-'){

		if(i+k-1<l){
		    for(int j=0;j<k;j++){
			if(s[i+j]=='+'){
			    s[i+j]='-';
			}
			else {
			    s[i+j]='+';
			}
		    }
		    count++;
		}
		else{
		    fl = 1;
		}
	    }
	}
	if(!fl){
	    cout <<"Case #"<<cases<<": "<<count;
	}
	else {
	    cout <<"Case #"<<cases<<": IMPOSSIBLE";
	}
	cout << endl;
	cases++;
    }
    return 0;
}
