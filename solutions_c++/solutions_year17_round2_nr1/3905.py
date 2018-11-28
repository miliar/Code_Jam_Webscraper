#include<iostream>
#include <conio.h>
#include<limits.>

#include <math.h>
#include <string.h>
#include <stdlib.h>
#include<stdio.h>
#define F0(i,n) for(int i=0;i<n;i++)
#define F1(i,n) for(int i=1;i<=n;i++)
using namespace std;
typedef long long ll;
#define SZ(x) (int)(x.size())
#define F0(i,n) for(int i=0;i<n;i++)
#define F1(i,n) for(int i=1;i<=n;i++)
#define Fj(i,j,n) for(int i=j;i<=n;i++)    
#define Fr(i,j,n) for(int i=j;i>=n;i--)    
const int MOD = 1000002013;
const double pi = atan(1.0)*4.0;
const double eps = 1e-8;
ll gcd(ll x, ll y) { return y ? gcd(y, x%y) : x; }
int bc(int n) { return n ? bc((n-1)&n)+1 : 0; }
int ctoi(char k){ if(k=='O') return 0;if(k=='1') return 1;if(k=='2') return 2;if(k=='3') return 3;if(k=='4') return 4;
                  if(k=='5') return 5;if(k=='6') return 6;if(k=='7') return 7;if(k=='8') return 8;if(k=='9') return 9;
                    return '0';}
int i, j, k, m, n, l;
int cnt[1000];
int v[1000];
char compare (const void * a, const void * b)
{
  return ( *(char*)a - *(char*)b );
}
void sortchar(char ch[],int p)
{
    F1(i,p){
        Fj(j,i,p){
          if(ch[i]>ch[j])
          {
              char t=ch[i];
              ch[i]=ch[j];
              ch[j]=t;
          }  
        }
    }
}
int main() {
   // typedef std::numeric_limits< double > dbl;

//double d = 3.14159265358979;
//cout.precision(dbl::max_digits6);

    	freopen("C:/Users/kailash/Desktop/myprogram/a77.in", "r", stdin);	
        freopen("C:/Users/kailash/Desktop/myprogram/a88.out", "w", stdout);
	double tt, tn, dist,noh,d1,speed,time,remian,var;
     cin >> tn;
   F1(tt,tn){
      
    cin>>dist;
    cin>>noh;
    double slow=0;
    F1(i,noh)
    {
        cin>>d1;
        remian=dist-d1;
        cin>>speed;
        time=remian/speed;
        if(slow<time)
            slow=time;
    }
    var=dist/slow;
   // cout << "Pi: " << fixed << d << endl;
    cout<<"Case #"<<tt<<": ";
    printf("%.6f", var);
    cout<<endl;
   }
            //cout<<endl;
 
    
  /*  n=6;
   int values[]={10,5,4,3,12,1};
   qsort(values,6,sizeof(int),compare);
    F0(i,n)cout<<values[i];*/
    getch();	return 0;
}
