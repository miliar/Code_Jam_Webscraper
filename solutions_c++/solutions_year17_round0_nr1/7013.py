#include <iostream>
#include <fstream>
#include <vector>
using namespace std;
bool imp;
int k;
bool isdone(string temp){
 		for(int i=0;i<temp.size();i++){
 			if(temp[i]=='-')
 				return false;
		 }
		 imp = false;
		 return true;
}
int min(int x, int y){
	if(x<y)
		return x;
	return y;
}
 
int min_fun(string temp,int pos){
	if(isdone(temp))
		return 0;
	if(pos==temp.size())
		return 9999;
	
	if(temp[pos]=='+')
		return min_fun(temp,pos+1);
	else{
	if(pos+k <= temp.size())
		for(int i=pos;i<pos+k;i++){
			if(temp[i]=='-')
				temp[i]='+';
			else
				temp[i]='-';
		}
		return 1+min_fun(temp,pos+1);
	}
	
}

main(){
	  ifstream in; 
	in.open("A-large.in",ios::binary);    
	   ofstream out; 
	out.open("a-larg-out.txt",ios::binary); 
	string  s;
	int n;
	
	in>>n;
	for(int t=1;t<=n;t++){
		imp =true;
		string s;
		in>>s;
		in>>k;	
		
		int outmin=min_fun(s,0);
		if(imp)
			out<<"Case #"<<t<<": IMPOSSIBLE"<<endl;
		else
			out<<"Case #"<<t<<": "<<outmin<<endl;
	}
	
}

