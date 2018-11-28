#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>
#include <string>
#include <vector>
#include <map>
#include <list>
#include <set>
#include <iostream>
#include <tuple>
//#include <gmpxx.h>

typedef long long ll_t;

using namespace std;

int r,c;

struct tab_t {
  bool dead;
  tab_t () { dead=0;}
  vector<string> t;
  void toto() {
    for(auto &it:t)
      for(auto &jt:it) {
	if(jt=='-' || jt=='|') jt='B';
      }
  }

  void aff() const{
    for(auto &it:t)
      cout<<it<<endl;
    //cout<<"===== dead="<<dead<<endl;
  }

  int nx(int x,int dir) {
    if(dir==0) return x+1;
    if(dir==2) return x-1;
    return x;
  }

  int ny(int y,int dir) {
    if(dir==1) return y+1;
    if(dir==3) return y-1;
    return y;
  }
  
  void ray(int x,int y,int dir) {
    //printf("ray %d %d %d\n",x,y,dir);
    if(x<0 || y<0 || x>=r || y>=c) return;
    if(t[x][y]=='B' || t[x][y]=='-' || t[x][y]=='|') {
      dead=1;return;
    }
    if(t[x][y]=='#') return;
    if(t[x][y]=='/') return ray(nx(x,dir^3),ny(y,dir^3),dir^3);
    if(t[x][y]=='\\') return ray(nx(x,dir^1),ny(y,dir^1),dir^1);
    if(t[x][y]=='!' && dir%2==0) t[x][y]='+';
    if(t[x][y]=='~' && dir%2==1) t[x][y]='+';
    if(dir%2==0) {t[x][y]='!';}
    if(dir%2==1) {t[x][y]='~';}
    ray(nx(x,dir),ny(y,dir),dir);
  }
  
  tab_t test(int x,int y,int sens) const {
    tab_t r=*this;
    assert(t[x][y]=='B');
    if(sens==0) {
      r.t[x][y]='|';
      r.ray(x+1,y,0);
      r.ray(x-1,y,2);
    }
    if(sens==1) {
      r.t[x][y]='-';
      r.ray(x,y-1,3);
      r.ray(x,y+1,1);
    }
    return r;
  }
};

typedef tuple<int,int,int> ti3;
ti3 op(const ti3 &t)
{
  return ti3(get<0>(t),get<1>(t),1-get<2>(t));
}

int main() {
  char bf[10000];
  fgets(bf,10000,stdin);
  int ntc;
  int rs=sscanf(bf,"%d",&ntc);
  assert(rs==1);
  for(int tc=1;tc<=ntc;tc++) {
    //fgets(bf,10000,stdin);
    fgets(bf,10000,stdin);
    sscanf(bf,"%d %d",&r, &c);
    tab_t t;
    for(int i=0;i<r;i++) {
      fgets(bf,10000,stdin);
      bf[c]=0;
      t.t.push_back(bf);
    }
    //t.aff();
    t.toto();
    //t.aff();
    map<pair<int,int>,int> mp;
    map<pair<int,int>,tab_t> mt[2];
    bool dead=0;
    set<ti3> bb;
    for(int x=0;x<r;x++)
      for(int y=0;y<c;y++)
	if(t.t[x][y]=='B') {
	  auto r=t.test(x,y,0);
	  mp[make_pair(x,y)];
	  if(r.dead==0) {
	    mp[make_pair(x,y)]|=1;
	    mt[0][make_pair(x,y)]=r;
	    //r.aff();
	    bb.insert(ti3(x,y,0));
	  }
	  r=t.test(x,y,1);
	  if(r.dead==0) {
	    mp[make_pair(x,y)]|=2;
	    mt[1][make_pair(x,y)]=r;
	    bb.insert(ti3(x,y,1));
	  }
	  //r.aff();
	  if(mp[make_pair(x,y)]==0) dead=1;
	  if(dead) break;
	}
    bool redo=1;
    set<ti3> tt;
    while(!dead &&redo) {
      map<tuple<int,int,int>,set<tuple<int,int,int> > > mm;
      redo=0;
      for(int x=0;x<r;x++)
	for(int y=0;y<c;y++)
	  if(t.t[x][y]=='.') {
	    int k=0;
	    pair<int,int> pi;
	    int dd;
	    pair<int,int> pi2;
	    int dd2;
	    for(int d=0;d<2;d++)
	      for(auto &it:mt[d]) {
		if((mp[it.first]&(1<<d))==0) continue;
		if(it.second.t[x][y]!='.') {
		  k++;
		  //printf("%d %d : %d %d d=%d \n",x,y,it.first.first,it.first.second,d );
		  if(k==1) {
		    pi=it.first;dd=d;
		  }
		  if(k==2) {
		    pi2=it.first;dd2=d;
		  }
		}
	      }
	    assert(k<=2);
	    if(k==1) {
	      assert(mp[pi]&(1<<dd));
	      if(mp[pi]==3) {
		//fprintf(stderr,"force\n");
		redo=1;
		mp[pi]=(1<<dd);
	      }
	    }
	    if(k==2) {
	      mm[tuple<int,int,int>(pi.first,pi.second,1-dd)].insert(tuple<int,int,int>(pi2.first,pi2.second,dd2));
	      mm[tuple<int,int,int>(pi2.first,pi2.second,1-dd2)].insert(tuple<int,int,int>(pi.first,pi.second,dd));
	    }
	    if(k==0) dead=1;
	  }
      if(redo==0) {
	bb.clear();
	for(auto &it:mp) {
	  if(it.second&1) bb.insert(ti3(it.first.first,it.first.second,0));
	  if(it.second&2) bb.insert(ti3(it.first.first,it.first.second,1));
	}

	tt.clear();
	for(auto &it:bb) {
	  if(tt.find(it)!=tt.end()) continue;
	  if(tt.find(op(it))!=tt.end()) continue;
	  list<ti3> todo;
	  todo.push_back(it);
	  while(!todo.empty()) {
	    ti3 x=todo.front();
	    todo.pop_front();
	    tt.insert(x);
	    for(auto &jt:mm[x]) {
	      if(tt.find(jt)!=tt.end()) continue;
	      if(tt.find(op(jt))!=tt.end()) { dead=1; break;}
	      todo.push_back(jt);
	    }
	  }
	}
      }
    }
    if(dead) cout<<"Case #"<<tc<<": IMPOSSIBLE"<<endl;
    if(dead) continue;

    for(auto &it:bb) {
      if(tt.find(it)!=tt.end()) {
	t.t[get<0>(it)][get<1>(it)]=get<2>(it)?'-':'|';
      }
    }
    
    cout<<"Case #"<<tc<<": POSSIBLE\n";
    t.aff();
    //cout<<endl;
  }

  return 0;
}
