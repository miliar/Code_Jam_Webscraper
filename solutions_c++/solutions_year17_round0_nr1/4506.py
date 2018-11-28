

#include <iostream>
#include <vector>
#include <cstdio>
#include <cstring>

#define FOR(I,A,B) for(int I = (A); I < (B); ++I)

using namespace std;



	



int main(int argc, char **argv)
{
    
    //freopen("A-large-practice.in", "r", stdin);
    //freopen("a-large.out", "w", stdout);
        
    freopen("A-small-attempt1.in", "r", stdin);
    freopen("A-small1.out", "w", stdout);

	char S[1000];
	int K;
	  
    int T; cin >> T;
        
    FOR(ts, 1, T+1){
		
		int nfl=0;
		int np=0;
		
		getchar();
		do{
			S[np] = getchar();
			np++;
		}while (S[np-1]=='+' || S[np-1]=='-');
		//while (S[np] != char(32));
		np--;
		
		cin >> K; 
		//FOR(i,0,np) cout << S[i]; cout << endl;
		
		
		
		
		int i=0;
		do{
			if (S[i]=='-'){
				
				nfl++;
				FOR(j,0,K){
						if (S[i+j]=='-') S[i+j]='+'; else S[i+j]='-';
				}
				//FOR(i,0,np) cout << S[i]; cout << endl;
			} 	
			i++;	
		} while (i <= np-K);


	 while (S[i]=='+' && i<np) {
		 i++;
	 } ;
	 
	 if (i==np) 	 
		cout << "Case #" << ts << ": " << nfl << endl;
	 else
		cout << "Case #" << ts << ": IMPOSSIBLE" << endl;
	
	    //cout << "i: " << i << "   nflips: " << nfl << endl << endl << endl;
        
    }
  
  
  
    return 0;
}

