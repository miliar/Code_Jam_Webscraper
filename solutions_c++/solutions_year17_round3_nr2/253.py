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

int tab[1440+10][1440+10][2];

char w[1440+10];

void toto(int &i,int j)
{
  //printf("%d %d\n",i,j);
  if(i<0 || i>j) i=j;
}

int main() {
  char bf[10000];
  fgets(bf,10000,stdin);
  int ntc;
  int rs=sscanf(bf,"%d",&ntc);
  assert(rs==1);
  for(int tc=1;tc<=ntc;tc++) {
    memset(tab,-1,sizeof(tab));
    memset(w,' ',1440);
    w[1440]=0;

    //fgets(bf,10000,stdin);
    int A,B;
    fgets(bf,10000,stdin);      
    rs=sscanf(bf,"%d %d",&A,&B);
    //fprintf(stderr,"n=%d k=%d\n",n,k);
    assert(rs==2);
    for(int i=0;i<A;i++) {
      int d,f;
      fgets(bf,10000,stdin);      
      rs=sscanf(bf,"%d %d",&d,&f);
      //fprintf(stderr,"n=%d k=%d\n",n,k);
      assert(rs==2);
      for(int j=d;j<f;j++)
	w[j]='A';
    }
    for(int i=0;i<B;i++) {
      int d,f;
      fgets(bf,10000,stdin);      
      rs=sscanf(bf,"%d %d",&d,&f);
      //fprintf(stderr,"n=%d k=%d\n",n,k);
      assert(rs==2);
      for(int j=d;j<f;j++) {
	assert(w[j]==' ');
	w[j]='B';
      }
    }
    //cout<<w<<endl;

    for(int t=1;t<=1440;t++) 
      for(int l=0;l<=1400;l++) 
	tab[t][l][0]=-1;
    for(int t=1;t<=1440;t++) 
      for(int l=0;l<=1400;l++) 
	tab[t][l][1]=-1;

    int re=-1;
    for(int dd=0;dd<2;dd++) {
      for(int t=1;t<=1440;t++) 
	for(int l=0;l<=721;l++) 
	  tab[t][l][0]=-1;
      for(int t=1;t<=1440;t++) 
	for(int l=0;l<=721;l++) 
	  tab[t][l][1]=-1;
      
      tab[0][0][0]=dd;
      tab[0][0][1]=1-dd;
      for(int t=1;t<=1440;t++) {
	for(int l=0;l<=t;l++) {
	  if(l>720) break;
	  for(int d=0;d<2;d++) {
	    for(int d2=0;d2<2;d2++) {
	      if(l-d2>=0 && tab[t-1][l-d2][d]>=0 && w[t-1]!='A'+d2) {
		//if(l==t/2) printf("%d %d %d %d\n",t,l,d,d2);
		toto(tab[t][l][d2],tab[t-1][l-d2][d]+(d!=d2));
	      }
	    }
	  }
	}
	/*for(int i=0;i<t;i++)
	  printf("%d ",tab[t][i][0]);
	  cout<<endl;
	*/
      }
      //cout<<tab[1440][720][0]<<endl;
      //cout<<tab[1440][720][1]<<endl;
      
      if(tab[1440][720][0]>=0)
	toto(re,tab[1440][720][0]+(dd!=0));
      if(tab[1440][720][1]>=0)
	toto(re,tab[1440][720][1]+(dd!=1));
    }
    
    cout<<"Case #"<<tc<<": "<<re;
    
    cout<<endl;
  }
  return 0;
}
