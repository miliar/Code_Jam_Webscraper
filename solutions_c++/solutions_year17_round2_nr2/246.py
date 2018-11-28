#include <stack>
#include <sstream>
#include <queue>
#include <iostream>
#define REP(i,n) for(int i=0; i<(int)(n); i++)

#include <cstdio>
inline int getInt(){ int s; scanf("%d", &s); return s; }

#include <set>

using namespace std;

string repeat(string s, int cnt){
  stringstream ss;
  REP(i,cnt) ss << s;
  return ss.str();
}

int main(){
  const int t = getInt();
  REP(c,t){
    const int n = getInt();

    int r = getInt();
    int o = getInt();
    int y = getInt();
    int g = getInt();
    int b = getInt();
    int v = getInt();

    const char * impossible = "IMPOSSIBLE";
    printf("Case #%d: ", c + 1);

    if(o + y + b + v == 0){
      if(r == g){
	REP(i,r) printf("RG"); puts("");
      }else{
	puts(impossible);
      }
    }else if(r + o + g + b == 0){
      if(y == v){
	REP(i,y) printf("YV"); puts("");
      }else{
	puts(impossible);
      }
    }else if(r + y + g + v == 0){
      if(b == o){
	REP(i,b) printf("BO"); puts("");
      }else{
	puts(impossible);
      }
    }else{
      stack<string> rs, ys, bs;

      if(g != 0){
	rs.push(repeat("RG", g) + "R");
	r -= g + 1;
      }

      if(v != 0){
	ys.push(repeat("YV", v) + "Y");
	y -= v + 1;
      }

      if(o != 0){
	bs.push(repeat("BO", o) + "B");
	b -= o + 1;
      }

      if(r < 0 || y < 0 || b < 0){
	puts(impossible);
      }else{
	REP(i,r) rs.push("R");
	REP(i,y) ys.push("Y");
	REP(i,b) bs.push("B");

	vector<stack<string> > v;
	const int mx = max(max(rs.size(), ys.size()), bs.size());

	char last;
	if(mx == (int)rs.size()){
	  v.push_back(rs);
	  v.push_back(ys);
	  v.push_back(bs);
	  last = 'Y';
	}else if(mx == (int)ys.size()){
	  v.push_back(ys);
	  v.push_back(rs);
	  v.push_back(bs);
	  last = 'B';
	}else{
	  v.push_back(bs);
	  v.push_back(rs);
	  v.push_back(ys);
	  last = 'R';
	}

	stringstream ans;
	while(v[0].size() + v[1].size() + v[2].size() > 0){
	  const int mx = max(max(v[0].size(), v[1].size()), v[2].size());

	  bool done = false;
	  REP(i,3) if((int)v[i].size() == mx){
	    if(v[i].top()[0] != last){
	      ans << v[i].top();
	      last = v[i].top().back();
	      v[i].pop();
	      done = true;
	      break;
	    }
	  }

	  if(done) continue;

	  vector<stack<string> *> vs;
	  REP(i,3) if(v[i].size() != 0 && v[i].top()[0] != last)
	    vs.push_back(&v[i]);

	  if(vs.size() == 1){
	    ans << vs[0]->top();
	    last = vs[0]->top().back();
	    vs[0]->pop();
	  }else if(vs.size() == 2){
	    const int idx = vs[0]->size() >= vs[1]->size() ? 0 : 1;
	    ans << vs[idx]->top();
	    last = vs[idx]->top().back();
	    vs[idx]->pop();
	  }else{
	    puts(impossible);
	    goto loop;
	  }
	}

	const string s = ans.str();
	if(s[0] != s[s.size() - 1]){
	  puts(s.c_str());
	}else{
	  puts(impossible);
	}
      }
    }
  loop:;
  }
  return 0;
}

