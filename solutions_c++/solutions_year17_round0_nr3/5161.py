#include<fstream>
#include<iostream>
#include<algorithm>
#include<string>

using namespace std;

long long find(long long K)
{   long long x=1;
    
     while(K>x)
     {   x*=2;}
     
   if(K==x) return x;
   else 
   return x/2;   
}
   

void solve(long long N, long long K, long long &res1, long long &res2)
{
   
    long long remain=N-K+1;
    
    long long a=find(K);
    double y=1.0*remain/a;
    long long x=remain/a;
    if(y-x>0) x++;
    if(x%2==0) { res1=x/2; res2=x/2-1;}
    else { res1=(x-1)/2; res2=res1;}
    
    
   
}


int main()
{ 
 int n,i,j;
  long long N,K,res1,res2;
  ofstream output;
  output.open("outputCb.txt");
  
  ifstream input;
  input.open("C-small-2-attempt1.in");
  input>>n;
  cout<<n<<endl;
 
  for(j=1;j<=n;j++)
  { //input>>s; //cout<<s<<endl;
    input>>N>>K;
         
    solve(N,K,res1,res2);
    output<<"Case #"<<j<<": "<<res1<<" "<<res2<<endl; 
    cout<<j<<endl;

  }
  
 input.close();
 output.close();
//long long a,b;
//solve(1000,1,a,b);
//cout<<a<<" "<<b<<endl;
   return 0;
}
