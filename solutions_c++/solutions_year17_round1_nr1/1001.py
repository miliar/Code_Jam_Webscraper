#include <stdio.h>
#include <cstring>
#include <fstream>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

int m,n;
char mp[30][30];
char b[30][30];

int num(int x1,int y1,int x2,int y2){
	vector<char> c;
	if(x1>x2||y1>y2) return -1;
	for(int i=x1;i<=x2;i++){
		for(int j=y1;j<=y2;j++){
            int k;
			if(mp[i][j]=='?') continue;
			if(c.size()==0) {c.push_back(mp[i][j]);continue;}
			for(k=0;k<c.size();k++){
				if(c[k]==mp[i][j]) break;
			}
			if(k==c.size()) c.push_back(mp[i][j]);
		}
	}
	return c.size();
}

char whatis(int x1,int y1,int x2,int y2){
	for(int i=x1;i<=x2;i++){
		for(int j=y1;j<=y2;j++){
			if(mp[i][j]=='?') continue;
			return mp[i][j];
		}
	}
}

void makematrix(int x,int y){
	if(x<0||y<0||x>m||y>n) return;
	if(!b[x][y]) return;
	int a=x,b=y,c=x,e=y;
	while(a>=0&&num(a,b,c,e)<=1) a--;a++;
	while(b>=0&&num(a,b,c,e)<=1) b--;b++;
	while(c<m&&num(a,b,c,e)<=1) c++;c--;
	while(e<n&&num(a,b,c,e)<=1) e++;e--;
	char temp=whatis(a,b,c,e);
	for(int i=a;i<=c;i++){
		for(int j=b;j<=e;j++){
			mp[i][j]=temp;
		}
	}
}

int main(){
    ifstream filei("A.in");
	ofstream file("A.out");
	int T,temp;
	filei>>T;
	for(int i=0;i<T;i++){
		filei>>m>>n;
		for(int j=0;j<m;j++){
			for(int k=0;k<n;k++){
				filei>>mp[j][k];
				if(mp[j][k]!='?') b[j][k]=1;
				else b[j][k]=0;
			}
		}
		for(int j=m-1;j>=0;j--){
			for(int k=n-1;k>=0;k--){
				makematrix(j,k);
			}
		}
		file<<"Case #"<<i+1<<":"<<endl;
		for(int j=0;j<m;j++){
			for(int k=0;k<n;k++){
				file<<mp[j][k];
			}
			file<<endl;
		}

	}
	file.close();filei.close();
	return 0;
}
