/*
 * test.cpp
 *
 *  Created on: Sep 26, 2016
 *      Author: SCE15-0683
 */

#include<iostream>
#include<cstdio>
#include<vector>
#include<algorithm>
#include<queue>
#include<string>
#include<map>
#include<cmath>
#include<bitset>
#include<set>
#include<iomanip>
#include<fstream>
#include<bitset>
#include<cstring>
#include<cstdlib>
#include<complex>
#include<list>
#include<sstream>

using namespace std;

typedef pair<int,int> ii;
typedef pair<int,long long> il;
typedef pair<long long,long long> ll;
typedef pair<ll,int> lli;
typedef pair<long long,int> li;
typedef pair<double,double> dd;
typedef pair<ii,int> iii;
typedef pair<double,int> di;
long long mod = 1000000007LL;
long long base = 37;
long long large = 1000000000000000000LL;

int main(){
	int tt;
	int test=0;
	cin>>tt;
	ofstream out;
	out.open("result.txt");
	while(tt--){
		test++;
		out<<"Case #"<<test<<": ";
		int n,m;
		cin>>n>>m;
		vector<vector<char> > g;
		g.assign(n,vector<char>(m,'0'));
		for(int i=0;i<n;i++){
			for(int j=0;j<m;j++){
				cin>>g[i][j];
			}
		}

		vector<int> rmax(26,0),rmin,cmin,cmax;
		rmax.assign(26,0);
		cmax=rmax;
		rmin.assign(26,10000);
		cmin=rmin;
		for(int i=0;i<n;i++){
			for(int j=0;j<m;j++){
				if(g[i][j]=='?') continue;
				int d = (int)(g[i][j]-'A');
				rmax[d]=max(rmax[d],i);
				rmin[d]=min(rmin[d],i);
				cmin[d]=min(cmin[d],j);
				cmax[d]=max(cmax[d],j);
			}
		}
		for(int c=0;c<26;c++){
			for(int i=rmin[c];i<=rmax[c];i++){
				for(int j=cmin[c];j<=cmax[c];j++){
					g[i][j]=(char)('A'+c);
				}
			}
		}
		/*out<<endl;
		for(int i=0;i<n;i++){
			for(int j=0;j<m;j++) out<<g[i][j];
			out<<endl;
		}*/
		for(int i=0;i<n;i++){
			char pre = '0';
			for(int j=0;j<m;j++){
				if(g[i][j]!='?') {
					pre = g[i][j];
					break;
				}
			}
			if(pre=='0') continue;
			for(int j=0;j<m;j++){
				if(g[i][j]=='?') g[i][j]=pre;
				else pre = g[i][j];
			}
		}
		/*for(int i=0;i<n;i++){
			for(int j=0;j<m;j++) cout<<g[i][j];
			cout<<endl;
		}*/
		for(int j=0;j<m;j++){
			char pre ;
			for(int i=0;i<n;i++){
				if(g[i][j]!='?'){
					pre = g[i][j];
					break;
				}
			}
			for(int i=0;i<n;i++){
				if(g[i][j]=='?'){
					g[i][j]=pre;
				}else{
					pre=g[i][j];
				}
			}
		}
		out<<endl;
		for(int i=0;i<n;i++){
			for(int j=0;j<m;j++) out<<g[i][j];
			out<<endl;
		}

	}
	out.close();
	return 0;
}
