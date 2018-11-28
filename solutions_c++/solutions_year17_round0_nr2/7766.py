#include<bits/stdc++.h>

using namespace std;

int main(){
	
	
	fstream fin;
	fin.open("B-small-attempt0.in");
	ofstream fout;
	fout.open("2.txt");
	int T;
	fin>>T;
	for(int tt=1;tt<=T;tt++){
		int n;
		fin>>n;
		
		
		while(n>0){
			int a=n;	
			int r=n%10;
			a=a/10;
			bool tidy=true;
			while(a!=0){
				int x=a%10;
				if(x>r){
					tidy=false;
					break;
				}
				r=x;
				a=a/10;
			}
			if(tidy==true){
				fout<<"Case #"<<tt<<": "<<n<<endl;
				break;
			}
					
			n--;
		}
		
		
		
	}
	fout.close();
//	long long n;
	
	
	
}
