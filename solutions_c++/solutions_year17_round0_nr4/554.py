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
#include <utility>
using namespace std;

ifstream in("D-small-attempt9.in");
ofstream out("out-d.txt");

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

#define N 104
#define ULL unsigned long long
#define LL long long

char mat[N][N];
int t,n,m;
int cost;
//int left=0,right=0;
pair<char,pair<int,int> > memorable, fk;
		vector<pair<char,pair<int,int> > > res;

void init_mat(int n){
	for(int i=0; i<=n; i++){
		for(int j=0; j<=n; j++){
			mat[i][j]='.';
		}
	}
}

void fill_up_holes(){
	for(int i=1,j=1; j<=n; j++){
		if(mat[i][j]=='.'){
			cost++;
			fk.first='+';
			fk.second.first=i;
			fk.second.second=j;
			res.push_back(fk);
		}
		
	}
}

void fill_down_holes(){
	for(int i=n,j=2; j<n; j++){
		if(mat[i][j]=='.'){
			cost++;
			fk.first='+';
			fk.second.first=i;
			fk.second.second=j;
			res.push_back(fk);
		}
		
	}
}

void left_right_x(){
	int left=0,right=0;

	//left
	for(int i=memorable.second.first+1,j=memorable.second.second-1; i<=n&&j>0;i++,j--){
		left++;
		if(j==1){
			cost+=2;
			fk.first='o';
			fk.second.first=i;
			fk.second.second=j;
			res.push_back(fk);
		}else{
			cost++;
			fk.first='x';
			fk.second.first=i;
			fk.second.second=j;
			res.push_back(fk);
		}
	}

	//right
	for(int i=memorable.second.second+1,j=memorable.second.second+1; i<=n&&j<=n;i++,j++){
	
		if(left==0 && j==n){
			cost+=2;
			fk.first='o';
			fk.second.first=i;
			fk.second.second=j;
			res.push_back(fk);
		}else{
			cost++;
			fk.first='x';
			fk.second.first=i;
			fk.second.second=j;
			res.push_back(fk);
		}
	}
	
}

void left_right_o(){
	//left
	for(int i=memorable.second.first+1,j=memorable.second.second-1; i<=n&&j>0;i++,j--){
		
			cost++;
			fk.first='x';
			fk.second.first=i;
			fk.second.second=j;
			res.push_back(fk);
	}

	//right
	for(int i=memorable.second.second+1,j=memorable.second.second+1; i<=n&&j<=n;i++,j++){
		
		
			cost++;
			fk.first='x';
			fk.second.first=i;
			fk.second.second=j;
			res.push_back(fk);
		
	}
}

void input_taker(){
	cin>>n>>m;
		init_mat(n);
		res.clear();
		cost=0;
		
		memorable.first='.';
		
		for(int i=0; i<m; i++){
			char c;
			int a,b;
			c=0;
			while(!(c=='.' || c=='+' || c=='x' || c=='o')){
				
				cin>>c;
				//cout<<c;
			}
			
			
			cin>>a>>b;
			mat[a][b]=c;

			//cout<<c<<" "<<a<<" "<<b<<endl;
			//cout<<mat[a][b]<<endl;
			
			if(c=='o'){
				cost+=2;
			}else{
 				cost++;
			}
			
			if(c!='+'){
				memorable.first=c;
				memorable.second.first=a;
				memorable.second.second=b;
				if(c=='x'){
					cost++;
					memorable.first=c='o';
					res.push_back(memorable);
				}
			}
		}
}

int main()
{
	xiomod  ob;
	ob.redirect_ouput (string("out-d.txt"));
	ob.redirect_input (string("D-small-attempt9.in"));

	

	cin>>t;

	for(int x=1; x<=t; x++){
		input_taker();

		
		if(memorable.first=='o'){
			left_right_o();

			//fillup the holes
			
			fill_up_holes ();
			fill_down_holes();
		}else if(memorable.first=='.'){

			cost++;
			fk.first='o';
			fk.second.first=1;
			fk.second.second=n;
			res.push_back(fk);

			memorable=fk;
			
			if(mat[1][n]=='.'){
				mat[1][n]='o';
				cost++;
			}
			
			left_right_o ();
			
			//fill down holes
			fill_up_holes ();
			fill_down_holes();
			
		}

		cout<<"Case #"<<x<<": "<<cost<<" "<<res.size()<<endl;
		for(int i=0; i<res.size(); i++){
			cout<<res[i].first<<" "<<res[i].second.first<<" "<<res[i].second.second<<endl;
		}
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