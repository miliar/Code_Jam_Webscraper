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

ifstream in("C-large.in");
ofstream out("out-c.txt");

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
#define ULL unsigned long long
#define LL long long


int main()
{
	xiomod  ob;
	ob.redirect_ouput (string("out-c.txt"));
	ob.redirect_input (string("C-large.in"));

	LL t,n,k;

	cin>>t;
	int x=0;
	while(t--){
		x++;
		cin>>n>>k;

		LL mn,mx;
		LL dv=0;

		dv=k;
		while(dv&(dv-1)){
			dv-=(dv&(-dv));
		}
		dv<<=1LL;

		mn = (n-k)/dv;
		mx = (n-((dv>>1)^k))/dv;

		cout<<"Case #"<<x<<": "<<mx<<" "<<mn<<endl;
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