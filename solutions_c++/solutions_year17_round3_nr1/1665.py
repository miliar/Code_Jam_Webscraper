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
#include <list>
#include <utility>
#include <iomanip>
using namespace std;

ifstream in("A-large (2).in");
ofstream out("out-c-a.txt");

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

#define N 1001
#define LL unsigned long long
#define LD long double
#define PI 3.141592653589793238463L

LL n,k;
LL mat[N][N];
pair<LL,LL> inp[N];
LL mx_k[N];

void init_mat(LL n){
	for(int i=0; i<=n; i++){
		for(int j=0; j<=n; j++){
			mat[i][j]=0;
		}
	}
}

bool my_cmp(pair<LL,LL> &a, pair<LL,LL> &b){
	if(a.first==b.first){
		return a.second>b.second;
	}
	return a.first>b.first;
}

LL my_mn(LL a, LL b){
	if(a<b)return a;
	return b;
}

LL my_mx(LL a, LL b){
	if(a>b)return a;
	return b;
}


int main()
{
	xiomod  ob;
	ob.redirect_input (string("A-large (2).in"));
	ob.redirect_ouput (string("out-c-a.txt"));
	int t;
	cin>>t;
	for(int x=1; x<=t; x++){
		cin>>n>>k;
		for(int i=0; i<n; i++){
			cin>>inp[i].first>>inp[i].second;
		}

		init_mat(n);
		for(int i=0; i<=k; i++){
			mx_k[i]=0;
		}
		

		sort(inp, inp+n, my_cmp);

		for(int i=n-1; i>=0; i--){
			mat[i][1]=inp[i].first*inp[i].second;
	
			for(int j=2; j<=k&&j<=(n-i); j++){
				mat[i][j]=mx_k[j-1]+mat[i][1];
			}

			for(int j=1; j<=k; j++){
				mx_k[j]=my_mx(mx_k[j], mat[i][j]);
			}
		}
		LL res=0;
		for(int i=0;i<n; i++){
			res=my_mx(res, 2*mat[i][k]+inp[i].first*inp[i].first);
		}

		cout<<setprecision(9);
		cout<<fixed;
		cout<<"Case #"<<x<<": "<<(((LD)res)*PI)<<endl;
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