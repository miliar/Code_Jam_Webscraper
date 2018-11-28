#include <bits/stdc++.h>
using namespace std;
#define fori(n) for(int i=0;i<n;i++)
#define for0(i,n) for(int i=0;i<n;i++)
#define forit(i, c) for (__typeof__((c).begin()) i = (c).begin(); i != (c).end(); i++)
char cake[30][30];

int main()
{
  int T,t;
  cin >> T;
  t=T;
  int R,C;

  while(T--)
  {
    cin>> R>>C;
    for0(i,R) 
    for0(j,C) cin>>cake[i][j];
  
	for0(i,R)
    for0(j,C)
    {
      if(cake[i][j]!='?' &&cake[i][j+1]=='?') cake[i][j+1]=cake[i][j]; 	
    }
 
    for0(i,R)
    for(int j=C-1;j>=1;j--)
    {
	if(cake[i][j]!='?' && cake[i][j-1]=='?') cake[i][j-1]=cake[i][j];
	}

    for0(i,R)
    for0(j,C)
    {
      if(cake[i][j]!='?' &&cake[i+1][j]=='?') cake[i+1][j]=cake[i][j]; 	
    }
    
    for(int i=R-1;i>=1;i--)
    for0(j,C)
    {
      if(cake[i][j]!='?' &&cake[i-1][j]=='?') cake[i-1][j]=cake[i][j]; 	
    }
    
  
  
  cout <<"Case #"<<t-T<<":\n";
  for0(i,R) 
    {for0(j,C) printf("%c",cake[i][j]);
     if(i!=R-1) cout <<endl;
    }
    if(t>0) cout <<endl;
  }

	
	return 0;
	
	
	
	
}
