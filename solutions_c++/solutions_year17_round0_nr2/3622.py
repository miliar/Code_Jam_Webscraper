#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <fstream>
#include <vector>


using namespace std;

void sub(string &s,int r){
	int n=s.length();
	while(r>=0){
		if(s[r]=='0'){
			s[r]='9';r--;
		}
		else{
			s[r]--;if(r==0&&s[r]=='0') s.erase(0,1);
			break;
		}
	}
}

string tidy(string &s,int tail){
	if(tail==0) return s;
	for(int i=0;i<tail;i++){
		if(s[i]>s[i+1]){
			s[tail]='9';
			sub(s,tail-1);
			return tidy(s,tail-1);
		}
	}
	return s;
}

int main(){
	int n;
    string Tidy;
    //ofstream file;
    //ifstream file1;
    //file.open("2.out");
    //file1.open("2.in");
	cin>>n;
	for(int i=0;i<n;i++){
		cin>>Tidy;
        string res=tidy(Tidy,Tidy.length()-1);
		cout<<"Case #"<<i+1<<": ";
		cout<<res<<endl;
	}
    return 0;
}
