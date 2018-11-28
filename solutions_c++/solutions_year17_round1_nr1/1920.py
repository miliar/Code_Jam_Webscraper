#include <cstdio>
#include <cstring>
#include <string>
#include <map> 
#include <iostream> 
#define rep(i,a,b) for (int i = (a); i <= (b); ++i)
#define rep(i,a,b) for (int i = (a); i <= (b); ++i)
using namespace std;
const int N = 1010;
int k, n, m, l[N], xmin[N], xmax[N], ymin[N], ymax[N];
string s[N];
char str[N][N];
int find(char c){
	return c-'A';
}
bool check(int x,int y,int k){
	rep (i,min(x,xmin[k]),max(x,xmax[k]))
		rep (j,min(y,ymin[k]),max(y,ymax[k]))
			if (str[i][j]!=' ' && str[i][j]!=k+'A'){
				//cout << "fff" << i << " " << j << " " << k << endl; 
				return false;
			}	
		
		rep (i,min(x,xmin[k]),max(x,xmax[k]))
		rep (j,min(y,ymin[k]),max(y,ymax[k])){
			xmin[k] = min(x,xmin[k]);
			ymin[k] = min(y,ymin[k]);
			xmax[k] = max(x,xmax[k]);
			ymax[k] = max(y,ymax[k]);
			str[i][j]=k+'A';
		}
		return true;
}
int main() {
	freopen("A.txt","w",stdout);
	int h, sss, ttt;
	cin >> ttt;
	rep (sss,1,ttt){
		printf("Case #%d:\n",sss);
		memset(xmin,0x3f,sizeof(xmin));
		memset(ymin,0x3f,sizeof(ymin));
		memset(xmax,-1,sizeof(xmax));
	    memset(ymax,-1,sizeof(ymax));
		cin >> n >> m;
		rep (i,1,n){
			cin >> s[i];
		}
		rep (i,1,n)
		rep (j,0,m-1){
			str[i][j] = ' ';
			if (s[i][j]!='?'){
				h = s[i][j] - 'A';
				xmin[h] = min(xmin[h],i);
				xmax[h] = max(xmax[h],i);
				ymin[h] = min(ymin[h],j);
				ymax[h] = max(ymax[h],j);
			}
		}
		
		rep (k,0,25)
		if (ymax[k] != -1){
			//cout << k << endl;
			rep (i,xmin[k],xmax[k])
			rep (j,ymin[k],ymax[k])
				str[i][j] = k+'A';
		}
		rep (i,1,n)
		rep (j,0,m-1)
		if (str[i][j] == ' '){
			//cout << i <<"&&"<< j << endl;
			rep (k,0,25){
				if (ymax[k] != -1 && check(i,j,k))
					break;
			}
		}
		rep (i,1,n){
			str[i][m] = '\0';
			puts(str[i]);
		}
	}
	return 0;
}
