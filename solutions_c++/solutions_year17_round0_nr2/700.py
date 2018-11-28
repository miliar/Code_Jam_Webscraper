#include <iostream>
#include <vector>
#include <set>
#include <cmath>

using namespace std;


int main(){
	int nb;
	cin >>nb;
	for(int cases=0; cases<nb; cases++){
    cout << "Case #"<<cases+1<<": ";
    string s;
    cin>>s;
    char minseen='9';
    int prop=0;
    int i = s.size()-1;
    while(i>=0){
      if(s[i]<=minseen) minseen = s[i]; 
      else{
        while(s[i]=='0')
          s[i--]='9';
        s[i]--;
        minseen = s[i];
        for(int j=i+1; j<s.size();j++) s[j]='9';
      }
      i--;
    }
    string s2;
    bool ok = false;
    for(int i=0;i<s.size();i++){
      if( ok) s2+= s[i];
      else if(s[i]!='0') {ok = true; s2+= s[i];}
    }
//     cout << s<<endl;
    cout << s2<<endl;   
  }
	return 0;
}
