#include<stdio.h>
#include<iostream>
#include<string>
#include<sstream>
using namespace std;
//inputfile = fopen("input_file.txt", "r");
//outputfile = fopen("output_file.txt", "w");
bool increaseCheck(string s){
	int i;
	bool flag = true;
     i = s.length()-1;
     for (;i>0;i--){
     	if(s[i]<s[i-1]){
     		flag = false;
     		break;
     	}
     }
     return flag;
}
void tidyNum(string s){
	int i;
	bool flag = true;
     i = 0;
     for (;i<=s.length()-1;i++){
     	if(s[i]>=s[i+1]){
     		flag = false;
     		break;
     	}
     	else{
     		cout<<s[i];
     	}
     }
     if(i==s.length()-1){
     	cout<<s[i];
     	i = i+1;
     }
     else if(s[i]-49 != 0){
     	cout<<s[i]-49;	
     }
     i=i+1;
     for (;i<=s.length()-1;i++){	
    	cout << '9';
     }
     cout<<endl;

}
int main(){
	int i,test;
	scanf("%d",&test);
	
	for (i=1;i<=test;i++){
		std::ostringstream ss;
		ss << i;
		cout << "Case #"<< ss.str() << ": ";
		string s;
     		cin >> s;
     		if(s.length()>=2){
			if(increaseCheck(s)==false){
 		    		tidyNum(s) ;
			}
			else{
				cout<<s<<endl;
			}	
     		}
     		else{
     			cout<<s<<endl;
     		}
	}		
}
