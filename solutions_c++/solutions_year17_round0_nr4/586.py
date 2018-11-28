#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <fstream>
#include <vector>
#include <iostream>

using namespace std;

vector< vector<char> > res;
int point;
vector<char> comchar;
vector< vector<int> > comint;
vector< vector<char> > original;
vector< vector<int> > pos;
int gap=0;

ofstream ak("4_1.out");
ifstream sk("4.in");

vector< vector<int> > posnew(vector< vector<char> > &s){
	int n=s.size();
	return vector< vector<int> >(n,vector<int>(n,7));
}

void updatepos(vector< vector<char> > &s){
	pos=posnew(s);
	int n=s.size();
	int x,y;
	for(int i=0;i<n;i++){
		for(int j=0;j<n;j++){
			if(s[i][j]=='.') continue;
			if(s[i][j]=='+') //xie x
			{
				pos[i][j]=0;
				x=i+1;
				y=j+1;
				while(x>=0&&y>=0&&x<n&&y<n){
					pos[x][y]=pos[x][y]&2;
					x++;
					y++;
				}
				x=i-1;
				y=j-1;
				while(x>=0&&y>=0&&x<n&&y<n){
					pos[x][y]=pos[x][y]&2;
					x--;
					y--;
				}
				x=i+1;
				y=j-1;
				while(x>=0&&y>=0&&x<n&&y<n){
					pos[x][y]=pos[x][y]&2;
					x++;
					y--;
				}
				x=i-1;
				y=j+1;
				while(x>=0&&y>=0&&x<n&&y<n){
					pos[x][y]=pos[x][y]&2;
					x--;
					y++;
				}
			}
			if(s[i][j]=='x') //hengshu +
			{
				pos[i][j]=0;
				for(int k=0;k<n;k++){
					pos[i][k]=pos[i][k]&4;
					pos[k][j]=pos[k][j]&4;
				}
			}
			if(s[i][j]=='o') //xie x hengshu +
			{
				pos[i][j]=0;
				x=i+1;
				y=j+1;
				while(x>=0&&y>=0&&x<n&&y<n){
					pos[x][y]=pos[x][y]&2;
					x++;
					y++;
				}
				x=i-1;
				y=j-1;
				while(x>=0&&y>=0&&x<n&&y<n){
					pos[x][y]=pos[x][y]&2;
					x--;
					y--;
				}
				x=i+1;
				y=j-1;
				while(x>=0&&y>=0&&x<n&&y<n){
					pos[x][y]=pos[x][y]&2;
					x++;
					y--;
				}
				x=i-1;
				y=j+1;
				while(x>=0&&y>=0&&x<n&&y<n){
					pos[x][y]=pos[x][y]&2;
					x--;
					y++;
				}
				for(int k=0;k<n;k++){
					pos[i][k]=pos[i][k]&4;
					pos[k][j]=pos[k][j]&4;
				}
			}
		}
	}
}

bool checkboard(vector< vector<char> > &s){
	int n=s.size();
	for(int i=0;i<n;i++){
		int all=0;
		for(int j=0;j<n;j++){
			if(s[i][j]=='x') all++;
			if(s[i][j]=='o') all++;
			if(all>1) return 0;
		}
	}
	for(int i=0;i<n;i++){
		int all=0;
		for(int j=0;j<n;j++){
			if(s[j][i]=='x') all++;
			if(s[j][i]=='o') all++;
			if(all>1) return 0;
		}
	}
	int r=0;
	while(r<2*n-1){
		int all=0;
		int x,y;
		if(r<=n-1){
			x=r;
			y=0;
		}
		else{
			x=n-1;
			y=r-n+1;
		}
		while(x>=0&&y>=0&&x<n&&y<n){
			if(s[x][y]=='+') all++;
			if(s[x][y]=='o') all++;
			if(all>1) return 0;
			x--;
			y++;
		}
		r++;
	}
	r=0;
	while(r<2*n-1){
		int all=0;
		int x,y;
		if(r<=n-1){
			x=0;
			y=n-1-r;
		}
		else{
			x=r-n+1;
			y=0;
		}
		while(x>=0&&y>=0&&x<n&&y<n){
			if(s[x][y]=='+') all++;
			if(s[x][y]=='o') all++;
			if(all>1) return 0;
			x++;
			y++;
		}
		r++;
	}
	return 1;
}

int costboard(vector< vector<char> > &s){
	int c=0;
	for(int j=0;j<(int)s.size();j++){
		for(int k=0;k<(int)s[j].size();k++){
			if(s[j][k]=='+'||s[j][k]=='x') c++;
			if(s[j][k]=='o') c+=2;
		}
	}
	return c;
}

void printboard(vector< vector<char> > &s){
	for(int j=0;j<(int)s.size();j++){
		for(int k=0;k<(int)s[j].size();k++){
			cout<<s[j][k]<<" ";
		}
		cout<<endl;
	}
	cout<<endl;
}

void printpos(vector< vector<int> > &s){
	for(int j=0;j<(int)s.size();j++){
		for(int k=0;k<(int)s[j].size();k++){
			cout<<s[j][k]<<" ";
		}
		cout<<endl;
	}
	cout<<endl;
}

void searchboard(vector< vector<char> > &s,int x,int y){
	//printboard(s);
	//cout<<endl;
	int n=s.size();
	if(costboard(res)>3*n-2) return;
	if(x>0&&costboard(s)+2*n-x-1<3*n-2) return;
	if(checkboard(s)){
		int c=costboard(s);
		if(point<c){
			point=c;
			res.assign(s.begin(),s.end());
		}
		updatepos(s);
		//printpos(pos);
		for(int i=0;i<n;i++){
			for(int j=0;j<n;j++){
				if(i<x) continue;
				else if(i==x&&j<y) continue;
				if(pos[i][j]>0){
					if((pos[i][j]&1)==1){
						s[i][j]='o';
						searchboard(s,i,j);
						s[i][j]='.';
						updatepos(s);
					}
					if((pos[i][j]&2)==2){
						s[i][j]='x';
						searchboard(s,i,j);
						s[i][j]='.';
						updatepos(s);
					}
					if((pos[i][j]&4)==4){
						s[i][j]='+';
						searchboard(s,i,j);
						s[i][j]='.';
						updatepos(s);
					}
				}
			}
		}
	}
}

void changeboard(vector< vector<char> > &s,int x,int y){
	int n=s.size();
	if(checkboard(s)){
		searchboard(s,0,0);
	}
	for(int i=0;i<n;i++){
		for(int j=0;j<n;j++){
			if(i<x) continue;
			else if(i==x&&j<y) continue;
			if(s[i][j]=='+'){
				s[i][j]='o';
				changeboard(s,i,j);
				s[i][j]='+';
			}
			if(s[i][j]=='x'){
				s[i][j]='o';
				changeboard(s,i,j);
				s[i][j]='x';
			}
		}
	}
}

int compareboard(vector< vector<char> > &s,vector< vector<char> > &o){
	int n=s.size();
	comint.clear();
	comchar.clear();
	vector<int> temp;
	for(int i=0;i<n;i++){
		for(int j=0;j<n;j++){
			if(s[i][j]!=o[i][j]){
				temp.clear();
				comchar.push_back(s[i][j]);
				temp.push_back(i+1);
				temp.push_back(j+1);
				comint.push_back(temp);
			}
		}
	}
	return (int)comchar.size();
}

void printcom(){
	int n=comchar.size();
	for(int i=0;i<n;i++){
		ak<<comchar[i]<<" "<<comint[i][0]<<" "<<comint[i][1]<<endl;
	}
}

void addboard(vector< vector<char> > &s){
	int n=s.size();
	int flag=0;
	int pp;
	for(int i=0;i<n;i++){
		if(s[0][i]=='.') s[0][i]='+';
		else if(s[0][i]=='o') {flag=2;pp=i;}
		else if(s[0][i]=='x') {flag=1;pp=i;}
	}
	if(flag==0){
		s[0][0]='o';
		pp=0;
		flag=2;
	}
	if(flag==1){
		if(pp==0){
			for(int j=1;j<n-1;j++){
				s[j][j]='x';
				s[n-1][j]='+';
			}
			s[n-1][n-1]='o';

		}
		else if(pp==1){
			for(int j=2;j<n;j++){
				s[j][j]='x';
			}
			s[1][0]='o';
			s[n-2][n-1]='+';
			for(int j=1;j<n-2;j++){
				s[n-1][j]='+';
			}
		}
		else if(pp==n-1){
			for(int j=0;j<n-2;j++){
				s[j+1][j]='x';
				s[n-1][j]='+';
			}
			s[n-1][n-2]='o';
		}
		else{
			int p=1,q=0;
			while(p<n){
				if(q==pp){
					q++;
					continue;
				}
				s[p][q]='x';
				p++;
				q++;
			}
			for(int j=1;j<n-1;j++){
				s[n-1][j]='+';
			}
			s[pp][0]='+';
			s[n-1-pp][n-1]='+';
			s[n-1][n-1-pp]='.';
		}
	}
	else{
		if(pp!=n-1){
			int j=1,k=0;
			while(j<n){
				if(s[0][k]=='o'){
					k++;
					continue;
				}
				s[j][k]='x';
				j++;
				k++;
			}
			for(int m=1;m<n-1;m++){
				s[n-1][m]='+';
			}
		}
		else{
			if(n==1){
				s[0][0]='o';
			}
			else{
				for(int j=1;j<n-2;j++){
					s[n-1][j]='+';
				}
				for(int j=0;j<n-2;j++){
					s[j+1][j]='x';
				}
				s[n-1][n-2]='o';
			}
		}
	}

}

int main(){
	int n;
	sk>>n;
	vector< vector< vector<char> > > c;
	for(int i=0;i<n;i++){
		int m,k;
		sk>>m>>k;
		vector< vector<char> > s(m,vector<char>(m,'.'));
		for(int j=0;j<k;j++){
			char t;
			int p,q;
			sk>>t>>p>>q;
			s[p-1][q-1]=t;
		}
		c.push_back(s);
	}
	for(int i=0;i<n;i++){
		point=0;
		res.clear();
		comint.clear();
		comchar.clear();
		original.clear();
		pos.clear();
		original.assign(c[i].begin(),c[i].end());
		//printboard(c[i]);
		if(c[i].size()<4){
			changeboard(c[i],0,0);
		}
		else{
			addboard(c[i]);
			searchboard(c[i],0,0);
		}
		if(res.size()==0){
			cout<<"error!"<<endl;
			cout<<i<<endl;
			cout<<c[i].size()<<endl;
			return 0;
		}
		//printboard(res);
		if(c[i].size()>1&&point!=c[i].size()*3-2){
			cout<<"error!"<<endl;
			cout<<i<<endl;
			cout<<c[i].size()<<" "<<i+1<<endl;
			return 0;
		}
		ak<<"Case #"<<i+1<<": "<<point<<" "<<compareboard(res, original)<<endl;
		printcom();
	}
	sk.close();
	ak.close();
}

/*
1
3 4
+ 2 3
+ 2 1
x 3 1
+ 2 2
*/
