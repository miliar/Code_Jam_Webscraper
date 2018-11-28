#include <iostream>
#include <iomanip>
#include <vector>

using namespace std;

struct Case {
  int t, i;
  Case() : i(0) { cin >> t; }
  bool next() { return i++ < t; }
} T;
ostream& operator<<(ostream& o, const Case &i) { o<<"Case #"<<i.i<<": "; return o; }

vector<char> genlist(const char *c, int x, int y, int z) {
  vector<char> l(x, c[0]);
  vector<char> l1, l2;
  for (char t: l) {
    l1.push_back(t);
    if (t==c[0] && y) {
      l1.push_back(c[1]); y--;
    }
  }
  reverse(l1.begin(), l1.end());
  for (char t: l1) {
    if (t==c[0] && z) {
      // cerr<<c[2];
      l2.push_back(c[2]); z--;
    }
    // cerr<<t;
    l2.push_back(t);
  }
  // cerr<<endl;
  reverse(l2.begin(), l2.end());
  return l2;
}

int main() {
  cout<<fixed<<setprecision(10);
while (T.next()) {
  int n, r, o, y, g, b, v;
  cin >> n >> r >> o >> y >> g >> b >> v;
  // BOBOB...
  // RGRGR...
  // YVYVY...
  // BRY...
  cout<<T;
  if (n==1) {
    if (b) cout<<"B";
    else if (o) cout<<"O";
    else if (r) cout<<"R";
    else if (g) cout<<"G";
    else if (y) cout<<"Y";
    else if (v) cout<<"V";
    cout<<endl;
    continue;
  }
  if ((b+o>0) + (r+g>0) + (y+v>0) == 1) {
    cerr<<"balance"<<endl;
    if (b+o > 0 && b == o) {
      for (int i=0;i<o;i++) cout<<"OB";
    } else if (r+g>0 && r == g) {
      for (int i=0;i<g;i++) cout<<"GR";
    } else if (y+v>0 && y == v) {
      for (int i=0;i<v;i++) cout<<"VY";
    } else {
      cerr<<b<<" "<<o<<" "<<r<<" "<<g<<" "<<y<<" "<<v<<endl;
      cout<<"IMPOSSIBLE";
    }
    cout<<endl;
    continue;
  }
  if ((o && b <= o) || (g && r <= g) || (v && y <= v)) {
    cerr<<"err1: "<<b<<" "<<o<<" "<<r<<" "<<g<<" "<<y<<" "<<v<<endl;
    cout<<"IMPOSSIBLE"<<endl;
    continue;
  }
  b-=o;r-=g;y-=v;
  if (b>r+y || r>b+y || y>r+b) {
    cerr<<"err2: "<<b<<" "<<o<<" "<<r<<" "<<g<<" "<<y<<" "<<v<<endl;
    cout<<"IMPOSSIBLE"<<endl;
    continue;
  }
  vector<char> l;
  if (b>=r && b>=y) {
    l=genlist("BRY", b, r, y);
  } else if (r>=b && r>=y) {
    l=genlist("RBY", r, b, y);
  } else if (y>=b && y>=r) {
    l=genlist("YRB", y, r, b);
  } else {cout<<1/0;}
  for (auto c: l) {
    cout<<c;
    if (c=='B' && o) {
      for (int i=0;i<o;i++) cout<<"OB";
      o=0;
    } else if (c=='R'&&g) {
      for (int i=0;i<g;i++) cout<<"GR";
      g=0;
    } else if (c=='Y'&&v) {
      for (int i=0;i<v;i++) cout<<"VY";
      v=0;
    }
  }
  cout<<endl;
}
}
