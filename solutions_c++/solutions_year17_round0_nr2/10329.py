 //============================================================================
// Name        : Tidy_Numbers.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <string>
using namespace std;
bool isTedy(unsigned long long x){
	string s=to_string(x);
	int count=0;
	int len=s.length();
	for(int i=1;i<len;i++){
		if(s[i-1]<=s[i]){
			count++;
		}
		else {
			return false;
		}
		if(count==len){
			return true;
		}
	}

}
int main() {
  freopen("B-small-attempt4.in","rt",stdin);
  freopen("output.txt","wt",stdout);
	 int t;
	 int cases=0;
	 //bool flag=true;
	 cin>>t;
	 while(t--){
	 	++cases;
		 unsigned long long n;
		 cin>>n;
		 while(!isTedy(n)){
			 n--;
			 }
			 cout<<"Case #"<<cases<<": "<<n<<endl;
		 }




	return 0;
}
