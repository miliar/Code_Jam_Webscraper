/*
  name 			:- Rajat Sharma
  college 			:- GEC,Ajmer
  codechef		:- dragon_ball
  spoj				:- rajat189
  hackerearth	:- er.rajat.sharma9
  hackerrank		:- rajat_sharma
  project_euler	:- rajat189
  codeforce		:- rajat189
  moto 				:- sometimes i feel like giving up then i remember
        					i have a lot of motherfu*ckers to prove wrong!
*/
#include <bits/stdc++.h>
#include <algorithm>
#include <bitset>
#include <deque>
#include <cassert>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <utility>
#include <vector>

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pi;
typedef vector<string> vs;

// Basic macros
#define pii         pair<ll,ll>
#define inf         INT_MAX
#define st          first
#define se          second
#define all(x)      (x).begin(), (x).end()
#define ini(a, v)   memset(a, v, sizeof(a))
#define re(i,s,n)  	for(int i=s;i<(n);++i)
#define rep(i,s,n)  for(int i=s;i<=(n);++i)
#define fr(i,n)     re(i,0,n)
#define repv(i,f,t) for(int i = f; i >= t; --i)
#define rev(i,f,t)  repv(i,f - 1,t)
#define frv(i,n)    rev(i,n,0)
#define pu          push_back
#define mp          make_pair
#define sz(x)       (int)(x.size())
#define s(x) scanf("%d",&x)
#define i64 long long
#define gc() getchar()
inline i64 readLLD()
{
  i64 ret=0;
  bool negg=false;
  char c;
  c=gc();
  while((c<'0' || c>'9') && c!='-')
  {
    //scanf("%c",&c);
    c=gc();
  }
  if(c=='-'){negg=true;c=gc();}
  while(c>='0' && c<='9')
  {
    ret=ret*10+(c-'0');
    c=gc();
  }
  if(negg){ret=-ret;}
  return ret;
}//=readLLD();
inline int readInt()
{
  int ret=0;
  bool negg=false;
  char c;
  c=gc();
  while((c<'0' || c>'9') && c!='-')
  {
    c=gc();
  }
  if(c=='-')
  {
    negg=true;
    c=gc();
  }
  while(c>='0' && c<='9')
  {
    ret=ret*10+(c-'0');
    c=gc();
  }
  if(negg)
  {
    ret=-ret;
  }
  return ret;
}//=readInt();
bool cross(pi, pi, int d);
int main(){
    int t=readInt();
    rep(tCase,1,t){
        int n=readInt();
        pair<int, char> c[6];
        re(i,0,6){
            cin>>c[i].st;
        }
        c[0].se='R';
        c[1].se='O';
        c[4].se='B';
        c[5].se='V';
        c[2].se='Y';
        c[3].se='G';
        sort(c,c+6,greater<pair<int,char>>());
        string s1;
        if ( (c[1].st + c[2].st)<c[0].st){
            cout<<"Case #"<<tCase<<": IMPOSSIBLE"<<endl;
            continue;
        }
        if((c[2].st+c[1].st-c[0].st)%2==1){
            s1.pu(c[1].se);
            c[1].st--;
        }
        int diff=(c[2].st+c[1].st-c[0].st)/2;
        re(i,0,c[0].st){
            s1.pu(c[0].se);
            if (c[2].st<(c[0].st - i + diff ))s1.pu(c[1].se);
            else s1.pu(c[2].se);
        }
        re(i,0,diff){
            s1.pu(c[1].se);
            s1.pu(c[2].se);
        }
        cout<<"Case #"<<tCase<<": "<<s1<<endl;
    }
    return 0;
}
