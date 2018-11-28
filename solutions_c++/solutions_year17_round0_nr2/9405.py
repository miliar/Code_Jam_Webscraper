//

//  main.cpp

//  coding is back

//

//  Created by VERDU SANJAY on 23/01/17.

//  Copyright © 2017 VERDU SANJAY. All rights reserved.

//



#include <iostream>
#include<string.h>
#include<map>
#include<math.h>
#include<stdlib.h>
#include<vector>
#include<algorithm>
#include<stack>
#include<time.h>
#include<fstream>
#define mod 1000000007

using namespace std;

typedef long long ll;

using namespace std;

map<string,string> mp;

ll mark[100003] = {0};


int modInverse(int a, int m)
{
    a = a%m;
    for (int x=1; x<m; x++)
       if ((a*x) % m == 1)
          return x;
}

int power(int x, unsigned int y)
{
    int res = 1;     // Initialize result
 
    while (y > 0)
    {
        // If y is odd, multiply x with result
        if (y & 1)
            res = res*x;
 
        // n must be even now
        y = y>>1; // y = y/2
        x = x*x;  // Change x to x^2
    }
    return res;
}

int main(){
   
  freopen("B-small-attempt2.in","r",stdin);
   
   freopen("output.txt","w",stdout);
    
  ll t,n;
  
  ll i,j;
  
  ll p,k;
  

cin >> t;  
  ll b = 1;
  
  ll count = 0;
  
  while(t--){
  	
  	cin >> n;
  	
  	count = 0;
  	
  	ll k = n;
  	
  	while(k!=0){
  		
  		k = k/10;
  		count++;
	  }
  
  for(i=count-1;i>=0;i--){
  	
  	
  	mark[i] = n%10;
  	n = n/10;
  	
  }
  
  for(i=count-1;i>=0;i--){
  	
  	if(mark[i-1] > mark[i]){
  		
  		mark[i-1]--;
  		
  		for(j = i;j<count;j++){
  			
  			mark[j] = 9;
		  }
  		
	  }
  	
  }
  
  
  
  if(mark[0]!=0){
  		cout << "Case #" << b << ": " ;
  	
  	for(i = 0;i<count;i++){
  		
  	cout<<mark[i];	
  		
	  }
	  	b++;;
	  cout << endl;
  	
  }else{
  	
  		cout << "Case #" << b << ": ";
  	for(i=1;i<count;i++){
  		
  	cout<<mark[i];
	  }
	  b++;
	  cout << endl;
  }
}
}
