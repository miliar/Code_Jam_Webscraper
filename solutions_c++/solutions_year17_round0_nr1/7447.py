#include <iostream>
#include <cstring>
#include <fstream>
using namespace std;

void flip(char *s){
    if(*s=='+') *s='-';
    else *s='+';
}

int main() {
	string line;
  ifstream myfile ("A-large.in");
  ofstream ofile ("examplelarge.txt");
  ofile.is_open();
  if (myfile.is_open()){
  	
      int t;
      myfile>>t;
       int c=1;
       
        string s;
        int k;
       while ( myfile>>s>>k )
    {
        int count=0;
        bool flag=false;
        for(int i=0;i<s.length();i++){
            if(i==s.length()-1&&s[i]=='+') flag=true;
            if(s[i]=='-'){
                if(i+k-1<=s.length()-1){
                    count++;
                for(int j=0;j<k;j++){
                flip(&s[i+j]);
            }
                }
            else break;
            
        }
    }
    if(flag) ofile<<"Case #"<<c<<": "<<count<<endl;
    else ofile<<"Case #"<<c<<": "<<"IMPOSSIBLE"<<endl;
    c++;
    }
	myfile.close();
  }
    ofile.close();
	return 0;
}

