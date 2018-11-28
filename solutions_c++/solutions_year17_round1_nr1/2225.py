#include <cstring>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <memory.h>
#include <cassert>
#include <complex>



using namespace std;
int dx[8]={1,-1,0,0,1,-1,1,-1};
int dy[8]={0,0,-1,1,1,-1,-1,1};

/*
 -- Valid
 -- const (10^9>sz)
 -- array index
 -- less or more , check if
 -- even or odd
 -- inequality
 */
int t ,r,c;
char g[30][30];
int down[30][30],up[33][33];
bool let[33];
void update(){
	for(int i=0;i<r;i++){
	for(int j=0;j<c;j++){
	if(i){
	if(g[i-1][j]!='?'){
	up[i][j]=1;
	}else{
	up[i][j]=up[i-1][j]+1;
	}
	}else{
	up[i][j]=1;
	}	
	}
	}
   	for(int i=r-1;i>-1;i--){
	for(int j=0;j<c;j++){
	if(i+1<r){
	if(g[i+1][j]!='?'){
	down[i][j]=1;
	}else{
	down[i][j]=down[i+1][j]+1;
	}
	}else{
	down[i][j]=1;
	}	
	}
	}
}
void f(int u,int d,int from,int to,int sr,char c){

	for(int i=0;i<d;i++){
	for(int j=from;j<=to;j++){
	g[sr+i][j]=c;
	}
	}
	for(int i=0;i<u;i++){
	for(int j=from;j<=to;j++){
	g[sr-i][j]=c;
	}
	}
	
}
  

int main(){
	freopen("A-large.in","r",stdin);
	freopen("out1.txt","w",stdout);
	scanf("%d",&t);
	for(int tt=1;tt<=t;tt++){
	cout<<"Case #"<<tt<<":"<<endl;
	scanf("%d%d",&r,&c);
	memset(let,0,sizeof(let)); 
	for(int i=0;i<r;i++){
	for(int j=0;j<c;j++){
	cin>>g[i][j];

	}

	}

	update();
	for(int i=0;i<r;i++){
	for(int j=0;j<c;j++){
	if(g[i][j]!='?'&&!let[g[i][j]-'A']){
	int mn=j,mx=j;
	while(mn>-1&&(g[i][mn]=='?'||g[i][mn]==g[i][j])){
	mn--;
	}
	while(mx<c&&(g[i][mx]=='?'||g[i][mx]==g[i][j])){
	mx++;
	}
	mx--;
	mn++;
	int mn_u=r,mn_d=r;	
	for(int k=mn;k<=mx;k++){
	mn_d=min(mn_d,down[i][k]);
	mn_u=min(mn_u,up[i][k]);
	}
	f(mn_u,mn_d,mn,mx,i,g[i][j]);
	update();
	let[g[i][j]-'A']=1;

	}
	}
	}
	for(int i=0;i<r;i++){
	for(int j=0;j<c;j++){

	cout<<g[i][j];
	}
	cout<<endl;
	}
	
	

	
	}
	

	
    return 0;//rev Ab steps
}