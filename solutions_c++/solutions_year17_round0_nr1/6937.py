#include<iostream>
#include<fstream>
using namespace std;
int main(){
	fstream  file,file2 ;
	file.open("A-small-attempt0.in",ios::in);
	file2.open("out",ios::out);
	int t;
	file>>t;
	for(int f=1;f<=t;f++){ 
		string str;
		int k,ans=0;
		bool out=0;
		file>>str>>k;
		file2<<"Case #"<<f<<": ";
		for(int i=0;i<str.size()-k+1;i++){
			if(str[i]=='-'){
				for(int j=i;j<i+k;j++){
					if(str[j]=='-')str[j]='+';
					else str[j]='-';
				}
				ans++;
			}
		}
		for(int i=0;i<str.size();i++){
			if(str[i]=='-'){
				out=1;
				file2<<"IMPOSSIBLE\n";
				break;
			}
		}
		if(out==0)file2<<ans<<"\n";
	}
}

