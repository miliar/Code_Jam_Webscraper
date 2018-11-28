#include<iostream>
#include<fstream>
using namespace std;
int main(){
	ifstream fin("C:\\Users\\Goyal\\Downloads\\A-large.in");
	ofstream fout("C:\\Users\\Goyal\\Downloads\\A-large.out");
	if(fin.is_open()){		
		int t;		
		fin>>t;
		for(int l=0;l<t;l++){
			string st;			
			fin>>st;
			int k;					
			fin>>k;
			int c=0;
			bool flag=true;
			for(int i=0;i<st.length();i++){
				if(st[i]=='-'){
					if(st.length()-i>=k){
						for(int j=0;j<k;j++){
							if(st[i+j]=='-'){
								st.replace(i+j,1,"+");
							}
							else{
								st.replace(i+j,1,"-");
							}	
						}
						c++;
					}
					else{
						flag=false;
						fout<<"CASE #"<<l+1<<": IMPOSSIBLE"<<"\n";
						break;
					}
				}
			}
			if(flag==true){
				fout<<"CASE #"<<l+1<<": "<<c<<"\n";
			}
		}		
	}
	if(fout.is_open()){
		cout<<"File opened"<<"\n";
	}
	fin.close();
	fout.close();
}
