//GAURAV BHOLLA ASET
#include<iostream>
#include<string.h>
using namespace std;
const int INFINITY = 20000000;


int flips(int a[], int M, int N, int want) {
  int s[M]; 
  for(int i=0,_n=M; i<_n; ++i)
  s[i] = 0;
  
  
  int sum=0, ans=0;
	for(int i=0,_n=M; i<_n; ++i){
    s[i] = (a[i]+sum)%2 != want;
    sum += s[i] - (i>=N-1?s[i-N+1]:0);
    ans += s[i];
    if(i>M-N and s[i]!=0)
	{return INFINITY;}
  }
  return ans;
}
typedef long long int ll;
int main()
{
    ll t,m=0,p=0,s=0,c=0,T=0;
    cin>>t;
    while(++T<=t)
     {	
           char a[1500];
            cin>>a;
			
          ll length=strlen(a);
         cin>>s;
         int A[length];
         for(ll i=0;i<length;i++)
          { if(a[i]=='-')
            A[i]=0;

            else
            A[i]=1;
            
          }
          
//MAIN CHECKING
     
  	ll ANS=flips(A, length, s, 1);
  
     if(ANS==20000000)
     cout<<"Case #"<<T<<": IMPOSSIBLE\n";

     else{
		cout<<"Case #"<<T<<": "<<ANS<<"\n";
     }
}
    return 0;
}
