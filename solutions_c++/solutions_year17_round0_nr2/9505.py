#include<iostream>
#include<string>
#include<fstream>
#include<algorithm>
#include<math.h>
#include<stdio.h>
#include<sstream>
using namespace std;
long is_sorted(string n){
	int p=-1;
	int temp=0;
	for(int i=0;i<n.length();i++){
		if(((int)n[i])-48<temp){
			string s=n.substr(i,n.length()-i);
			//cout<<((int)n[i])<<temp<<"\n";
			istringstream ss;
			long long x=0;
			ss.clear();
			ss.str("");
			ss.str(s);
            ss>>x;
			return x;
		}
		temp=((int)n[i])-48;
	}
	return -1;
}
int main(){
    ifstream fin("C:\\Users\\Goyal\\Downloads\\B-small-attempt1.in");
	ofstream fout("C:\\Users\\Goyal\\Downloads\\B-small-attempt1.out");
	if(fin.is_open()){
        int t;
        fin>>t;
        for(int k=0;k<t;k++){
            long long n;
            fin>>n;
            ostringstream ss;
            ss<<n;
            string x=ss.str();
            bool flag=false;
            for(int i=0;i<x.length();i++){
                if(((int)x[i])-48>=2){
                    flag=true;
                    break;
                }
            }
            if(flag==false){
                int i=0;
                for(i=0;i<x.length();i++){
                    if(((int)x[i])-48==0){
                        break;
                    }
                }
                if(i<x.length()){
                    fout<<"CASE #"<<k+1<<": "<<pow(10,x.length()-1)-1<<"\n";
                }
                else{
                    fout<<"CASE #"<<k+1<<": "<<n<<"\n";
                }
                continue;
            }
            long long val=is_sorted(x);
            while(val!=-1){
                ostringstream ss;
                ss<<(n-val-1);
                string x=ss.str();
                n=n-val-1;
                val=is_sorted(x);
            }
            fout<<"CASE #"<<k+1<<": "<<n<<"\n";
            /*else{
                ostringstream ss;
                ss<<(n-val-1);
                string x=ss.str();
                if(is_sorted(x)!=-1){

                }
                fout<<"CASE #"<<k+1<<": "<<n-val-1<<"\n";
            }*/
        }
	}
	fin.close();
	fout.close();
}
