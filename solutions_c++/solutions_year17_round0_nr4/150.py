#include<iostream>
#include<cstdio>
#include<algorithm>
#include<set>
#include<map>
#include<queue>
#include<cassert>
#define PB push_back
#define MP make_pair
#define sz(v) (in((v).size()))
#define forn(i,n) for(in i=0;i<(n);++i)
#define forv(i,v) forn(i,sz(v))
#define fors(i,s) for(auto i=(s).begin();i!=(s).end();++i)
#define all(v) (v).begin(),(v).end()
using namespace std;
typedef long long in;
typedef vector<in> VI;
typedef vector<VI> VVI;
struct eg{
  in dest,c,f,rev;
};
struct flow{
  vector<bool> vtd;
  vector<vector<eg> > egs;
  vector<vector<in> > ept;
  vector<in> dtt;
  in n,s,t,tot,inf;
  void ini(in pn, in ps, in pt){
    n=pn;s=ps;t=pt;
    egs.resize(0);
    ept.resize(0);
    ept.resize(n,vector<in>(0));
    egs.resize(n,vector<eg>(0));
    dtt.resize(0);
    dtt.resize(n);
    tot=0;
    inf=1000000000000000LL;
    vtd.resize(n);
  }
  void add(in a, in b, in c1, in c2=0){
    eg ta,tb;
    ta.dest=b;
    tb.dest=a;
    ta.f=tb.f=0;
    ta.c=c1;
    tb.c=c2;
    ta.rev=egs[b].size()+(a==b);
    tb.rev=egs[a].size();
    egs[a].push_back(ta);
    egs[b].push_back(tb);
  }
  in doit(in u, in lim){
    if(u==t)
      return lim;
    in cfl=0;
    in dlm;
    in pl;
    while(cfl<lim && ept[u].size()>0){
      eg& tp=egs[u][ept[u].back()];
      dlm=lim-cfl;
      if(dlm>tp.c-tp.f)
	dlm=tp.c-tp.f;
      pl=doit(tp.dest,dlm);
      tp.f+=pl;
      egs[tp.dest][tp.rev].f-=pl;
      if(pl<dlm || dlm==0)
	ept[u].pop_back();
      cfl+=pl;
    }
    return cfl;
  }
  in dinic(){
    while(true){
      forn(i,n){
	ept[i].resize(0);
	dtt[i]=inf;
      }
      queue<in> q;
      dtt[t]=0;
      q.push(t);
      while(!q.empty()){
	in u=q.front();
	q.pop();
	forv(i,egs[u]){
	  eg& tp=egs[u][i];
	  if(dtt[tp.dest]<inf)
	    continue;
	  if(egs[tp.dest][tp.rev].c==egs[tp.dest][tp.rev].f)
	    continue;
	  dtt[tp.dest]=dtt[u]+1;
	  q.push(tp.dest);
	}
      }
      forn(i,n)
	vtd[i]=0;
      vtd[s]=1;
      q.push(s);
      while(!q.empty()){
	in u=q.front();
	q.pop();
	forv(i,egs[u]){
	  eg& tp=egs[u][i];
	  if(dtt[tp.dest]+1>dtt[u])
	    continue;
	  if(tp.f==tp.c)
	    continue;
	  ept[u].push_back(i);
	  if(!vtd[tp.dest])
	    q.push(tp.dest);
	  vtd[tp.dest]=1;
	}
      }
      in pl=doit(s,inf);
      if(pl==0)
	break;
      tot+=pl;
    }
    return tot;
  }
};
flow tfl;
VVI orbd;
VVI nubd;
VI usdl,usdt,usdsm,usddf;
void dot(){
  in n,m;
  cin>>n>>m;
  orbd=VVI(n,VI(n));
  char typ;
  in ta,tb;
  in vl;
  usdl=usdt=VI(n);
  usdsm=usddf=VI(2*n-1);
  in ofs=n-1;
  forn(z,m){
    cin>>typ>>ta>>tb;
    vl=2;
    if(typ=='x')
      vl=1;
    if(typ=='o')
      vl=3;
    --ta;
    --tb;
    orbd[ta][tb]|=vl;
    if(vl&1){
      usdl[ta]=1;
      usdt[tb]=1;
    }
    if(vl&2){
      usdsm[ta+tb]=1;
      usddf[ta-tb+ofs]=1;
    }
  }
  nubd=orbd;
  in s=2*n;
  in t=s+1;
  tfl.ini(t+1,s,t);
  forn(i,n){
    if(!usdl[i])
      tfl.add(s,i,1);
    if(!usdt[i])
      tfl.add(i+n,t,1);
  }
  forn(i,n){
    forn(j,n){
      tfl.add(i,j+n,1);
    }
  }
  tfl.dinic();
  forn(i,n){
    forv(j,tfl.egs[i]){
      if(tfl.egs[i][j].f==1)
	nubd[i][tfl.egs[i][j].dest-n]|=1;
    }
  }
  s=2*(2*n-1);
  t=s+1;
  in cpus=2*n-1;
  tfl.ini(t+1,s,t);
  forn(i,cpus){
    if(!usdsm[i])
      tfl.add(s,i,1);
    if(!usddf[i])
      tfl.add(i+cpus,t,1);
  }
  forn(i,n){
    forn(j,n){
      tfl.add(i+j,i-j+ofs+cpus,1);
    }
  }
  tfl.dinic();
  forn(i,cpus){
    forv(j,tfl.egs[i]){
      if(tfl.egs[i][j].f==1){
	nubd[(i+tfl.egs[i][j].dest-ofs-cpus)/2][(i-(tfl.egs[i][j].dest-ofs-cpus))/2]|=2;
      }
    }
  }
  in scr=0;
  VI adx,ady;
  string adtyp;
  string ttyp="ax+o";
  forn(i,n){
    forn(j,n){
      if(nubd[i][j]&1)
	++scr;
      if(nubd[i][j]&2)
	++scr;
      if(nubd[i][j]!=orbd[i][j]){
	adx.PB(i+1);
	ady.PB(j+1);
	adtyp+=ttyp[nubd[i][j]];
      }
    }
  }
  cout<<scr<<" "<<sz(adx)<<endl;
  forv(i,adx){
    cout<<adtyp[i]<<" "<<adx[i]<<" "<<ady[i]<<endl;
  }
}
int main(){
  ios::sync_with_stdio(0);
  cin.tie(0);
  in t;
  cin>>t;
  forn(z,t){
    cout<<"Case #"<<(z+1)<<": ";
    dot();
  }
  return 0;
}
