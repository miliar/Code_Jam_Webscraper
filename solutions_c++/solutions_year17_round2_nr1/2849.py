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
#include <iomanip>
using namespace std;

ifstream in("A-large (1).in");
ofstream out("out-1b-a.txt");

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

#define N 10000
#define LL unsigned long long
#define LD long double
LL n,d;
LL k[N], s[N];

int main()
{
	xiomod  ob;
	ob.redirect_input (string("A-large (1).in"));
	ob.redirect_ouput (string("out-1b-a.txt"));
	

	LL t;

	cin>>t;

	for(int x=1; x<=t; x++){
		cin>>d>>n;
		LD max_time=0.0;
		for(int i=0; i<n; i++){
			cin>>k[i]>>s[i];
			LD tmp_time = ((LD)(d-k[i]))/((LD)(s[i])); 
			if(tmp_time >max_time){
				max_time=tmp_time;
			}
		}


		//ans speed calculation
		if(max_time==0.00L){
			max_time = 1.00L;
		}
		LD speed = ((LD)(d))/(max_time);
		cout<<"Case #"<<x<<": ";
		
		cout <<setprecision(6);
		cout <<fixed;
		cout<<speed<<endl;
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