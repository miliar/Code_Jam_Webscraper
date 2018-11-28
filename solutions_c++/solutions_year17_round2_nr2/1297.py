#include <iostream>
#include <string>

using namespace std;

int cas, N, R, O, Y, G, B, V;

string x[3];

string sol(int a, int b, int c) {
  string s="";
  if (a>b+c) return s;

  int bb=b, nn=b+c-a, cc=c-nn;
  for (int i=0; i<a; ++i) {
    s+=x[0];
    if (bb) {
      s+=x[1]; --bb;
      if (nn) {s+=x[2]; --nn;}
    }
    else if (cc) {
      s+=x[2]; --cc;
    }
    else cout<<"error\n";
  }
  if (bb||cc||nn) cout<<"error2\n";
  return s;
}

int main() {
  cin>>cas;

  for (int k=1; k<=cas; ++k) {
    cin>>N>>R>>O>>Y>>G>>B>>V;
    x[0]="R"; x[1]="Y"; x[2]="B";
    int a=R, b=Y, c=B, ix;
    string sx;
    if (a<b) {ix=a; a=b; b=ix; sx=x[0]; x[0]=x[1]; x[1]=sx;}
    if (a<c) {ix=a; a=c; c=ix; sx=x[0]; x[0]=x[2]; x[2]=sx;}
    if (b<c) {ix=b; b=c; c=ix; sx=x[1]; x[1]=x[2]; x[2]=sx;}

    cout<<"Case #"<<k<<": ";
    sx=sol(a,b,c);
    if (sx=="") cout<<"IMPOSSIBLE\n";
    else cout<<sx<<endl;
  }
  return 0;
}
