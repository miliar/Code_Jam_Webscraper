#include <iostream>
using namespace std;
 
int main ()
{
   freopen("B-small-attempt0.in", "r", stdin);
   freopen("B-small-attempt0.out", "w", stdout);
   int T, N;
   cin >> T;
   
   for( int i = 1; i <= T; i = i + 1 ) 
   {
       char c;
       int Data[100];
       int Len, k;
       
       //input
       k = 1;
      
       c=cin.get();
       while ((c < '0') || (c > '9')) { c = cin.get();}
       //cout << c <<endl;
       while ((c>='0') && (c<='9'))
       {
        	Data[k] = (int)(c - '0'); 
            k = k + 1;
            c=cin.get();
       }
       
       Len = k-1;
       //cout << endl <<Len << endl;
       
       //compare
       for ( int k = Len-1; k >= 1; k = k -1) 
       {
        if ( Data[k] > Data[k+1] )
        {
         Data[k] = Data[k]-1;
         for (int j = k+1; j <= Len; j = j + 1 )
         {
         	Data[j]=9;
         }
        }
       }
       
       //print out
       cout << "Case #" <<i<<": ";
       k = 1;
       while (Data[k] ==0) {k++;}
       for (int j = k; j<=Len; j = j+1 )
       {
         cout << Data[j];
       }
       cout << endl;
   
   }
   
    
 return 0;
}