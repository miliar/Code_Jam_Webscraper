#include <iostream> 
#include <cmath> 
using namespace std; 
int checktidy(long long int a) 
{
 if(a/10==0) return 1;
 if((a%10)<((a/10)%10)) return 0;
 return checktidy(a/10); } long long int ct(long long int a) { int i; long long int c=1; for(i=0;i<20;i++) { if(checktidy(a)==1) return a; else{ c=c*10; a=(a-(a%c)-1);} } } int main() { int i=1,t; long long int a; cin>>t; while(t--) { cin>>a; cout << "Case #" << i << ": " <<ct(a)<<endl;i++; } return 0; }
