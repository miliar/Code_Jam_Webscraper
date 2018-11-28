// Created by alex_mat21. And it works!

#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <queue>
#include <cstring>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <sstream>
#include <stdio.h>
#include <math.h>
#include <bitset>
#include <string> 
#include <iomanip>
#include <cmath>
#include <utility>
 
#define FOR(i,n) for(int i=0,_n=n;i<_n;i++)
#define FORR(i,s,n) for(int i=s,_n=n;i<_n;i++)
#define mp make_pair
#define vi vector<int>
#define fs first
#define sd second
#define pii pair<int,int>

using namespace std;

vector<pair<int,int> > max_flow(vector <vector <vector <int> > > & edge, int nn){
	int n=edge.size();
	vector <vector < vector<int> > > rev;
	for (int i=0; i<n; i++){
		vector <vector <int > > r1;
		rev.push_back(r1);
		}
	for (int i=0; i<n; i++){
		for (int j=0; j<edge[i].size(); j++){
			vector <int> r1;
			r1.push_back(i);
			r1.push_back(j);
			rev[edge[i][j][0]].push_back(r1);
			}
		}
	vector <int> v;
	vector <int> u;
	for (int i=0; i<n; i++){
		v.push_back(-2);
		u.push_back(0);
		}
	vector <int> x;
	int t=1;
	while (t){
		t=0;
		for (int i=0; i<n; i++)
			v[i]=-2;
		v[0]=-1;
		int p=0;
		x.push_back(0);
		while (p<x.size() || x[p]==1){
			for (int j=0; j<edge[x[p]].size(); j++){
				int l=edge[x[p]][j][0];
				if (v[l]==-2 && edge[x[p]][j][2]-edge[x[p]][j][1]>0){
					v[l]=x[p];
					u[l]=j;
					x.push_back(l);
					}
				}
			for (int j=0; j<rev[x[p]].size(); j++){
				int l=rev[x[p]][j][0];
				int k=rev[x[p]][j][1];
				if (v[l]==-2 && edge[l][k][1]>0){
					v[l]=x[p];
					u[l]=-(k+1);
					x.push_back(l);
					}
				}
			p++;
			}
		if (v[1]!=-2){
			t=1;
			int s,s1;
			int l=1;
			s=-1;
			while (l!=0){
				if (u[l]>=0)
					s1=edge[v[l]][u[l]][2]-edge[v[l]][u[l]][1];
				else
					s1=edge[l][-u[l]-1][1];
				l=v[l];
				if (s==-1 || s1<s)
					s=s1;
				}
			l=1;
			while (l!=0){
				if (u[l]>=0)
					edge[v[l]][u[l]][1]+=s;
				else
					edge[l][-u[l]-1][1]-=s;
				l=v[l];
				}
			}
		x.clear();
		}
	vector <pair<int,int> > f_edges;
	for (int i=2; i<2*nn+1; i++) {
		for (int j=0; j<edge[i].size();j++){
		   if (edge[i][j][1]>0)
		      f_edges.push_back(make_pair(i,edge[i][j][0]));
	   }	   
	}
	return f_edges;
	}


int main () {
   int t111;
   cin >> t111;
   
   int n,m,vx,vy;
   int a[100][100];
   int ax[100], ay[100];
   int b[100][100];
   int bx[200], by[200];
   char ch;
   for (int i111=0 ; i111<t111; i111++) {
	   cin >> n >> m;
	   memset(a,0,sizeof a);
	   memset(b,0,sizeof b);
	   for (int i=0; i<m; i++){
	      cin >> ch >> vy >> vx;
	      vy--;
	      vx--;
	      if (ch=='+')
	         b[vx][vy]=1;
	      if (ch=='x')
	         a[vx][vy]=1;
	      if (ch=='o'){
	         a[vx][vy]=1;
	         b[vx][vy]=1;
	      }
	   }
	   memset(ax,0,sizeof ax);
	   memset(ay,0,sizeof ay);
	   for (int i=0; i<n; i++){
	      for (int j=0; j<n; j++){
	         if (a[i][j]==1){
	            ax[i]=1;
	            ay[j]=1;
	         }
	      }
	   }
	   int k=0;
	   for (int i=0; i<n; i++){
	      if (ax[i]==0){
	         while (ay[k]!=0)
	            k++;
	         a[i][k]=2;
	         ay[k]=1;
	      }
	   }
	   memset(bx,0,sizeof bx);
	   memset(by,0,sizeof by);
	   for (int i=0; i<n; i++){
	      for (int j=0; j<n; j++){
	         if (b[i][j]==1){
	            bx[i+j]=1;
	            by[i-j+n-1]=1;
	         }
	      }
	   }
	   vector <vector <vector <int> > > edge;
	   FOR(i,4*n){
	      vector <vector<int> > es;
	      edge.push_back(es);
	   }
	   FOR(i,2*n-1){
	      vector <int> e;
	      e.push_back(i+2);
	      e.push_back(0);
	      e.push_back(1);
	      edge[0].push_back(e);
	   }
	   FOR(i,2*n-1){
	      vector <int> e;
	      e.push_back(1);
	      e.push_back(0);
	      e.push_back(1);
	      edge[i+2*n+1].push_back(e);
	   }
	   FOR(i,2*n-1){
	      if (bx[i]==0){
	         int jl=abs(n-1 -i);
	         int jr=2*n-2 - abs(n-1 -i);
	         //cout << i << ' ' << jl << ' ' << jr << endl;
	         for(int j=jl; j<=jr; j+=2) {
	            if (by[j]==0){
	               vector <int> e;
	               e.push_back(2*n+1+j);
	               e.push_back(0);
	               e.push_back(1); 
	               edge[2+i].push_back(e);
	            }
	         }
	      }
	   }
	   /*FOR(i,edge.size()){
	      FOR(j,edge[i].size()){
	         cout << i << ' ' << edge[i][j][0] << endl;
	      }
	   }*/
	   vector<pair<int, int> > f_edges = max_flow(edge, n);
	   FOR(i,f_edges.size()){
	      int i1 = f_edges[i].first-2;
	      int j1 = f_edges[i].second - (3*n);
	      b[(i1+j1)/2][(i1-j1)/2]=2;
	   }
	   int num=0;
	   vector < vector <int> > ans;
	   FOR(i,n){
	      FOR(j,n){
	         if (a[i][j]>0)
	            num++;
	         if (b[i][j]>0)
	            num++;
	         if (a[i][j]==2 || b[i][j]==2) {
	            vector <int> ans0;
	            if (a[i][j]>0 && b[i][j]>0)
	               ans0.push_back(2);
	            else if (a[i][j]==2)
	               ans0.push_back(0);
	            else
	               ans0.push_back(1);
	            ans0.push_back(j+1);
	            ans0.push_back(i+1);
	            ans.push_back(ans0);
	         }
	      }
	   }
	   cout << "Case #"<< i111 +1 << ": " << num<< ' ' << ans.size() << endl;
	   FOR(i,ans.size()){
	      if (ans[i][0]==0)
	         cout << "x ";
	      if (ans[i][0]==1)
	         cout << "+ ";
	      if (ans[i][0]==2)
	         cout << "o ";
	      cout << ans[i][1] << ' ' << ans[i][2] << endl;
	   }
	}
   return 0;
}
