#include <iostream>
#include <fstream>
#include <vector>
using namespace std;
int istidy(unsigned long long  x){
	int temp;
	while(x!=0){
		temp = x%10;
		x=x/10;
		if(temp<x%10)
			return 0;
	}
	return 1;
}

main(){
	  ifstream in; 
	in.open("B-large.in",ios::binary);    
	   ofstream out; 
	out.open("B-larg-out.txt",ios::binary); 
	unsigned long long  s;
	int n;
	
	in>>n;
	for(int t=1;t<=n;t++){
		vector <int> v,vv;
		in>>s;
		while (s!=0){
			vv.push_back(s%10);
			s=s/10;
		}
		for(int i=0;i<vv.size();i++){
			v.push_back(vv[vv.size()-1-i]);
		}
					
		for(int k=0;k<18;k++){
		for(int i=0;i<v.size();i++){
			if(v[i]>v[i+1] && (i+1)!=v.size()){
				v[i]--;
				for(int j= i+1;j<v.size();j++){
					v[j]=9;
				}	
				break;
			}
		}
	}
		while(v[0]==0 && !v.empty())
		v.erase(v.begin());
		out<<"Case #"<<t<<": ";
		for(int i=0;i<v.size();i++){
			out<<v[i];
		}
		out<<endl;
	}
	
}

