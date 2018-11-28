#include <cstdio>
#include <vector>
#include <algorithm>
#include <fstream>
#include <windows.h>
#include <iostream>
#include <math.h>
#include <istream>
#include <string.h>
#include <string>
#include <map>
#include <iomanip>
#include <deque>
#include <sstream>
#include <cmath>
#include <ctgmath>

using namespace std;

#define For(i,j,s) for(int i=j; i<s; i++)
#define FOR1(i,s) for(int i=1; i<=s; i++)
#define IA(a,b) if(a&&b)
#define IGE(a,b) if(a>=b)
#define IE(a,b) if(a==b)

#define All(v) v.begin(), v.end()
#define cn continue;
#define gli getline


#define ll long long int
#define ld long double


#define L ifstream nl("A-large-practice.in");  nl1.open ("examplel.txt"); nl>>r;
#define L_ ifstream nl("A-small-practice.in"); nl1.open ("example.txt"); nl>>r;
#define J  ofstream nl1;
#define U ll n=0,i=0,c=0,e=0,s=0,r,r0=0,r1=0,r2=0,r3=0,r4=0,r5=0,r6=0,r7=0,r8=0,n1=0,n2=0,n3=0,n4=0,n5,n6; \
          flo nn=0.0f,ii=0.0f,cc=0.0f,ee=0.0f,ss=0.0,rr=0.0; \
          string st,str; \
          bool n_=false,i_=false,c_=false,e_=false,s_=false; \
          ld sss=0L;

#define ou nl1<<"Case #"<<wnri<<": "<<
#define se ShellExecute(0,"open","notepad++","" ,"",1);

#define N 1000000

#define vivi(a,b) vector<vector<ll> > vivi(a, vector<ll>(b));
#define vivi2(a,b) vector<vector<ll> > vivi2(a, vector<ll>(b));

#define _s st[i]

typedef int its;
typedef float flo;
typedef pair<int,int> par;
typedef pair<ll , ll> parl;
typedef pair<flo, flo> parf;
typedef vector<ll> vi;
typedef vector<string> vis;
typedef vector<flo>  vf;
typedef vector<long double>  vd;


typedef vector<pair<ll,ll> > parlvi;
typedef vector<pair<flo,flo> > parfvi;

int mx(int a,int b){if(a>b) return a; else return b;}

bool isprime(int a){for(int i=2; i<a;i++){if((a%i)==0) return false;} if(a!=0&&a!=1) return true; else return 0;}

ll whatisformod10(int mod,int n){vi vix(10);
              For(j,0,100) {if(n>=mod) {vix[j]=n%mod; n=n/mod;}
                                        else { vix[j]=n; For(j_,j+1,100) {vix[j_]=0; j++;}}}

              ll s=0;
              For(i,0,100) s+=pow(10,i)*vix[i]; return s;}
