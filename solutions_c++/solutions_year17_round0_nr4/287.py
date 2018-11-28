#include <cstdio>
#include <cassert>
#include <vector>
#include <algorithm>
using namespace std;

int N;
int calccheck(vector<vector<char> > const& s) {
  int ret=0;
  vector<char> Row(N,0),Col(N,0),DiSum(2*N-1,0),DiDif(2*N-1,0); // dif offs. by N-1
  for (int r=0;r<N;++r) {
    for (int c=0;c<N;++c) {
      if (s[r][c]=='x') { assert(Row[r]==0 && Col[c]==0); Row[r]=Col[c]=1; ++ret; }
      else if (s[r][c]=='+') { assert(DiSum[r+c]==0 && DiDif[N-1+r-c]==0); DiSum[r+c]=DiDif[N-1+r-c]=1; ++ret; }
      else if (s[r][c]=='o') {
	assert(Row[r]==0 && Col[c]==0 && DiSum[r+c]==0 && DiDif[N-1+r-c]==0);
	Row[r]=Col[c]=DiSum[r+c]=DiDif[N-1+r-c]=1;
	++ret;
	++ret;
      }
    }
  }
  return ret;
}

inline void norm(int& x) {
  if (2*x>=N) x=N-1-x;
}
bool myless(pair<int,int> lhs, pair<int,int> rhs) {
  norm(lhs.first);
  norm(lhs.second);
  norm(rhs.first);
  norm(rhs.second);
  return lhs.first+lhs.second<rhs.first+rhs.second;
}

void run() {
  int M,R,C;
  char x;
  scanf("%d%d", &N, &M);
  vector<vector<char> > s(N,vector<char>(N,'.'));
  for (int i=0;i<M;++i) {
    scanf(" %c%d%d", &x, &R, &C); --R; --C;
    s[R][C]=x;
  }
  vector<char> fRow(N,true),fCol(N,true),fDiSum(2*N-1,true),fDiDif(2*N-1,true); // dif offs. by N-1
  for (int r=0;r<N;++r) {
    for (int c=0;c<N;++c) {
      if (s[r][c]=='x') { fRow[r]=false; fCol[c]=false; }
      else if (s[r][c]=='+') { fDiSum[r+c]=false; fDiDif[N-1+r-c]=false; }
      else if (s[r][c]=='o') { fRow[r]=false; fCol[c]=false; fDiSum[r+c]=false; fDiDif[N-1+r-c]=false; }
    }
  }

  vector<pair<int,int> > ord;
  for (int r=0;r<N;++r) {
    for (int c=0;c<N;++c) {
      ord.push_back(pair<int,int>(r,c));
    }
  }
  sort(ord.begin(),ord.end(),myless);

  vector<pair<char,pair<int,int> > > mods;
  for (vector<pair<int,int> >::const_iterator it=ord.begin();it!=ord.end();++it) {
    int r=(*it).first;
    int c=(*it).second;
    //    fprintf(stderr,"%d %d\n",r,c);
    if (fRow[r] && fCol[c] && fDiSum[r+c] && fDiDif[N-1+r-c]) {
      assert(s[r][c]=='.');
      s[r][c]='o';
      fRow[r]=fCol[c]=fDiSum[r+c]=fDiDif[N-1+r-c]=false;
      mods.push_back(pair<char,pair<int,int> >('o',pair<int,int>(r+1,c+1)));
    } else if (fRow[r] && fCol[c]) {
      switch(s[r][c]) {
      case '.': s[r][c]='x'; break;
      case '+': s[r][c]='o'; break;
      default: assert(false);
      }
      fRow[r]=fCol[c]=false;
      mods.push_back(pair<char,pair<int,int> >(s[r][c],pair<int,int>(r+1,c+1)));
    } else if (fDiSum[r+c] && fDiDif[N-1+r-c]) {
      switch(s[r][c]) {
      case '.': s[r][c]='+'; break;
      case 'x': s[r][c]='o'; break;
      default: assert(false);
      }	
      fDiSum[r+c]=fDiDif[N-1+r-c]=false;
      mods.push_back(pair<char,pair<int,int> >(s[r][c],pair<int,int>(r+1,c+1)));
    }
  }
  int score=calccheck(s);
  printf("%d %d\n", score, int(mods.size()));
  for (vector<pair<char,pair<int,int> > >::const_iterator it=mods.begin();it!=mods.end();++it) {
    printf("%c %d %d\n", (*it).first,(*it).second.first,(*it).second.second);
  }
}

int main() {
  int T;
  scanf("%d",&T);
  for (int t=1;t<=T;++t) {
    printf("Case #%d: ",t);
    run();
  }
  return 0;
}
