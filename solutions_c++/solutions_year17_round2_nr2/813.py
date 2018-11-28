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
#include <gmpxx.h>

typedef long long ll_t;

using namespace std;
//a = -cp + R, ap = -B + cp + Y, b = -cp + B, bp = cp - R + Y, c = B - cp + R - Y,
#define COMP {  a = -cp + R;ap = cp - B + Y;b = -cp + B;bp = cp - R + Y;c = -cp + B + R - Y;}
bool solve(int R,int Y,int B,string &r)
{
  //fprintf(stdout,"SOLVE %d %d %d\n",R,Y,B);
  int N=Y+R+B;
  r="";
  if(N==0) return 1;
  
  int a,b,c,ap,bp,cp;
  cp=0;
  int ma=R; //a = -cp + R;
  if(ma>B) ma=B; //b = -cp + B;
  if(ma>B+R-Y) ma=B+R-Y; //c = -cp + B + R - Y;

  int mi=B-Y; //ap = cp - B + Y;
  if(mi<R-Y) mi=R-Y; //bp = cp - R + Y;
  if(mi<0) mi=0;
  //cout<<mi<<" - "<<ma<<endl;
  if(mi>ma) return 0;
  cp=mi;
  COMP;
  if(a>=0 && b>=0 && c>=0 && ap>=0 && bp>=0 &&cp>=0) {
  } else {
    assert(0);
  }
  if(R) {r="R";R--;}
  else if(Y) {r="Y";Y--;}
  else if(B) {r="B";B--;}
  for(int i=1;i<N;i++) {
    //cout<< r<< " " << a <<" "<< b << " "<<c << " "<< ap <<" "<< bp <<" "<<cp<<endl; 
    char o=r[r.size()-1];
    if(o=='R') {
      assert(a || cp);
      if((a>0 && Y>B) || cp==0) {
	a--;
	r.push_back('Y'); Y--;
      } else {
	cp--;
	r.push_back('B'); B--;
      }
    }
    if(o=='Y') {
      assert(b || ap);
      if((b>0 && B>R )|| ap==0) {
	b--;
	r.push_back('B'); B--;
      } else {
	ap--;
	r.push_back('R'); R--;
      }
    }
    if(o=='B') {
      assert(c || bp);
      if((c>0 && R>Y) || bp==0) {
	c--;
	r.push_back('R'); R--;
      } else {
	bp--;
	r.push_back('Y'); Y--;
      }
    }
  }
  assert(Y==0 && R==0 && B==0);
  assert(a>=0);
  assert(b>=0);
  assert(c>=0);
  assert(ap>=0);
  assert(bp>=0);
  assert(cp>=0);
  assert(a+b+c+ap+bp+cp==1);
  assert(r.size()==N);
  return 1;
}

string po(string a,int n)
{
  string r;
  for(int i=0;i<n;i++)
    r+=a;
  return r;
  
}

int main() {
  char bf[10000];
  fgets(bf,10000,stdin);
  int ntc;
  int rs=sscanf(bf,"%d",&ntc);
  assert(rs==1);
  for(int tc=1;tc<=ntc;tc++) {
    fgets(bf,10000,stdin);
    int N,R,Y,B,O,V,G;
    rs=sscanf(bf,"%d %d %d %d %d %d %d",&N,&R,&O,&Y,&G,&B,&V);
    assert(rs==7);
    assert(N==R+O+Y+G+B+V);
    //printf("%d %d %d    %d %d %d\n",R,Y,B,V,O,G);
    int Yp=Y-V;
    int Bp=B-O;
    int Rp=R-G;
    if(Yp<0 || Bp<0 || Rp<0) {
      printf("Case #%d: IMPOSSIBLE\n",tc);
    } else {
      string r;
      if(!solve(Rp,Yp,Bp,r)) {
	printf("Case #%d: IMPOSSIBLE\n",tc);
      } else {
	//cerr<<"r='"<<r<<"'"<<endl;
	string r2="";
	if(r=="") {
	  if(V>0) r2=po("YV",V);
	  if(O>0) {if(r2=="") r2=po("BO",O); else r2="IMPOSSIBLE";}
	  if(G>0) {if(r2=="") r2=po("RG",G); else r2="IMPOSSIBLE";}
	  //cerr<<"r2="<<r2<<endl;
	} else {
	  for(int i=0;r[i];i++) {
	    if(r[i]=='Y') {
	      r2+="Y";
	      while(V>0) {r2+="VY";V--;Y--;}
	    }
	    if(r[i]=='B') {
	      r2+="B";
	      while(O>0) {r2+="OB";O--;B--;}
	    }
	    if(r[i]=='R') {
	      r2+="R";
	      while(G>0) {r2+="GR";G--;R--;}
	    }
	  }
	  if(V>0 || O>0 || G>0) r2="IMPOSSIBLE";
	  //cerr<<"r2="<<r2<<endl;
	}
	//printf("%d %s \n",tc,r.c_str());
	printf("Case #%d: %s\n",tc,r2.c_str());
      }
    }
  }

  return 0;
}

//RYBYBYBYRYBYRYBYRBYRBY
