#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <string.h>
#include <string>
//#include <gmpxx.h>
#include <map>
#include <set>
#include <vector>
#include <iostream>
#include <unistd.h>
using namespace std;

#define INF 99999


struct t_t {
  char c;
  char p;
  t_t() {c=' ';p=7;}
  bool valid() const {
    if(c=='+' && (p&1)==0) return false;
    if(c=='x' && (p&2)==0) return false;
    if(c=='o' && (p&4)==0) return false;
    return true;
  }
};


struct tab_t {
  int N;
  t_t t[100][100];
  bool valid() const {
    for(int x=0;x<N;x++)
      for(int y=0;y<N;y++) 
	if(!t[x][y].valid()) return false;
    return true;
  }
  int sc() const {
    int r=0;
    int x,y;
    for(x=0;x<N;x++) {
      for(y=0;y<N;y++) {
	if(t[x][y].c=='+' || t[x][y].c=='x')r++;
	if(t[x][y].c=='o') r+=2;
      }
    }
    return r;
  }
  void aff() {
    int x,y;
    for(x=0;x<N;x++) {
      for(y=0;y<N;y++) {
	fprintf(stderr,"%c%d",t[x][y].c,t[x][y].p);
      }
      fprintf(stderr,"\n");
    }
    fprintf(stderr,"----\n");
  }

  bool choose(int &x,int &y,char &c) const {
    for(x=0;x<N;x++) 
      for(y=0;y<N;y++) {
	assert(t[x][y].valid());
	if(t[x][y].p==0) continue;
	if(t[x][y].p&4 && t[x][y].c!='o') {c='o'; return 1;}
      }
    return 0;
    for(x=0;x<N;x++) 
      for(y=0;y<N;y++) {
	assert(t[x][y].valid());
	if(t[x][y].p==0) continue;
	//if(t[x][y].p&4 && t[x][y].c!='o') {c='o'; return 1;}
	if(t[x][y].p&1 && t[x][y].c!='+') {c='+'; return 1;}
	if(t[x][y].p&2 && t[x][y].c!='x') {c='x'; return 1;}
      }
    return 0;
  }
  bool ok(int x,int y) {
    return x>=0 && y>=0 && x<N && y<N;
  }
  void up(int x,int y,char c)
  {
    t[x][y].c=c;
    assert(t[x][y].valid());
    up_(x,y);
  }
  void up_(int x,int y) {
    if(t[x][y].c=='+' || t[x][y].c=='o') {
      for(int j=-N;j<=N;j++) {
	if(j==0) continue;
	int xx=x+j;
	int yy=y+j;
	if(ok(xx,yy)) t[xx][yy].p&=2;
	xx=x+j;
	yy=y-j;
	if(ok(xx,yy)) t[xx][yy].p&=2;
      }
    }
    if(t[x][y].c=='x' || t[x][y].c=='o') {
      for(int j=-N;j<=N;j++) {
	if(j==0) continue;
	int xx=x+j;
	int yy=y;
	if(ok(xx,yy)) t[xx][yy].p&=1;
	xx=x;
	yy=y+j;
	if(ok(xx,yy)) t[xx][yy].p&=1;
      }
    }
    if(t[x][y].c=='+')  t[x][y].p&=1+4;
    if(t[x][y].c=='x')  t[x][y].p&=2+4;
    if(t[x][y].c=='o')  t[x][y].p&=4;
  }
};

void up(char &c,char n) {
  if(n=='+') {
    if(c=='x'||c=='o') c='o';
    else c='+';
    return;
  }
  if(n=='x') {
    if(c=='+'||c=='o') c='o';
    else c='x';
    return;
  }
  assert(0);
}

int main() {
  char bf[10000];
  fgets(bf,9999,stdin);
  int ntc;
  int sr=sscanf(bf,"%d",&ntc);
  assert(sr==1);
  for(int tc=1;tc<=ntc;tc++) {
    fgets(bf,9999,stdin);
    int m;
    int n;
    sr=sscanf(bf,"%d %d",&n,&m);
    assert(sr==2);

    map<pair<int,int>,char> morig,mnew;
    set<int> opp,npp,npp2;
    int pp[200];
    int pb[400];
    set<int> forb;
    
    for(int i=0;i<n;i++) {
      pp[i]=-1;
      npp.insert(i);
      npp2.insert(i);

      pb[2*i]=INF;
      pb[2*i+1]=INF;
    }

    for(int a=0;a<m;a++) {
      fgets(bf,9999,stdin);
      char c;
      int x,y;
      sr=sscanf(bf,"%c %d %d",&c,&x,&y);
      assert(sr==3);
      x-=1;
      y-=1;
      assert(morig.find(make_pair(x,y))==morig.end());
      morig[make_pair(x,y)]=c;
      if(c!='+') {
	assert(pp[x]<0);
	opp.insert(x);
	npp.erase(x);
	npp2.erase(y);
	pp[x]=y;
      }
      if(c!='x') {
	assert(pb[x+y]==INF);
	pb[x+y]=x-y;
	forb.insert(x-y);
      }
    }
    while(!npp.empty()) {
      int x=*(npp.begin());
      int y=*(npp2.begin());
      assert(pp[x]<0);
      pp[x]=y;
      npp.erase(x);
      npp2.erase(y);
    }
    assert(npp2.empty());

    
    for(int j=0;j<n;j++)
      for(int d=-1;d<=1;d+=2) {
	int xy=n-1+d*j;
	if(pb[xy]!=INF) continue;
	int mi=INF,ma=INF;
	for(int xy2=-n-1;xy2<=n-1;xy2++) {
	  if(forb.find(xy2)!=forb.end()) continue;
	  int x=(xy+xy2);
	  int y=(xy-xy2);
	  if(x%2) continue;
	  assert(y%2==0);
	  x/=2;y/=2;
	  if(x<0 || y<0 || x>=n || y>=n) continue;
	  if(mi==INF) mi=xy2;
	  ma=xy2;
	}
	if(mi==INF) continue;
	int xy2=mi;
	if(abs(ma)>abs(mi)) xy2=ma;
	pb[xy]=xy2;
	forb.insert(xy2);
      }

    for(int x=0;x<n;x++) {
      up(mnew[make_pair(x,pp[x])],'x');
    }
    
    int b=0;

    for(int xy=0;xy<2*n-1;xy++) {
      int xy2=pb[xy];
      if(xy2==INF) continue;
      b++;

      int x=(xy+xy2);
      int y=(xy-xy2);
      assert(x%2==0);
      assert(y%2==0);
      x/=2;y/=2;
      assert(x>=0 && y>=0 && x<n && y<n);
      up(mnew[make_pair(x,y)],'+');
    }

    /*
    for(auto &it:morig) {
      cout<<it.second << " " <<mnew.at(it.first)<<endl;
    }
    continue;
    */
    
    tab_t t;
    t.N=n;
    for(auto &it:mnew) {
      t.up(it.first.first,it.first.second,it.second);
    }
    assert(t.valid());
    assert(t.sc() == n+b);
    //continue;
    
    cout<<"Case #"<<tc<<": ";
    vector<tuple<int,int,char> > v;
    for(auto &it:mnew) {
      if(morig[it.first]==it.second) continue;
      v.push_back(tuple<int,int,char>(it.first.first,it.first.second,it.second));
    }
    cout<<n+b<<" "<<v.size()<<endl;
    for(auto &it:v) {
      cout<<get<2>(it)<<" "<<get<0>(it)+1<<" "<<get<1>(it)+1<<endl;
    }
  }
  return 0;
}
