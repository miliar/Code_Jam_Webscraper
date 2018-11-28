
#include <iostream>  // includes cin to read from stdin and cout to write to stdout
using namespace std;  // since cin and cout are both in namespace std, this saves some text
// constructing priority queues
#include <iostream>       // std::cout
#include <queue>          // std::priority_queue
#include <vector>         // std::vector
#include <functional>     // std::greater
#include <algorithm>    // std::max


int main() {
  int t, R, C;
  t = 1;
  cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
  for (int x = 1; x <= t; ++x)
  {
     cin >> R >> C;
     std::vector< std::vector<char> > s(R, std::vector<char>(C));
     std::string a;
     for (int i=0; i < R; i++)
     {
        cin >> a;
        for(int j=0; j<C; j++)
           s[i][j] = a[j];
     }
     
     for (int i=0; i < R; i++)
     {
        char str = 'x';
        bool first = true;
        for(int j=0; j<C; j++) 
        {
           if(s[i][j]=='?')
             s[i][j] = str;
           else 
           {
             str = s[i][j];
             if(first==true) 
             {
        	first = false;
        	for(int k=0; k<j; k++)
        	   s[i][k] = str;
             }    
           }
           
     	}
     }
     for (int i=0; i < R; i++)
     {
        if(s[i][0]=='x') 
          if(i==0) 
        	  for (int k=0; k<C; k++) {
        		  s[i][k] = s[i+1][k];
        	  }
          else 
        	  for (int k=0; k<C; k++) 
        	  {
        		  s[i][k] = s[i-1][k];
        	  }
     }

	for (int i=0; i < R; i++) {
		if(s[i][0]!='x'){
			for(int m = i-1; m>=0; m--) {
				for(int n = 0; n<C; n++) {
					s[m][n] = s[m+1][n];
				}
			}
			break;
		}
	}



     cout << "Case #" << x << ":" << endl;

     for (int i=0; i < R; i++) {
        for(int j=0; j<C; j++)  {
        	cout << s[i][j] ;
        }
    	cout << endl;
     }

  }
}


