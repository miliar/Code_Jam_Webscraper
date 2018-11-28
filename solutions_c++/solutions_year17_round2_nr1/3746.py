#include<fstream>
#include<iostream>
#include<algorithm>
#include<string>
#include<iomanip>

using namespace std;




int main()
{ 
 int n,i,j,k;
  int N,P,a,b;
  double t,value,mini;
  
 
  ofstream output;
  output.open("outa-la-0.txt");
  
  ifstream input;
  input.open("/home/hong/Downloads/A-large.in");
  input>>n;
  cout<<n<<endl;
 
  for(j=1;j<=n;j++)
  { //input>>s; //cout<<s<<endl;
    input>>N>>P; cout<<N<<" "<<P<<endl;
   // mini=2147483647;
    mini=1.7E308;
    for(i=0;i<P;i++)
      {                     
         input>>a>>b;// cout<<a<<" - "<<b<<endl;
         t=1.0*(N-a)/b;
         value=a/t+b;
         if(value<mini) mini=value;
      }
   
     cout<<"Case #"<<j<<": "<<fixed<<setprecision(6)<<mini<<endl; 
    output<<"Case #"<<j<<": "<<fixed<<setprecision(6)<<mini<<endl; 
    

  }
  
 input.close();
 output.close();
//long long a,b;
//solve(1000,1,a,b);
//cout<<a<<" "<<b<<endl;
   return 0;
}
