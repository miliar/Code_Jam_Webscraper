#include <iostream>
#include <fstream>
#include <string>
#include <cstring>
#include <cmath>
#include <vector>
#include <map>
#include <algorithm>
#include <stack>
#include <queue>
using namespace std;

ifstream in("A-large.in");
ofstream out("out-a.txt");

class xiomod{
	private: 
		streambuf *cin_stbuf;
		streambuf *cout_stbuf;
		
	public:
		xiomod();
		void redirect_input(string name);
		void redirect_ouput(string name);
		void restore_cin();
		void restore_cout();
 };

#define N 100009
#define LL unsigned long long


int main()
{
	xiomod  ob;
	ob.redirect_ouput (string("out-a.txt"));
	ob.redirect_input (string("A-large.in"));

	int t,k;
	char s[N];

	cin>>t;

	for(int x=1; x<=t; x++){
		cin>>s>>k;
		
		//for test
		//cout<<"input: "<<s<<" "<<k<<endl;


		bool flag=true;
		int res=0;
		int len=strlen(s);
		for(int i=0; i<len&&flag==true; i++){
			if(s[i]!='+'){
				int lim2=i+k;
				res++;
				if(lim2<=len){
					for(int j=i; j<lim2; j++){
						s[j]=(s[j]=='+')?'-':'+';
					} 
				}else{
					flag=false;
				}
			}
		}

		//output
		cout<<"Case #"<<x<<": ";
		if(flag==false){
			cout<<"IMPOSSIBLE";
		}else{
			cout<<res;
		}
		cout<<endl;
	}
	
	return 0;
}

		xiomod::xiomod(){
			cin_stbuf=cout_stbuf=NULL;
		}
		void xiomod::redirect_input(string name){
			if(cin_stbuf!=NULL){
				return;
			}
			
			cin_stbuf=cin.rdbuf();
			cin.rdbuf(in.rdbuf());
		}

		void xiomod::redirect_ouput(string name){
			if(cout_stbuf != NULL){
				return;
			}
			
			cout_stbuf=cout.rdbuf();
			cout.rdbuf(out.rdbuf());
		}

		void xiomod::restore_cin(){
			if(cin_stbuf!=NULL){
				cin.rdbuf(cin_stbuf);
				cin_stbuf=NULL;
			}
		}

		void xiomod::restore_cout(){
			if(cout_stbuf!=NULL){
				cout.rdbuf(cout_stbuf);
				cout_stbuf=NULL;
			}
		}