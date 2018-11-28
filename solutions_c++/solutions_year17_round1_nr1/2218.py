#include <iostream>
#include <string>
#include <vector>
#include <cstring>
using namespace std;

const int MAX=26;

int rows, cols;
string grid[MAX];
bool seengrid[MAX][MAX];
bool isinput[MAX][MAX];

void fill(int lowrow, int lowcol, int highrow, int highcol, char c) {
	for(int i=lowrow;i<=highrow;i++) for(int j=lowcol;j<=highcol;j++) {
		grid[i][j]=c; 
		seengrid[i][j]=true;
	}
}

int nextrow(int crow, int lowcol, int highcol) {
	for(int i=crow+1;i<rows;i++) for(int j=lowcol;j<=highcol;j++) if(isinput[i][j]&&grid[i][j]!='?') return i;
	return rows;
}

int prevrow(int crow, int lowcol, int highcol) {
	for(int i=crow-1;i>=0;i--) for(int j=lowcol;j<=highcol;j++) if(grid[i][j]!='?') return i;
	return -1;
}

void doit1() {
	memset(seengrid,false,sizeof(seengrid));
	for(int i=0;i<rows;i++) {
		int last=-1;
		for(int j=0;j<cols;j++) if(grid[i][j]!='?'&&isinput[i][j]) {
			int lowrow=i;
			int lowcol=last+1;
			int highcol=j;
			int highrow=nextrow(i,lowcol,cols-1)-1;
			fill(lowrow,lowcol,highrow,highcol,grid[i][j]);
			last=j;
		}
	}
}

void doit2() {
	memset(seengrid,false,sizeof(seengrid));
	for(int i=rows-1;i>=0;i--) {
		int last=cols;
		for(int j=cols-1;j>=0;j--) if(grid[i][j]!='?') {
			int highrow=i;
			int highcol=last-1;
			int lowcol=j;
			int lowrow=prevrow(i,0,highcol)+1;
			fill(lowrow,lowcol,highrow,highcol,grid[i][j]);
			last=j;
		}
	}
}

void solve(int tc) {
	memset(isinput,false,sizeof(isinput));
	cin>>rows>>cols;
	for(int i=0;i<rows;i++) {
		cin>>grid[i];
		for(int j=0;j<cols;j++) if(grid[i][j]!='?') isinput[i][j]=true;
	}

	doit1();
	doit2();

	cout<<"Case #"<<tc<<":"<<endl;
	for(int i=0;i<rows;i++) cout<<grid[i]<<endl;
}

int main() {
	int cases;
	cin>>cases;
	for(int j=1;j<=cases;j++) solve(j);
}
