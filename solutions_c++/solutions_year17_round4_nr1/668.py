#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <iostream>
#include <tuple>
//#include <gmpxx.h>

typedef long long ll_t;

using namespace std;


int b[101][101][101][4];

void toto(int &i, int j)
{
  if(j<0) return;
  if(i<0) {i=j;return;}
  if(i<j) i=j;
}

int main() {
  char bf[10000];
  fgets(bf,10000,stdin);
  int ntc;
  int rs=sscanf(bf,"%d",&ntc);
  assert(rs==1);
  for(int tc=1;tc<=ntc;tc++) {
    int n, p;
    cin>> n>>p;
    int ng[4]={0,0,0,0};
    int t[4]={0,0,0,0};

    for(int i=0;i<n;i++) {
      int a;
      cin>> a;
      t[a%p]++;
    }
    assert(n<=100);
    assert(p<=4);
    
    //memset(b,0,sizeof(b));
    
    for(int i=0;i<=n;i++)
      for(int j=0;j<=n;j++)
	for(int k=0;k<=n;k++) {
	  for(int l=0;l<4;l++)
	    b[i][j][k][l]=-20;
	}
    
    b[0][0][0][0]=0;

    if(p==4) {
      for(int i=0;i<=n;i++)
	for(int j=0;j+i<=n;j++)
	  for(int k=0;k+i+j<=n;k++) {
	    for(int l=0;l<p;l++) {
	      int d=0;
	      if(l==0)d=1; 
	      if(i) toto(b[i][j][k][(l+1)%p],b[i-1][j][k][l]+d);
	      if(j) toto(b[i][j][k][(l+2)%p],b[i][j-1][k][l]+d);
	      if(k) toto(b[i][j][k][(l+3)%p],b[i][j][k-1][l]+d);
	      
	    }
	  }
    }
    if(p==3) {
      int k=0;
      for(int i=0;i<=n;i++)
	for(int j=0;j+i<=n;j++)
	  for(int l=0;l<p;l++) {
	    int d=0;
	    if(l==0)d=1; 
	    if(i) toto(b[i][j][k][(l+1)%p],b[i-1][j][k][l]+d);
	    if(j) toto(b[i][j][k][(l+2)%p],b[i][j-1][k][l]+d);
	    
	  }
    }
    if(p==2) {
      int j=0,k=0;
      for(int i=0;i<=n;i++)
	for(int l=0;l<p;l++) {
	  int d=0;
	  if(l==0)d=1; 
	  if(i) toto(b[i][j][k][(l+1)%p],b[i-1][j][k][l]+d);
	}
    }
    
    //fgets(bf,10000,stdin);
    
    cout<<"Case #"<<tc<<": ";
    int r=-1;
    for(int i=0;i<4;i++) {
      if(b[t[1]][t[2]][t[3]][i]>=0) r=b[t[1]][t[2]][t[3]][i];
    }
    cout<<t[0]+r<<endl;
  }

  return 0;
}
