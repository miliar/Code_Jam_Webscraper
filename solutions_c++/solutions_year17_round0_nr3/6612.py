/*
 * Boilerplate for Google Gode Jam work
 * version 1.0
 * 2017 QR - B
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
   	unsigned long long 	rst1=0,rst2=0,N=0,K=0,J=0,R=0,C=0,P=0,st[1002];  	
    Fi(0,1001) st[i]=0;
   
   	// Print "Case #t: "
   	cout << "Case #" << t << ": "; 
   	//---------------- 1 int -----------
	//cin >> R;
   	//-----------------2 ints ----------
	cin >> N >> K;
	st[0]=1; st[N+1]=1; 
	//test
	//st[11]=st[22]=st[33]=st[64]=st[95]=st[97]=st[99]=1;
	//
	unsigned long long minlr = 0, maxlr = 0;
	   
	J=K;
	while(J){
	   int f=0;
	   unsigned long long ad=0,mc=0,g = 0;
	   unsigned long long a0=0;
	   Fi(0,N+1){
	    if(st[i]==1){
	    	if(f==1){
	    	    if(ad > g){
	    	    	mc=1; g = ad;
	    	    	a0=i;
	    	    }else if(ad == g){
	    	    	mc++;
	    	    }else{
	    	    	
	    	    }
	    		ad=0; f=0;
	    	}
	    }else{
	      ad++; f=1;
	    }	
	   }
	   a0-=(g+1);
	   //cout << "a01= " << a0 << " ";
	   
	   if(g<=1){
	   	minlr=maxlr=0;
	   	}else if(g==2){
	   		minlr=0; maxlr=1;
	   	}else{
	   		if(g%2==1){
	   			minlr = (g-1)/2;
	   			maxlr = (g-1)/2;
	   		}else{
	   			minlr = g/2 -1;
	   			maxlr = g/2;
	   		}
	   	}
	   	a0+=(minlr+1);
	   	st[a0]=1;
	   	
	    //cout << "g= " << g << " mc=" << mc << " a0=" << a0 << endl;
	   J--; 
	}
	
	

    
  
    cout << maxlr << " " << minlr << endl;
    
    
   	//---------------- 1 str (no space)-
	//cin >> S;
   	//---------------- N line str ----
	//Fi(1,N){cin >> ss[i];	}
   	//---------------- N cont. ints ----
   	//Fi(1,N){cin >> F[i];	}
   	//----------------------------------
   	
   




   	/************/
   	return 0;
}

int main(){
  int T; 
  cin >> T; 
  Fi(1,T) xcase(i);
  return 0;
}
