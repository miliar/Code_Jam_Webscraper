#include<iostream>
#include<cstdio>
#include<algorithm>
#include<set>
#include<stack>
#include<map>
#include<queue>
#include<cassert>
#define ff first
#define ss second
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
template<typename T>
void clr(stack<T>& t){
  while(!t.empty())
    t.pop();
}
struct twosat{
  in mhsh;
  VVI impl;
  stack<in> whr;
  stack<in> hsn;
  stack<in> ci;
  VI vst;
  VI hit;
  stack<in> ts;
  VI comp,psd,gvh;
  void ad(in a, in b){
    impl[a].PB(b);
    impl[neg(b)].PB(neg(a));
  }
  void ini(in n){
    mhsh=n;
    impl=VVI(2*n,VI(0));
  }
  in neg(in h){
    return h>=mhsh?h-mhsh:h+mhsh;
  }
  bool hasol(){
    clr(whr);
    clr(hsn);
    clr(ci);
    vst.clear();
    hit.clear();
    clr(ts);
    comp.clear();
    psd.clear();
    gvh.clear();
    vst.resize(mhsh*2,0);
    hit.resize(mhsh*2,0);
    psd=hit;
    comp.resize(mhsh*2,-1);
    gvh.resize(mhsh*2,0);
    in crn=0;
    in ccp=0;
    forn(z,mhsh*2){
      if(vst[z])
	continue;
      crn++;
      whr.push(z);
      hsn.push(0);
      vst[z]=crn;
      hit[z]=0;
      in chit=1;
      ci.push(0);
      in u,i,ch,v;
      while(!whr.empty()){
	u=whr.top();
	i=ci.top();
	ch=hsn.top();
	gvh[u]=ch;
	if(!psd[u]){
	  ts.push(u);
	  psd[u]=1;
	}
	if(i==sz(impl[u])){
	  if(ch>=hit[u]){
	    while(1){
	      comp[ts.top()]=ccp;
	      ts.pop();
	      if(comp[u]!=-1)
		break;
	    }
	    ccp++;
	  }
	  whr.pop();
	  ci.pop();
	  hsn.pop();
	  continue;
	}
	v=impl[u][i];
	if(vst[v]==0){
	  whr.push(v);
	  hsn.push(chit);
	  ci.push(0);
	  hit[v]=chit++;
	  vst[v]=crn;
	  continue;
	}
	if(vst[v]==crn && comp[v]==-1){
	  if(gvh[v]<ch){
	    hsn.top()=gvh[v];
	  }
	}
	ci.top()++;
      }
    }
    forn(i,mhsh)
      if(comp[i]==comp[neg(i)])
	return 0;
    return 1;
  }
  VVI incomp;
  VI compindeg;
  queue<in> q;
  VI compval;
  void mksol(VI& tvl){
    tvl.resize(mhsh);
    compval.clear();
    incomp.clear();
    compindeg.clear();
    while(!q.empty())
      q.pop();
    in cct=0;
    forv(i,comp)
      cct=max(cct,comp[i]);
    ++cct;
    compval.resize(cct,-1);
    compindeg.resize(cct,0);
    incomp.resize(cct);
    forv(i,comp){
      incomp[comp[i]].PB(i);
      forv(j,impl[i]){
	if(comp[impl[i][j]]!=comp[i])
	  ++compindeg[comp[impl[i][j]]];
      }
    }
    forn(i,cct){
      if(compindeg[i]==0 && compval[i]==-1){
	compval[i]=0;
	compval[comp[neg(incomp[i][0])]]=1;
	q.push(i);
      }
    }
    in u;
    in cspc;
    in cimp;
    while(!q.empty()){
      u=q.front();
      q.pop();
      forv(i,incomp[u]){
	cspc=incomp[u][i];
	if(cspc<mhsh)
	  tvl[cspc]=0;
	else
	  tvl[neg(cspc)]=1;
	forv(j,impl[cspc]){
	  cimp=comp[impl[cspc][j]];
	  --compindeg[cimp];
	  if(compindeg[cimp]==0 && compval[cimp]==-1){
	    compval[cimp]=0;
	    q.push(cimp);
	    compval[comp[neg(incomp[cimp][0])]]=1;
	  }
	}
      }
    }
  }
};
twosat ts;
vector<string> bd;
VVI varid;
VVI d={{1,0},{0,1},{-1,0},{0,-1}};
pair<in,in> rcr(in x, in y, in dr){
  if(bd[x][y]=='#')
    return MP(-1,-1);
  if(bd[x][y]=='.')
    return rcr(x+d[dr][0],y+d[dr][1],dr);
  if(bd[x][y]=='*')
    return MP(varid[x][y],dr%2);
  in ndr=-1;
  if(bd[x][y]=='/'){
    if(dr==0)
      ndr=3;
    if(dr==3)
      ndr=0;
    if(dr==1)
      ndr=2;
    if(dr==2)
      ndr=1;
  }
  if(bd[x][y]=='\\'){
    if(dr==0)
      ndr=1;
    if(dr==1)
      ndr=0;
    if(dr==2)
      ndr=3;
    if(dr==3)
      ndr=2;
  }
  assert(ndr!=-1);
  return rcr(x+d[ndr][0],y+d[ndr][1],ndr);
}
string imp="IMPOSSIBLE";
string pos="POSSIBLE";
void dot(){
  in r,c;
  cin>>r>>c;
  bd.resize(r+2);
  bd[0]=bd[r+1]=string(c+2,'#');
  varid.clear();
  varid.resize(r+2,VI(c+2,-1));
  in nvr=0;
  for(in i=1;i<=r;++i){
    cin>>bd[i];
    bd[i]='#'+bd[i]+'#';
    for(in j=1;j<=c;++j){
      if(bd[i][j]=='-' || bd[i][j]=='|'){
	bd[i][j]='*';
	varid[i][j]=nvr++;
      }
    }
  }
  ts.ini(nvr);
  for(in i=1;i<=r;++i){
    for(in j=1;j<=c;++j){
      if(bd[i][j]!='*')
	continue;
      forn(dr,4){
	if(rcr(i+d[dr][0],j+d[dr][1],dr).ff!=-1){
	  if(dr%2==0)
	    ts.ad(varid[i][j],ts.neg(varid[i][j]));
	  else
	    ts.ad(ts.neg(varid[i][j]),varid[i][j]);
	}
      }
    }
  }
  vector<pair<in,in> > g(4);
  vector<pair<in,in> > pr(2);
  for(in i=1;i<=r;++i){
    for(in j=1;j<=c;++j){
      if(bd[i][j]!='.')
	continue;
      forn(dr,4){
	g[dr]=rcr(i+d[dr][0],j+d[dr][1],dr);
      }
      forn(k,2){
	if((g[k].ff==-1)==(g[k+2].ff==-1)){
	  pr[k]=MP(-1,-1);
	}
	else{
	  if(g[k].ff==-1)
	    pr[k]=g[k+2];
	  else
	    pr[k]=g[k];
	}
      }
      if(pr[0].ff==-1 && pr[1].ff==-1){
	cout<<imp<<endl;
	return;
      }
      if(pr[0].ff==-1){
	swap(pr[0],pr[1]);
      }
      if(pr[1].ff==-1){
	if(pr[0].ss==0){
	  ts.ad(ts.neg(pr[0].ff),pr[0].ff);
	}
	else{
	  ts.ad(pr[0].ff,ts.neg(pr[0].ff));
	}
      }
      else{
	in v1=pr[0].ff;
	if(pr[0].ss==0)
	  v1=ts.neg(v1);
	in v2=pr[1].ff;
	if(pr[1].ss==1)
	  v2=ts.neg(v2);
	ts.ad(v1,v2);
      }
    }
  }
  if(!ts.hasol()){
    cout<<imp<<endl;
    return;
  }
  cout<<pos<<endl;
  VI sol;
  ts.mksol(sol);
  for(in i=1;i<=r;++i){
    for(in j=1;j<=c;++j){
      if(varid[i][j]==-1)
	cout<<bd[i][j];
      else{
	if(sol[varid[i][j]]==1)
	  cout<<"|";
	else
	  cout<<"-";
      }
    }
    cout<<endl;
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
