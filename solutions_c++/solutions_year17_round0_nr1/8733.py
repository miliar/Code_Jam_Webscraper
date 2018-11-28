#include<bits/stdc++.h>
using namespace std;

int main(){
	fstream fin;ofstream fout;
	fin.open("A-large.in");
	fout.open("large.txt");
	int T;
	fin>>T;
	int tt=1;
	for(int tt=1;tt<=T;tt++){
		string s;
		fin>>s;
		int K;
		fin>>K;
	//	s="-+-+-";K=4;
		bool chk=true;
		int flips=0;int skip=0;
		for(int k=0; k<=s.length()-K;k++){
			
			if(s[k]=='-'){
				for(int i=k;i<K+k;i++){
					if(s[i]=='-')s[i]='+';
					else if(s[i]=='+')s[i]='-';
					
				}
				flips++;		
			}
			
			if(k==(s.length()-K)){
				for(int i=k;i<s.length();i++){
					if(s[i]=='-'){
						chk=false;
						break;
					}
								
							
				}	
			}
		//	cout<<s<<endl;
		}	
	
		if(chk==true)
			fout<<"Case #"<<tt<<": "<<flips<<endl;
		else if(chk==false)
			fout<<"Case #"<<tt<<": IMPOSSIBLE"<<endl;
		}
		fout.close();
}
