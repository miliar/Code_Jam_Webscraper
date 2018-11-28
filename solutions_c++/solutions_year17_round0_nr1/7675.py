#include <iostream>
#include <string>
using namespace std;
 
int main ()
{
  //freopen("A-small-attempt0.in", "r", stdin);
  // freopen("A-small-attempt0.out", "w", stdout);
   int T;
   cin >> T;
   //cout <<T <<endl;
   
   for( int i = 1; i <= T; i = i + 1 ) 
   {
       
       char c;
       int S[100];
       int Len, K, num;
       
       //input
       int j = 1;
      
       c=cin.get();
       while ((c != '+') && (c != '-')) { c = cin.get();}
       //cout << c <<endl;
       
       while ((c=='+') || (c=='-'))
       {
        	if (c=='+') {S[j] = 1;} 
        	else {S[j]=0;}
            j = j + 1;
            c=cin.get();
       }
       
       Len = j-1;
       //cout << endl <<Len << endl;
       
       //compute
       cin >> K;
       num=0;
       
       for ( int j = Len; j >= K; j = j -1) 
       {
        if (S[j] ==0)
        {
        	num++;
        	for (int m = j; m>=j-K+1; m--)
        	{
        		if (S[m]==0) {S[m]=1;}
        		else {S[m]=0;}
        	}
        }
       }
       
       //print out
       cout << "Case #" <<i<<": ";
       int m=1;
       for (j=1; j<=K; j++)
       {
       	//cout<<S[j];
       	if (S[j]==0) {m=0;}
       }
       
       if (m==1) {cout<< num<<endl;}
       else {cout <<"IMPOSSIBLE" <<endl;}
       
       
   
   }
   
    
 return 0;
}