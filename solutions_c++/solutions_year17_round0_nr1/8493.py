/*
 * Boilerplate for Google Gode Jam work
 * version 1.0
 * 2017 QR - A
 */
#include<algorithm>
#include<bitset>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<ctime>
#include<iostream>
#include<map>
#include<queue>
#include<set>
#include<vector>

// Useful Macro
#define INFNAME  "in"
#define OUTFNAME "out"
#define Fi(a,b) for(int i=a;i<=b;i++)
#define Fj(a,b) for(int j=a;j<=b;j++)
#define Fk(a,b) for(int k=a;k<=b;k++)
#define Fl(a,b) for(int l=a;l<=b;l++)

using namespace std;

int xcase(int t){
   	int 	rst=0,N=0,K=0,J=0,R=0,C=0,P=0;
   	
   	int		F[1001],G[1001];   	
   	bool	B[1001];
   	//Fi(0,1000){
   	//	F[i]=0;G[i]=0;B[i]=false;
   	//}
   	char	S[11],T[51];
    S[0]=0;T[0]=0;
    char    ss[1001][51];
    //Fi(0,1000) ss[i][0]=0;
   
   	// Print "Case #t: "
   	cout << "Case #" << t << ": "; 
   	//---------------- 1 int -----------
	//cin >> R;
   	//-----------------2 ints ----------
	//cin >> R >> C;
   	//---------------- 1 str (no space)-
	cin >> S >> K;
	
	  int l = strlen(S);
	  int c=0,d=0;
	  Fi(0,l-K) {
	     if(S[i]=='+') continue;
	     Fj(0,K-1){
	       S[i+j]=(S[i+j]=='+'?'-':'+');
	     }
	     c++;
	   }
	//cout << "1):" << S << endl;
	
    Fi(l-K,l-1){
      if(S[i]=='-'){
        cout << "IMPOSSIBLE" << endl;
        return 0;
      }
    }
	   	
	
   	//---------------- N line str ----
	//Fi(1,N){cin >> ss[i];	}
   	//---------------- N cont. ints ----
   	//Fi(1,N){cin >> F[i];	}
   	//----------------------------------
   	
   
     cout << c << endl;
   	
   	/************/
   	return 0;
}

int main(){
  int T; 
  cin >> T; 
  Fi(1,T) xcase(i);
  return 0;
}
