/*
tags: 
LANG: C++11
*/

#include<bits/stdc++.h> //g++ -std=c++11

using namespace std;

//#define DEBUG
#ifndef DEBUG
  #define din if(0) cin
  #define dout if(0) cout
#else
  #define din cin
  #define dout cout
#endif


#define inf (1 << 30)
#define pi (2*asin(1))
#define repall(it,A) for(typeof A.begin() it = A.begin(); it!=A.end(); it++)
#define rep(i,x,y) for (int i = x; i < y; i++)
#define irep(i,x,y) for (int i = x; i >= y; i--)
#define clr(A,x) memset(A, x, sizeof A)
#define pb push_back
#define mp make_pair
#define MAX 100005

typedef vector < int > vi;
typedef pair < long long int , long long int > pii;
typedef vector < pii > vii;
typedef long long int i64;
typedef vector < i64 > vi64;
typedef pair < pii , long long int > piii;
i64 n, k;
void print(vector < piii > v)
{
  puts("----------------");
  rep(i, 0, v.size())
  {
    cout<<v[i].first.first<< "  "<<v[i].first.second<< "  "<<v[i].second<<endl;
  }
  puts("++++++++++++++++++");
}
pii sol()
{
  vector < vector < piii > >  v = vector < vector < piii > > (2, vector < piii >());

  if(n & 1ll) //odd
    v[0].push_back(piii(pii(n/2ll, n/2ll), 1ll));
  else
    v[0].push_back(piii(pii((n - 1ll)/ 2ll, n/2ll), 1ll));
      
  int xind = 0, yind = -1;
  int tmp = 0;
  while(1)
  {
    tmp++;
    dout<< xind << " --> "<< k<<endl;
    //print(v[xind]);
    i64 ac = 0;
    map < i64, i64 > frec;
    frec.clear();
    irep(j, (int) v[xind].size() - 1, 0)
    {
      if(k - v[xind][j].second - ac <= 0ll)
      {
        yind = j;
        break;
      }
      else ac += v[xind][j].second;
      dout<<"ac : "<<ac<<"  "<< v[xind][j].second<<endl;
      frec[v[xind][j].first.first] += v[xind][j].second;
      frec[v[xind][j].first.second] += v[xind][j].second;
      dout<<"   ---> "<< v[xind][j].first.first<< " "<<frec[v[xind][j].first.first]<<endl;
      dout<<"   +++> "<< v[xind][j].first.second<< " "<<frec[v[xind][j].first.second]<<endl;
    }
    if(yind>=0)break; 
    else
    {
      v[xind xor 1].clear();
      repall(it, frec)
      {
        i64 val = it -> first;
        i64 cnt = it -> second;
        if(val == 0ll) continue;
        
        dout<< val<< " * "<< cnt<<endl;
        
        if(val & 1ll) //odd
        {
          dout<<"en1"<<endl;
          v[xind xor 1].push_back(piii(pii(val/2ll, val/2ll), cnt));
        }  
        else
        {
          dout<<"en2"<<endl;
          v[xind xor 1].push_back(piii(pii((val - 1ll)/2ll, val/2ll), cnt));
        }
      }
      k -= ac;
    }
    dout<< xind << " ++> "<< k<<" "<<ac<<endl;
    xind = xind xor 1;
  }
  dout<<tmp<<endl;
  return v[xind][yind].first;
}
int main() 
{
  int test;
  scanf("%d", &test);
  rep(te, 1, test+1)
  {
    cin>>n>>k;
    dout<<"input "<<n<<"  "<< k<<endl;
    pii ans  = sol();
    printf("Case #%d: ", te);
    cout<<ans.second<<" "<<ans.first<<endl;
  }
}
